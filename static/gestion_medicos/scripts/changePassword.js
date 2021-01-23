let contraseniaActual = document.getElementById("passActual");
let contraseniaNueva = document.getElementById("passNueva");
let contraseniaNuevaConfirmacion = document.getElementById("passNuevaConfirmacion");

let contraseniaActualError = document.getElementById("passActualError");
let contraseniaNuevaError = document.getElementById("passNuevaError");
let contraseniaNuevaConfirmacionError = document.getElementById("passNuevaConfirmacionError");

function limpiarLabels(labels) {
    for (let i = 0; i < labels.length; i++) {
        labels[i].innerHTML = "";
    }
}

function validarLongitud(valorInput, label) {
    if (valorInput.length > 20 && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Solo se admiten " + 20 + " caracteres como máximo en este campo";
        return 0;
    }

    if (valorInput.length < 8 && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Solo se admiten " + 8 + " caracteres como mínimo en este campo";
        return 0;
    }
    return 1;
}

function validarContrasenia(valorInput, label) {
    let alfaRegex = new RegExp(/^[A-Za-z0-9]+$/g);
    if (!alfaRegex.test(valorInput) && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Este campo solo acepta letras sin acentos y números";
        console.log(alfaRegex.test(valorInput));
        return 0;
    }
    return 1;
}

function validarConfirmacion(valorInput, valorInput2, label, label2) {
    if ((validarCampoLleno(valorInput, label) && validarCampoLleno(valorInput, label2) && valorInput != valorInput2)) {
        label2.innerHTML = "Esta contraseña no coincide con la primera ingresada";
        return 0;
    }
    return 1;
}

function validarCampoLleno(valorInput, label) {
    if (valorInput.length == 0) {
        label.innerHTML = "Campo requerido";
        return 0;
    }
    label.innerHTML = "";
    return 1;
}

function validarDatosContrasenia() {
    let valido = 1;
    let labels = document.getElementsByClassName("labelError");
    limpiarLabels(labels);
    valido *= validarCampoLleno(contraseniaActual.value, contraseniaActualError);
    valido *= validarCampoLleno(contraseniaNueva.value, contraseniaNuevaError);
    valido *= validarCampoLleno(contraseniaNuevaConfirmacion.value, contraseniaNuevaConfirmacionError);

    valido *= validarContrasenia(contraseniaNueva.value, contraseniaNuevaError);
    valido *= validarConfirmacion(contraseniaNueva.value, contraseniaNuevaConfirmacion.value, contraseniaNuevaError, contraseniaNuevaConfirmacionError);

    valido *= validarLongitud(contraseniaNueva.value, contraseniaNuevaError);
    valido *= validarLongitud(contraseniaNuevaConfirmacion.value, contraseniaNuevaConfirmacionError);
    return valido;
}

function modificarContrasenia() {
    Swal.fire({
        title: '¿Estás seguro de cambiar tu contraseña?',
        icon: 'question',
        showCancelButton: 1,
        confirmButtonText: `Sí, cambiar contraseña`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }).then((result) => {
        if (result.isConfirmed) {
            if (validarDatosContrasenia()) {
                document.cambiarPassForm.submit();
            } else {
                Swal.fire('Los datos ingresados no son válidos', '', 'error')
            }
        }
    });
}