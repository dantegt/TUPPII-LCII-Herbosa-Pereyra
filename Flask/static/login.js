let botonEnviar = document.getElementById('enviar');

botonEnviar.addEventListener('click' , evento =>{
    evento.preventDefault()
    let campoUsuario = document.getElementById('usuario').value;
    let campoPassword = document.getElementById('password').value;
    let campoError = document.getElementById('errorLogin');
    
    let data = {
        usuario: campoUsuario,
        contrasenia: campoPassword,
    }
    
    let requestOptions = {
        method: 'POST',
        mode: 'cors', 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    };

    fetch('http://127.0.0.1:5000/api/login', requestOptions)
        .then( resp => resp.json())
        .then( validado => {
            if (validado){
                console.log("usuario registrado");
                campoError.innerHTML = "";
                let expiracion = new Date();
                expiracion.setDate(expiracion.getDate() + 1);
                document.cookie =`usuario=${validado.usuario};expires=${expiracion}`
                document.cookie =`nombre=${validado.nombre};expires=${expiracion}`
                document.cookie =`id=${validado.id};expires=${expiracion}`
                document.cookie =`validado=true;expires=${expiracion}`
                window.location = "/"; // redirecciona a otra pag
            } else{
                console.log("error de login");
                campoError.innerHTML = "Error en el ingreso";
            }
        })
})