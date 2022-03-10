from http import HTTPStatus
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__, template_folder='templates')
app.config['JSON_AS_ASCII'] = False
CORS(app)

data = open("db.json")
db = json.load(data)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingresar')
def ingresar():
    return render_template('login.html')

@app.route('/api')
def api_docs():
    return render_template('api_docs.html')

@app.route('/directores')
def directores():
    return render_template('directores.html')

@app.route('/peliculas')
def api_peliculas():
    return render_template('peliculas.html')

@app.route('/agregar')
def api_agregar():
    return render_template('agregar.html')

@app.route('/typicons')
def typicons_demo():
    return render_template('typicons.html')
    

#
#        ***   USUARIOS   ***
#

@app.route("/usuarios", methods=['GET'])
def retornar_usuarios():
    return jsonify(db["usuarios"])


@app.route("/usuario/<id>", methods=['GET'])
def retornar_usuario(id):
    usuarios = db["usuarios"]
    usuario_id = int(id)
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return jsonify(usuario), HTTPStatus.OK
    return jsonify({}), HTTPStatus.BAD_REQUEST

#funcion interna, no flask

def existe_usuario(nombre):
    usuarios = db["usuarios"]
    for usuario in usuarios:
        if usuario["usuario"].lower() == nombre.lower():
            return True
    return False


@app.route("/usuario", methods=['POST'])
def alta_usuario():
    # recibir datos por parte del cliente
    data = request.get_json()
    if "nombre" in data:
        next_id = int(db["usuarios"][-1]["id"]) + 1
        nuevo_usuario = {
            "id": next_id,
            "nombre": data["nombre"],
            "password": data["password"],
        }
        db["usuarios"].append(nuevo_usuario)
        return jsonify(nuevo_usuario), HTTPStatus.OK
    else:
        return jsonify({}), HTTPStatus.BAD_REQUEST


@app.route("/usuario", methods=['PUT'])
def editar_usuario():
    data = request.get_json()
    if "id" in data:
        usuarios = db["usuarios"]
        for usuario in usuarios:
            if usuario["id"] == data["id"]:
                if "nombre" in data:
                    usuario["nombre"] = data["nombre"]
        # todo: devolver el usuario modificado
        return jsonify({}), HTTPStatus.OK
    else:
        return jsonify({}), HTTPStatus.BAD_REQUEST


#
#        ***   PELICULAS   ***
#


@app.route("/peliculas", methods=['GET'])
def retornar_peliculas():
    return jsonify(db["peliculas"])


@app.route("/peliculas/<titulo>", methods=['GET'])
def retornar_pelicula(titulo):
    peliculas = db["peliculas"]
    # pelicula_id = int(id)
    for pelicula in peliculas:
        if pelicula['titulo'].lower() == titulo.lower():
            return jsonify(pelicula), HTTPStatus.OK
    return jsonify({}), HTTPStatus.BAD_REQUEST

def existe_pelicula(titulo):
    peliculas = db["peliculas"]
    for pelicula in peliculas:
        if pelicula['titulo'].lower() == titulo.lower():
            return True
    return False


# revisar
@app.route("/peliculas", methods=['POST'])
def alta_pelicula():
    # recibir datos por parte del cliente
    data = request.get_json()
    # Validar data que viene del pedido
    # data.keys() >= {"usuario", "titulo"}  retorna true si hay coincidencia

    campos = {"usuario", "titulo", "genero", "director", "sinopsis", "imagen", "trailer", "promedio", "subidapor", "comentarios"}
    if data.keys() < campos:
        return jsonify("Falta usuario o titulo"), HTTPStatus.BAD_REQUEST

    if not existe_usuario(data["usuario"]):
        return jsonify("Quien te conoce papa."), HTTPStatus.BAD_REQUEST

    if existe_pelicula(data["titulo"]):
        return jsonify("La pelicula ya fue cargada por otro usuario."), HTTPStatus.BAD_REQUEST

    next_id = int(db["peliculas"][-1]["id"]) + 1
    pelicula_nueva = {
        "id": next_id,
        "titulo": data["titulo"],
        "anio": data["anio"],
        "genero": data["genero"],
        "genero_sub": data["genero_sub"],
        "director": data["director"],
        "sinopsis": data["sinopsis"],
        "imagen": data["imagen"],
        "trailer": data["trailer"],
        "promedio": data["promedio"],
        "subidapor": data["subidapor"],
        "comentarios": data["comentarios"]
    }
    db["peliculas"].append(pelicula_nueva)
    return jsonify(pelicula_nueva), HTTPStatus.OK


# revisar
@app.route("/pelicula", methods=['DELETE'])
def borrar_pelicula():
    # recibir datos por parte del cliente
    data = request.get_json()
    if "pelicula" in data and "comentarios" != [""]:
        db["peliculas"]["pelicula"].pop()
        return jsonify({}), HTTPStatus.OK
    else:
        return jsonify({}), HTTPStatus.BAD_REQUEST

@app.route("/directores", methods=['GET'])
def retornar_directores():
    return jsonify(db["directores"])

@app.route("/director/<id>", methods=['GET'])
def retornar_pelicula_director(id):
    id_director = int(id)
    peliculas_director = [pelicula["titulo"] for pelicula in db["peliculas"] if pelicula["id_director"] == id_director]
    return jsonify(peliculas_director), HTTPStatus.OK


@app.route("/api/login", methods=['POST'])
def validar_login():
    data = request.get_json() 
    for usuario in db["usuarios"]:
        if usuario["usuario"].lower() == data["usuario"].lower():
            if usuario["contrasenia"] == data["contrasenia"]:
                user = {key: val for key, val in usuario.items() if key not in ["contrasenia"]}
                return jsonify(user), HTTPStatus.OK
    return jsonify(False), HTTPStatus.OK


app.run(debug=True)
