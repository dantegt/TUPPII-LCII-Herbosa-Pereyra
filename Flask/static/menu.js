
let cookies = document.cookie
let logueado = cookies.includes("usuario") && cookies.includes("validado=true")
const nav = document.getElementById("navigation")
let user_logueado = ""

let obtenerCookie = (nombre) => {
    let array = document.cookie.split(";")
    c = array.filter(c => c.includes(nombre+"="))[0]
    let i = c.indexOf(nombre+"=")
    return c.substring(i+nombre.length+1)
}

if (logueado) {
    nav.innerHTML += '<a href="/agregar" class="link" id="agregar">+ Agregar</a><a href="javascript:void(0)" class="link" id="salir">Salir</a>'
    // Usuario actualmente logueado
    user_logueado = obtenerCookie("id")
} else {
    nav.innerHTML += '<a href="/ingresar" class="link login">Ingresar</a>'
}

// Navegacion Mobile
document.getElementById("mobile-hamburger").addEventListener("click", () => nav.classList.add("mobile-active"));
document.getElementById("mobile-cerrar").addEventListener("click", () => nav.classList.remove("mobile-active"));
document.getElementById("salir").addEventListener("click", () => document.cookie.split(';').forEach(c => {
    document.cookie = c.trim().split('=')[0] + '=;' + 'expires=Thu, 01 Jan 1970 00:00:00 UTC;';
}))
