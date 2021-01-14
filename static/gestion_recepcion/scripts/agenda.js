function eliminar() {
    Swal.fire({
        title: '¿Seguro que quiere eliminar cita?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: `Sí, eliminar cita`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }) .then((result) => {
        if (result.isConfirmed) {
            Swal.fire("Cita eliminada con éxito", '', 'success');
        }
    });
}
