let sku = document.getElementById("sku");
let nombre = document.getElementById("nombre");
let sustancia_activa = document.getElementById("sustancia_activa");
let presentacion = document.getElementById("presentacion");
let precio = document.getElementById("precio");
let fecha_caducidad = document.getElementById("fecha_caducidad");
let cantidad = document.getElementById("cantidad");

let skuError = document.getElementById("skuError");
let nombreError = document.getElementById("nombreError");
let sustanciaError = document.getElementById("sustanciaError");
let presentacionError = document.getElementById("presentacionError");
let precioError = document.getElementById("precioError");
let fecha_caducidadError = document.getElementById("fechaError");
let cantidadError = document.getElementById("cantidadError");

function validarCampoLleno(valorInput, label) {
    if (valorInput.length == 0) {
        label.innerHTML = "Campo requerido";
        return 0;
    }
    label.innerHTML = "";
    return 1;
}

function validarLongitud(valorInput, label, longitud) {
    if (valorInput.length > longitud && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Solo se admiten " + longitud + " caracteres en este campo";
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

function validarNumero(valorInput, label) {
    let decimalRegex = new RegExp("^[0-9]+([.][0-9]+)?$");
    if (!decimalRegex.test(valorInput) && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Ingresa un valor numérico válido";
        return 0;
    }
    return 1;
}

function validarCantidad(valorInput, label) {
    let decimalRegex = new RegExp("^[0-9]+$");
    if (!decimalRegex.test(valorInput) && validarCampoLleno(valorInput, label)) {
        label.innerHTML = "Ingresa una cantidad válida";
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
    if (x < hoy) {
        label.innerHTML = "Esta fecha de caducidad no es válida (Medicamento caducado)";
        return 0;
    }
    return 1;
}

function limpiarLabels(labels) {
    for (let i = 0; i < labels.length; i++) {
        labels[i].innerHTML = "";
    }
}

function validarDatos() {
    valido = 1;
    let labelsError = document.getElementsByClassName("labelError"); // Almacena los labels de error
    limpiarLabels(labelsError);
    valido *= validarCampoLleno(sku.value, skuError);
    valido *= validarCampoLleno(nombre.value, nombreError);
    valido *= validarCampoLleno(sustancia_activa.value, sustanciaError);
    valido *= validarCampoLleno(presentacion.value, presentacionError);
    valido *= validarCampoLleno(cantidad.value, cantidadError);
    valido *= validarCampoLleno(precio.value, precioError);
    
    valido *= validarNumero(precio.value, precioError);

    valido *= validarFecha(fecha_caducidad.value, fecha_caducidadError);

    valido *= validarCantidad(cantidad.value, cantidadError);
    return valido;
}

function registrarmedicamento() {
    Swal.fire({
        title: '¿Los datos ingresados son correctos?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: `Sí, agregar medicamento`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }) .then((result) => {
        if (result.isConfirmed) {
            if (validarDatos()) {
                document.addDrugForm.submit();
            } else {
                Swal.fire('Los datos ingresados no son válidos', '', 'error')
            }
        }
    });
}
