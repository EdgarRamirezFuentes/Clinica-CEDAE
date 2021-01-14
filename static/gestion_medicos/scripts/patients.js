var formulario = document.getElementById("buscarPaciente");
var buscador = document.getElementById("curp");

function errorMessage(message) {
    Swal.fire(message, '', 'error')
}

function validar(){
    if(buscador.value.length != 18){
        errorMessage("El campo de busqueda requiere un curp de 18 caracteres");
        console.log(buscador);
    }else{
        document.buscarPaciente.submit();
    }
}

