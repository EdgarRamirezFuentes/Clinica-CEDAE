/* ------------------ Campos paciente Externo ------------------ */

// Inputs del formulario para registrar paciente (Paciente externo)
let curpExterno = document.getElementById("curp");
let nombre = document.getElementById("nombrePaciente");
let aPaterno = document.getElementById("aPaternoPaciente");
let aMaterno = document.getElementById("aMaternoPaciente");
let nacimiento = document.getElementById("nacimiento");
let genero = document.getElementById("genero");
let telParticular = document.getElementById("telParticular");
let telCelular = document.getElementById("telCelular");
let paises = document.getElementById("paises");
let rfc = document.getElementById("rfc");
let correo = document.getElementById("correo");
let estados = document.getElementById("estados");
let alcaldia = document.getElementById("alcaldia");
let codigoPostal = document.getElementById("codigoPostal");
let colonia = document.getElementById("colonia");
let calle = document.getElementById("calle");
let numeroExterior = document.getElementById("numeroExterior");
let numeroInterno = document.getElementById("numeroInterior");
let estadoCivil = document.getElementById("estadoCivil");
let nombreEmergencia = document.getElementById("nombreEmergencia");
let aPaternoEmergencia = document.getElementById("aPaternoEmergencia");
let aMaternoEmergencia = document.getElementById("aMaternoEmergencia");
let telEmergencia = document.getElementById("telEmergencia");
let alergiasExterno = document.getElementById("alergias");
let antecedentePersonalExterno = document.getElementById("antecedentePersonal");
let antecedenteFamiliarExterno = document.getElementById("antecedenteFamiliar");
let padecimientoExterno = document.getElementById("padecimiento");
let temperaturaExterno = document.getElementById("temperatura");
let frecuenciaCardiacaExterno = document.getElementById("frecuenciaCardiaca");
let frecuenciaRepiratoriaExterno = document.getElementById("frecuenciaRespiratoria");
let presionArterialExterno = document.getElementById("presionArterial");
let oxigenacionExterno = document.getElementById("oxigenacion");
let alturaExterno = document.getElementById("altura");
let pesoExterno = document.getElementById("peso");
let examenFisicoExterno = document.getElementById("examenFisico");
let impresionDiagnosticaExterno = document.getElementById("impresionDiagnostica");
let estadosSelect = document.getElementById("estados");
let codigoPostalSelect = document.getElementById("codigoPostal");
let alcaldiaSelect = document.getElementById("alcaldia");
let coloniaSelect = document.getElementById("colonia");

// Labels de error de cada campo
let curpExternoError = document.getElementById("curpError");
let nombreError = document.getElementById("nombreError");
let aPaternoError = document.getElementById("aPaternoError");
let aMaternoError = document.getElementById("aMaternoError");
let nacimientoError = document.getElementById("nacimientoError");
let generoError = document.getElementById("generoError");
let telParticularError = document.getElementById("telParticularError");
let telCelularError = document.getElementById("telCelularError");
let paisesError = document.getElementById("paisNacimientoError");
let rfcError = document.getElementById("rfcError");
let correoError = document.getElementById("correoError");
let alcaldiaError = document.getElementById("alcaldiaError");
let codigoPostalError = document.getElementById("codigoPostalError");
let coloniaError = document.getElementById("coloniaError");
let calleError = document.getElementById("calleError");
let numeroExteriorError = document.getElementById("numeroExteriorError");
let numeroInternoError = document.getElementById("numeroInteriorError");
let estadoCivilError = document.getElementById("estadoCivilError");
let nombreEmergenciaError = document.getElementById("nombreEmergenciaError");
let aPaternoEmergenciaError = document.getElementById("aPaternoEmergenciaError");
let aMaternoEmergenciaError = document.getElementById("aMaternoEmergenciaError");
let telEmergenciaError = document.getElementById("telEmergenciaError");
let alergiasErrorExterno = document.getElementById("alergiasError");
let antecedentePersonalErrorExterno = document.getElementById("antecedentePersonalError");
let antecedenteFamiliarErrorExterno = document.getElementById("antecedenteFamiliarError");
let padecimientoErrorExterno = document.getElementById("padecimientoError");
let temperaturaErrorExterno = document.getElementById("temperaturaError");
let frecuenciaCardiacaErrorExterno = document.getElementById("frecuenciaCardiacaError");
let frecuenciaRepiratoriaErrorExterno = document.getElementById("frecuenciaRespiratoriaError");
let presionArterialErrorExterno = document.getElementById("presionArterialError");
let oxigenacionErrorExterno = document.getElementById("oxigenacionError");
let alturaErrorExterno = document.getElementById("alturaError");
let pesoErrorExterno = document.getElementById("pesoError");
let examenFisicoErrorExterno = document.getElementById("examenFisicoError");
let impresionDiagnosticaErrorExterno = document.getElementById("impresionDiagnosticaError");
let estadosSelectErrorExterno = document.getElementById("estadoError");
let codigoPostalSelectErrorExterno = document.getElementById("codigoPostalError");
let alcaldiaSelectErrorExterno = document.getElementById("alcaldiaError");
let coloniaSelectErrorExterno = document.getElementById("coloniaError");



