/* ------------------ Campos expediente ------------------ */

// Inputs del formulario para registrar paciente (Trabajador CEDAE)
let alergias = document.getElementById("alergiasCEDAE");
let antecedentePersonal = document.getElementById("antecedentePersonalCEDAE");
let antecedenteFamiliar = document.getElementById("antecedenteFamiliarCEDAE");
let padecimiento = document.getElementById("padecimientoCEDAE");
let temperatura = document.getElementById("temperaturaCEDAE");
let frecuenciaCardiaca = document.getElementById("frecuenciaCardiacaCEDAE");
let frecuenciaRepiratoria = document.getElementById("frecuenciaRespiratoriaCEDAE");
let presionArterial = document.getElementById("presionArterialCEDAE");
let oxigenacion = document.getElementById("oxigenacionCEDAE");
let altura = document.getElementById("alturaCEDAE");
let peso = document.getElementById("pesoCEDAE");
let examenFisico = document.getElementById("examenFisicoCEDAE");
let impresionDiagnostica = document.getElementById("impresionDiagnosticaCEDAE");

// Labels de error de cada campo
let curpError = document.getElementById("curpCEDAEError");
let alergiasError = document.getElementById("alergiasCEDAEError");
let antecedentePersonalError = document.getElementById("antecedentePersonalCEDAEError");
let antecedenteFamiliarError = document.getElementById("antedecenteFamiliarCEDAEError");
let padecimientoError = document.getElementById("padecimientoCEDAEError");
let temperaturaError = document.getElementById("temperaturaCEDAEError");
let frecuenciaCardiacaError = document.getElementById("frecuenciaCardiacaCEDAEError");
let frecuenciaRepiratoriaError = document.getElementById("frecuenciaRespiratoriaCEDAEError");
let presionArterialError = document.getElementById("presionArterialCEDAEError");
let oxigenacionError = document.getElementById("oxigenacionCEDAEError");
let alturaError = document.getElementById("alturaCEDAEError");
let pesoError = document.getElementById("pesoCEDAEError");
let examenFisicoError = document.getElementById("examenFisicoCEDAEError");
let impresionDiagnosticaError = document.getElementById("impresionDiagnosticaCEDAEError");

/* ------------------ Validaciones ------------------ */

function validarPresionArterial(presion, label) {
    let presionRegex = new RegExp("^[0-9]+/[0-9]+$");
    if (!presionRegex.test(presion) && validarCampoLleno(presion, label)) {
        label.innerHTML = "Ingrese una presión arterial válida";
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

function validarNumero(valorInput, label) {
    let decimalRegex = new RegExp("^[0-9]+([.][0-9]+)?$");
    if (!decimalRegex.test(valorInput) && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Ingresa un valor numérico válido";
        return 0;
    }
    return 1;
}

function validarLetra(valorInput, label) {
    let alfaRegex = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/g;
    if (!alfaRegex.test(valorInput) && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Este campo solo acepta letras";
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

function validarDatosExpediente() {
    let valido = 1; // Determina si todos los campos ingresados son válidos
    let labelsError = document.getElementsByClassName("cedaeLabel"); // Almacena los labels de error

    // Limpiamos labels para obtener los errores actuales
    limpiarLabels(labelsError);

    /*
        Validaciones
        Mediante operaciones matemáticas se va a determinar si todos los campos
        ingresados son válidos. 
        Con una solo campo que no sea válido, se retornará 0 indicando que 
        los datos no son válidos.
        Operación multiplicación:
        x * 0 -> 0
    */

    /* Validaciones de campo vacio
        1 -> Campo no vacío
        0 -> Campo vacío
    */
    valido *= validarCampoLleno(alergias.value.trim(), alergiasError);
    valido *= validarCampoLleno(antecedentePersonal.value.trim(), antecedentePersonalError);
    valido *= validarCampoLleno(antecedenteFamiliar.value.trim(), antecedenteFamiliarError);
    valido *= validarCampoLleno(padecimiento.value.trim(), padecimientoError);
    valido *= validarCampoLleno(temperatura.value.trim(), temperaturaError);
    valido *= validarCampoLleno(frecuenciaCardiaca.value.trim(), frecuenciaCardiacaError);
    valido *= validarCampoLleno(frecuenciaRepiratoria.value.trim(), frecuenciaRepiratoriaError);
    valido *= validarCampoLleno(presionArterial.value.trim(), presionArterialError);
    valido *= validarCampoLleno(oxigenacion.value.trim(), oxigenacionError);
    valido *= validarCampoLleno(altura.value.trim(), alturaError);
    valido *= validarCampoLleno(peso.value.trim(), pesoError);
    valido *= validarCampoLleno(examenFisico.value.trim(), examenFisicoError);
    valido *= validarCampoLleno(impresionDiagnostica.value.trim(), impresionDiagnosticaError);


    /* Validación de valores numéricos 
        1 -> Valor numérico válido
        0 -> Valor numérico no válido
    */
    valido *= validarNumero(temperatura.value.trim(), temperaturaError);
    valido *= validarNumero(frecuenciaCardiaca.value.trim(), frecuenciaCardiacaError);
    valido *= validarNumero(frecuenciaRepiratoria.value.trim(), frecuenciaRepiratoriaError);
    //valido *= validarNumero(presionArterial.value.trim(), presionArterialError);
    valido *= validarNumero(oxigenacion.value.trim(), oxigenacionError);
    valido *= validarNumero(altura.value.trim(), alturaError);
    valido *= validarNumero(peso.value.trim(), pesoError);

    /* Validación de presión arterial
        1 -> Tiene presión arterial correcta
        0 -> No tiene presión arterial correcta
    */
    validarPresionArterial(presionArterial.value.trim(), presionArterialError);

    /* Validación de longitud de cadena 
        1 -> Tiene longitud correcta
        0 -> No tiene longitud correcta
    */
    valido *= validarLongitud(alergias.value.trim(), alergiasError, 100);
    valido *= validarLongitud(antecedentePersonal.value.trim(), antecedentePersonalError, 100);
    valido *= validarLongitud(antecedenteFamiliar.value.trim(), antecedenteFamiliarError, 100);
    valido *= validarLongitud(padecimiento.value.trim(), padecimientoError, 100);
    valido *= validarLongitud(examenFisico.value.trim(), examenFisicoError, 100);
    valido *= validarLongitud(impresionDiagnostica.value.trim(), impresionDiagnosticaError, 100);

    return valido;
}

/* ------------------ Limpieza de campos ------------------ */

function limpiarLabels(labels) {
    for (let i = 0; i < labels.length; i++) {
        labels[i].innerHTML = "";
    }
}

/* ------------------ Acciones de la interfaz ------------------ */

function modificar() {
    Swal.fire({
        title: '¿Los datos ingresados son correctos?',
        icon: 'question',
        showCancelButton: 1,
        confirmButtonText: `Sí, modificar expediente`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }).then((result) => {
        if (result.isConfirmed) {
            if(validarDatosExpediente()) {
                document.modificarExpedienteForm.submit();
            }
        }
    });
}