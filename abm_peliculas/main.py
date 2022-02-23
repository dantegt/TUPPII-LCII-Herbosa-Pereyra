from http import HTTPStatus
from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__, template_folder='templates')
app.config['JSON_AS_ASCII'] = False

data = open("db.json")
db = json.load(data)


@app.route('/')
def index():
    return render_template('hello.html')

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


@app.route("/usuario", methods=['DELETE'])          #No hace falta baja de usuario
def borrar_usuario():
    # recibir datos por parte del cliente
    data = request.get_json()
    # if "nombre" in data:
    #     next_id = int(db["usuarios"][-1]["id"]) + 1
    #     db["usuarios"].append({
    #         "id": next_id,
    #         "nombre": data["nombre"]
    #     })
    #     return jsonify({}), HTTPStatus.OK
    # else:
    #     return jsonify({}), HTTPStatus.BAD_REQUEST

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


# revisar
@app.route("/peliculas", methods=['POST'])
def alta_pelicula():
    # recibir datos por parte del cliente
    data = request.get_json()
    # Validar data que viene del pedido
    if "usuario" in data and "titulo" in data:
        usuarios = db["usuarios"]
        for usuario in usuarios:
            # Existe usuario en la db
            if usuario["usuario"].lower() == data["usuario"].lower():
                peliculas = db["peliculas"]
                for pelicula in peliculas:
                    # Pelicula ya existe en la db?
                    if pelicula["titulo"] == data["titulo"]:
                        mensaje = f"La pelicula ya existe en la base de datos, {data['usuario']}"
                        return jsonify(mensaje), HTTPStatus.BAD_REQUEST
                    else:
                        next_id = int(db["peliculas"][-1]["id"]) + 1
                        pelicula_nueva = {
                            "id": next_id,
                            "titulo": data["titulo"],
                            # "anio": data["anio"],
                            # "genero": data["genero"],
                            # "director": data["director"],
                            # "sinopsis": data["sinopsis"],
                            # "imagen": data["imagen"],
                            # "trailer": data["trailer"],
                            # "promedio": data["promedio"],
                            # "subidapor": data["subidapor"],
                            # "comentarios": data[""],
                        }
                        db["peliculas"].append(pelicula_nueva)
                        return jsonify(pelicula_nueva), HTTPStatus.OK
    else:
        return jsonify("Falta usuario o titulo"), HTTPStatus.BAD_REQUEST


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


'''
@app.route("/usuario/<id>/compartidas", methods=['GET'])
def retornar_usuario_compartidas(id):
    usuario_id = int(id)
    compartidas = db["compartidas"]
    comp_user = [c for c in compartidas if c["user"] == usuario_id]
    return jsonify(comp_user), HTTPStatus.OK


@app.route("/compartir", methods=['POST'])
def usuario_comparte_receta():
    # recibir datos por parte del cliente
    data = request.get_json()
    if "usuario_id" in data and "receta_id" in data:
        usuario_id = int(data["usuario_id"])
        receta_id = int(data["receta_id"])
        compartidas = db["compartidas"]
        existe = [c
                  for c in compartidas
                  if c["user"] == usuario_id and c["receta"] == receta_id]
        if not existe:
            db["compartidas"].append({
                "user": usuario_id,
                "receta": receta_id
            })
        else:
            return jsonify({}), HTTPStatus.BAD_REQUEST
        return jsonify({}), HTTPStatus.OK
    else:
        return jsonify({}), HTTPStatus.BAD_REQUEST


@app.route("/descompartir", methods=['DELETE'])
def usuario_descomparte_receta():
    # recibir datos por parte del cliente
    data = request.get_json()
    if "usuario_id" in data and "pelicula_id" in data:
        usuario_id = int(data["usuario_id"])
        pelicula_id = int(data["pelicula_id"])
        compartidas = db["compartidas"]
        db["compartidas"] = [c
                             for c in compartidas
                             if not (c["user"] == usuario_id and c["pelicula"] == pelicula_id)]

        return jsonify({}), HTTPStatus.OK
    else:
        return jsonify({}), HTTPStatus.BAD_REQUEST
'''

app.run()