/* ------------------ Campos paciente CEDAE ------------------ */

// Inputs del formulario para modificar expediente
let curp = document.getElementById("curpCEDAE");
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

/* ------------------ Event Listeners ------------------ */

function evenListener() {
    estadosSelect.addEventListener('change', function () {
        listarMunicipios(estadosSelect.value);
    });
    alcaldiaSelect.addEventListener('change', function () {
        listarCodigoPostal(alcaldiaSelect.value);
    });
    codigoPostalSelect.addEventListener('change', function() {
        listarColonias(codigoPostalSelect.value);
    });
}

/* ------------------ Llenado de opciones de formulario paciente externo ------------------ */

// Llenado de estados de México
function listarEstados() {
    let estadosMexicoURL = 'https://api-sepomex.hckdrk.mx/query/get_estados';
    fetch(estadosMexicoURL)
        .then(data => data.json())
        .then(data => {
            let estados = data.response.estado;
            estados = estados.sort();
            estados.forEach(estado => {
                let opcion = document.createElement("option");
                opcion.text = estado;
                estadosSelect.add(opcion)
            });
        });
}

// Llenado de select de paises en el formulario paciente externo
function listarPaises() {
    let paisesURL = 'https://restcountries.eu/rest/v2/all';
    fetch(paisesURL)
        .then(data => data.json())
        .then(data => {
            let paises = data;
            let paisesSelect = document.getElementById('paises');
            paises.forEach(pais => {
                let opcion = document.createElement("option");
                opcion.text = pais["name"];
                paisesSelect.add(opcion)
            });
        });
}

function listarCodigoPostal(municipio) {
    if (municipio != "default" && validarCampoLleno(municipio, codigoPostalError)) {
        limpiarSelect(codigoPostalSelect);
        let cpURL = 'https://api-sepomex.hckdrk.mx/query/get_cp_por_municipio/' + encodeURIComponent(municipio);
        fetch(cpURL)
            .then(data => data.json())
            .then(data => {
                let cp = data.response.cp;
                cp.forEach(codigoPostal => {
                    let opcion = document.createElement("option");
                    opcion.text = codigoPostal;
                    codigoPostalSelect.add(opcion)
                });
            });
    }
}

function listarColonias(codigoPostal) {
    if (codigoPostal != "default" && validarCampoLleno(codigoPostal, alcaldiaError)) {
        limpiarSelect(coloniaSelect);
        let coloniasURL = 'https://api-sepomex.hckdrk.mx/query/get_colonia_por_cp/' + encodeURIComponent(codigoPostal);
        fetch(coloniasURL)
            .then(data => data.json())
            .then(data => {
                let cp = data.response.colonia;
                cp.forEach(colonia => {
                    let opcion = document.createElement("option");
                    opcion.text = colonia;
                    coloniaSelect.add(opcion)
                });
            });
    }
}

