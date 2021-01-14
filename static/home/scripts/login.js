let correo = document.getElementById("correo");
let password = document.getElementById("contrasenia");

let correoLabel = document.getElementById("correoError");
let passwordLabel = document.getElementById("passError");

function validarCampoLleno(valorInput, label) {
  if (valorInput.length == 0) {
      label.innerHTML = "Campo requerido";
      return 0;
  }
  label.innerHTML = "";
  return 1;
}

function validarCorreo(correo, label) {
  let mailRegex = new RegExp("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$");
  if (!mailRegex.test(correo) && validarCampoLleno(correo, label)) {
      label.innerHTML = "Ingrese un correo electrónico válido";
      return 0;
  }
  return 1;
}

function validarLongitud(valorInput, label, longitud) {
  if (valorInput.length > longitud && validarCampoLleno(valorInput, label)) {
      label.innerHTML = "Solo se admiten " + longitud + " caracteres en este campo";
      return 0;
  }
  return 1;
}

function validarCredenciales() {
  let valido = 1;
  valido *= validarCampoLleno(correo.value.trim(), correoLabel);
  valido *= validarCampoLleno(password.value.trim(), passwordLabel, 25);
  valido *= validarCorreo(correo.value.trim(), correoLabel);
  valido *= validarLongitud(password.value.trim(), passwordLabel, 25);
  if (valido) {
    document.iniciarSesionForm.submit();
} else {
    Swal.fire('Los datos ingresados no son válidos', '', 'error')
}
}
