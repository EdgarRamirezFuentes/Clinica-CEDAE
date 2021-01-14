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
            Swal.fire("Paciente registrado con éxito", '', 'success');
        }
    });
}

function medicamentoRegistrado() {
    Swal.fire("El medicamento que intenta registrar ya existe", '', 'error')
}

function camposIncompletos() {
    Swal.fire("Todos los campos obligatorios deben ser llenados", '', 'warning')
}