function listarMunicipios(estado) {
    if (estado != "default" && validarCampoLleno(estado, alcaldiaError)) {
        limpiarSelect(alcaldiaSelect);
        let municipiosURL = 'https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/' + encodeURIComponent(estado);
        fetch(municipiosURL)
            .then(data => data.json())
            .then(data => {
                let cp = data.response.municipios;
                cp.forEach(municipio => {
                    let opcion = document.createElement("option");
                    opcion.text = municipio;
                    alcaldiaSelect.add(opcion)
                });
            });
    }
}

/* ------------------ Validaciones ------------------ */

function validarCampoLleno(valorInput, label) {
    if (valorInput.length == 0) {
        label.innerHTML = "Campo requerido";
        return 0;
    }
    label.innerHTML = "";
    return 1;
}

function validarCURP(curp, label) {
    let curpRegex = new RegExp("^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$");
    if (!curpRegex.test(curp) && validarCampoLleno(curp, label)) {
        label.innerHTML = "Ingresa un CURP válido";
        return 0;
    }
    return 1;
}

function validarLetra(valorInput, label) {
    let alfaRegex = /^[a-zäÄëËïÏöÖüÜáéíóúáéíóúÁÉÍÓÚÂÊÎÔÛâêîôûàèìòùÀÈÌÒÙñÑ\s]+$/gi;
    if (!alfaRegex.test(valorInput) && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Este campo solo acepta letras";
        return 0;
    }
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

function validarSelect(opcion, label) {
    if (opcion == "default") {
        label.innerHTML = "Selecciona una opcion";
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

function validarTelefono(telefono, label) {
    let telefonoRegex = new RegExp("^([+][1-9]{2})?[0-9]{8,14}$");
    if (!telefonoRegex.test(telefono) && validarCampoLleno(telefono, label)) {
        label.innerHTML = "Ingresa un teléfono válido";
        return 0;
    }
    return 1;
}

function validarFecha(date, label) {
    let x = new Date();
    let fecha = date.split("-");
    let mes = fecha[1];
    let anio = fecha[0];
    if (mes == undefined || anio ==undefined) {
        label.innerHTML = "Ingresa una fecha de nacimiento";
        return 0;
    }
    x.setFullYear(fecha[0], fecha[1] - 1, fecha[2]);
    let hoy = new Date();
    if((hoy.getFullYear() - anio) >= 125) {
        console.log(hoy.getFullYear() + " " + anio + " " + (hoy.getFullYear() - anio));
        label.innerHTML = "Ingresa una año de nacimiento válido";
        return 0;
    } else if (x >= hoy) {
        label.innerHTML = "Ingresa una fecha de nacimiento válida";
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

function validarRFC(rfc, label) {
    let rfcRegex = new RegExp("^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])([A-Z]|[0-9]){2}([A]|[0-9]){1})?$");
    if (!rfcRegex.test(rfc) && validarCampoLleno(rfc, label)) {
        label.innerHTML = "Ingrese un válido RFC ";
        return 0;
    }
    return 1;
}

function validarPresionArterial(presion, label) {
    let presionRegex = new RegExp("^[0-9]+\/[0-9]+$");
    if (!presionRegex.test(presion) && validarCampoLleno(presion, label)) {
        label.innerHTML = "Ingrese una presión arterial válida";
        return 0;
    }
    return 1;
}

function validarDatosPacienteCEDAE() {
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
    valido *= validarCampoLleno(curp.value.trim(), curpError);
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

    /* Validación de CURP válido
        1 -> CURP válido
        0 -> CURP no válido
    */
    valido *= validarCURP(curp.value.trim(), curpError);

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


function validarDatosPacienteExterno() {
    let valido = 1; // Determina si todos los campos ingresados son válidos
    let labelsError = document.getElementsByClassName("externoLabel"); // Almacena los labels de error

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
    valido *= validarCampoLleno(curpExterno.value.trim(), curpExternoError);
    valido *= validarCampoLleno(nombre.value.trim(), nombreError);
    valido *= validarCampoLleno(aPaterno.value.trim(), aPaternoError);
    valido *= validarCampoLleno(aMaterno.value.trim(), aMaternoError);
    valido *= validarCampoLleno(nacimiento.value.trim(), nacimientoError);
    valido *= validarCampoLleno(genero.value.trim(), generoError);
    valido *= validarCampoLleno(correo.value.trim(), correoError);
    valido *= validarCampoLleno(calle.value.trim(), calleError);
    valido *= validarCampoLleno(numeroExterior.value.trim(), numeroExteriorError);
    // valido *= validarCampoLleno(numeroInterno.value.trim(), numeroInternoError);
    valido *= validarCampoLleno(nombreEmergencia.value.trim(), nombreEmergenciaError);
    valido *= validarCampoLleno(aPaternoEmergencia.value.trim(), aPaternoEmergenciaError);
    valido *= validarCampoLleno(aMaternoEmergencia.value.trim(), aMaternoEmergenciaError);
    valido *= validarCampoLleno(alergiasExterno.value.trim(), alergiasErrorExterno);
    valido *= validarCampoLleno(antecedentePersonalExterno.value.trim(), antecedentePersonalErrorExterno);
    valido *= validarCampoLleno(antecedenteFamiliarExterno.value.trim(), antecedenteFamiliarErrorExterno);
    valido *= validarCampoLleno(padecimientoExterno.value.trim(), padecimientoErrorExterno);
    valido *= validarCampoLleno(temperaturaExterno.value.trim(), temperaturaErrorExterno);
    valido *= validarCampoLleno(frecuenciaCardiacaExterno.value.trim(), frecuenciaCardiacaErrorExterno);
    valido *= validarCampoLleno(frecuenciaRepiratoriaExterno.value.trim(), frecuenciaRepiratoriaErrorExterno);
    valido *= validarCampoLleno(presionArterialExterno.value.trim(), presionArterialErrorExterno);
    valido *= validarCampoLleno(oxigenacionExterno.value.trim(), oxigenacionErrorExterno);
    valido *= validarCampoLleno(alturaExterno.value.trim(), alturaErrorExterno);
    valido *= validarCampoLleno(pesoExterno.value.trim(), pesoErrorExterno);
    valido *= validarCampoLleno(examenFisicoExterno.value.trim(), impresionDiagnosticaErrorExterno);
    valido *= validarCampoLleno(nacimiento.value.trim(), nacimientoError);

    /* Validación de RFC
        1 -> RFC válido
        0 -> RFC no válido
    */
    if (rfc.value.trim())
        valido *= validarRFC(rfc.value.trim(), rfcError);

    /* Validación de fecha 
        1 -> Fecha válida
        0 -> Fecha no válida
        Se considera una fecha válida a aquella que se encuentre previo al día actual
    */
    valido *= validarFecha(nacimiento.value.trim(), nacimientoError);

    /* Validación de CURP válido
        1 -> CURP válido
        0 -> CURP no válido
    */
    valido *= validarCURP(curpExterno.value.trim(), curpExternoError);

    /* Validación de valores alfabéticos 
        1 -> Valor alfabético válido
        0 -> Valor alfabético no válido
    */
    valido *= validarLetra(nombre.value.trim(), nombreError);
    valido *= validarLetra(aPaterno.value.trim(), aPaternoError);
    valido *= validarLetra(aMaterno.value.trim(), aMaternoError);
    valido *= validarLetra(nombreEmergencia.value.trim(), nombreEmergenciaError);
    valido *= validarLetra(aPaternoEmergencia.value.trim(), aPaternoEmergenciaError);
    valido *= validarLetra(aMaternoEmergencia.value.trim(), aMaternoEmergenciaError);

    /* Validación de teléfonos
        1 -> Valor telefónico válido
        0 -> Valor telefónico no válido
    */
    valido *= validarTelefono(telParticular.value.trim(), telParticularError);
    valido *= validarTelefono(telCelular.value.trim(), telCelularError);
    valido *= validarTelefono(telEmergencia.value.trim(), telEmergenciaError);

    /* Validación de campos select
         1 -> Opción seleccionada
         0 -> Opción no seleccionada
    */
    valido *= validarSelect(genero.value.trim(), generoError);
    valido *= validarSelect(paises.value.trim(), paisesError);
    valido *= validarSelect(estadosSelect.value.trim(), estadosSelectErrorExterno);
    valido *= validarSelect(codigoPostalSelect.value.trim(), codigoPostalSelectErrorExterno);
    valido *= validarSelect(alcaldiaSelect.value.trim(), alcaldiaSelectErrorExterno);
    valido *= validarSelect(coloniaSelect.value.trim(), coloniaSelectErrorExterno);

    /* Validación de valores numéricos 
        1 -> Valor numérico válido
        0 -> Valor numérico no válido
    */
    valido *= validarNumero(temperaturaExterno.value.trim(), temperaturaErrorExterno);
    valido *= validarNumero(frecuenciaCardiacaExterno.value.trim(), frecuenciaCardiacaErrorExterno);
    valido *= validarNumero(frecuenciaRepiratoriaExterno.value.trim(), frecuenciaRepiratoriaErrorExterno);
    //valido *= validarNumero(presionArterialExterno.value.trim(), presionArterialErrorExterno);
    valido *= validarNumero(oxigenacionExterno.value.trim(), oxigenacionErrorExterno);
    valido *= validarNumero(alturaExterno.value.trim(), alturaErrorExterno);
    valido *= validarNumero(pesoExterno.value.trim(), pesoErrorExterno);

    /* Validación de presión arterial
        1 -> Tiene presión arterial correcta
        0 -> No tiene presión arterial correcta
    */
   validarPresionArterial(presionArterial.value.trim(), presionArterialError);
   
    /* Validación de longitud de cadena 
        1 -> Tiene longitud correcta
        0 -> No tiene longitud correcta
    */
    valido *= validarLetra(nombre.value.trim(), temperaturaErrorExterno, 100);
    valido *= validarLetra(aPaterno.value.trim(), aPaternoError, 100);
    valido *= validarLetra(aMaterno.value.trim(), aMaternoError, 100);
    valido *= validarCampoLleno(nombreEmergencia.value.trim(), nombreEmergenciaError, 100);
    valido *= validarCampoLleno(aPaternoEmergencia.value.trim(), aPaternoEmergenciaError, 100);
    valido *= validarCampoLleno(aMaternoEmergencia.value.trim(), aMaternoEmergenciaError, 100);
    valido *= validarLongitud(alergiasExterno.value.trim(), alergiasErrorExterno, 100);
    valido *= validarLongitud(antecedentePersonalExterno.value.trim(), antecedentePersonalErrorExterno, 100);
    valido *= validarLongitud(antecedenteFamiliarExterno.value.trim(), antecedenteFamiliarErrorExterno, 100);
    valido *= validarLongitud(padecimientoExterno.value.trim(), padecimientoErrorExterno, 100);
    valido *= validarLongitud(examenFisicoExterno.value.trim(), examenFisicoErrorExterno, 100);
    valido *= validarLongitud(impresionDiagnosticaExterno.value.trim(), impresionDiagnosticaErrorExterno, 100);

    return valido;
}


/* ------------------ Limpieza de campos ------------------ */

function limpiarLabels(labels) {
    for (let i = 0; i < labels.length; i++) {
        labels[i].innerHTML = "";
    }
}

function limpiarSelect(select) {
    for (let i = select.options.length; i > 0; i--) {
        select.remove(i);
    }
}

/* ------------------ Acciones de la interfaz ------------------ */

function registrarPaciente(tipoPaciente) {
    Swal.fire({
        title: '¿Los datos ingresados son correctos?',
        icon: 'question',
        showCancelButton: 1,
        confirmButtonText: `Sí, registrar paciente`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }).then((result) => {
        if (result.isConfirmed) {
            /*
                Tipo de paciente:
                1 -> CEDAE
                2 -> Externo 
            */
            if (tipoPaciente == 1) {
                if (validarDatosPacienteCEDAE()) {
                    document.CEDAEForm.submit();
                } else {
                    Swal.fire('Los datos ingresados no son válidos', '', 'error')
                }
            } else {
                if (validarDatosPacienteExterno()) {
                    document.externoForm.submit();
                } else {
                    Swal.fire('Los datos ingresados no son válidos', '', 'error')
                }
            }
        }
    });
}

/* ------------------ Llamada de funciones ------------------ */

listarPaises();
listarEstados();
evenListener();