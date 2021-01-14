function moddata() {
    Swal.fire({
        title: '¿Desea modificar los datos del medicamento?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: `Sí, modificar medicamentos`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }) .then((result) => {
        if (result.isConfirmed) {
            Swal.fire("Solicitud de modificacion enviada", '', 'success');
        }
    });
}

function bajamed() {
    Swal.fire({
        title: '¿Estas seguro de dar de baja este medicamento?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: `Sí, dar de baja medicamento`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }) .then((result) => {
        if (result.isConfirmed) {
            Swal.fire("Medicamento dado de baja con exito", '', 'success');
        }
    });
}