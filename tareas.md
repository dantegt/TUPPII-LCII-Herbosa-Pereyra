# Proyecto Final TUP PII LPII
__Objetivo:__ Plataforma web para mantener una lista de películas recomendadas por parte de los usuarios.

### Objetos
    - Usuario
    - Pelicula
    - Review

### Acciones
    - Login de usuario
    - ABM Pelicula
    - ABM Review
    - Lista de Directores       /directores  /api/directores
    - Lista de Géneros          /api/generos
    - Lista de Peliculas por director
    - Lista de peliculas con Portada
    - PLUS: Link a trailer de la pelicula, Puntuación promediada

### Funcionalidades:
    - Listar ultimas 10 peliculas (Modo público)
    - Publicar o administrar un review
    - EXTRA: Paginado
    - EXTRA: Buscador de peliculas

### Tareas pendientes

    - API (Flask, CRUD, JSON "DB")
        - [80%] DB
        - Flask
        - CRUD Pelicula + Reseña
        - Editar Película
                se puede editar datos de peliculas, no comentarios de otros usuarios
                usuario puede eliminar pelicula si no tiene comentarios
                invitado no puede editar/eliminar nada.                

        - Listado de directores
        - Listado de generos (en la carga los generos se deben seleccionar de una lista pre armada por lo uqe entiendo)
        - Listado de peliculas por director
        
    - FrontEnd (HTML, CSS, Responsive)
        - [100%] Inicio
        - Login
        - Carga / Edicion de Peliculas
        - Lista de Peliculas por Director
        - Modo publico: muestra ultimas 10 peliculas listadas
