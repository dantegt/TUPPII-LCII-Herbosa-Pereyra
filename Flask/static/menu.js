
let cookies = document.cookie
let logueado = cookies.includes("usuario") && cookies.includes("validado=true")
const nav = document.getElementById("navigation")

if (logueado) {
    nav.innerHTML += '<a href="/agregar" class="link" id="agregar">+ Agregar</a><a href="/perfil" class="link" id="perfil">Perfil</a>'
} else {
    nav.innerHTML += '<a href="/ingresar" class="link login">Ingresar</a>'
}

// Navegacion Mobile
document.getElementById("mobile-hamburger").addEventListener("click", () => nav.classList.add("mobile-active"));
document.getElementById("mobile-cerrar").addEventListener("click", () => nav.classList.remove("mobile-active"));

let obtenerCookie = (nombre) => {
    let array = document.cookie.split(";")
    c = array.filter(c => c.includes(nombre+"="))[0]
    let i = c.indexOf(nombre+"=")
    return c.substring(i+nombre.length+1)
}

// Usuario actualmente logueado
let user_logueado = obtenerCookie("id")
