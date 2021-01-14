function primera() {
    Swal.fire({
        title: '¿Los datos ingresados son correctos?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: `Sí, agendar cita`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }) .then((result) => {
        if (result.isConfirmed) {
            Swal.fire("Cita registrada con éxito", '', 'success');
        }
    });
}

function segunda() {
    Swal.fire("La cita que intenta registrar ya existe", '', 'error')
}

function camposIncompletos() {
    Swal.fire("Todos los campos obligatorios deben ser llenados", '', 'warning')
}