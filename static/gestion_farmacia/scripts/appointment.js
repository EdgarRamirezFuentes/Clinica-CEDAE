function finalizarConsulta() {
    Swal.fire({
        title: '¿Los datos ingresados son correctos?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: `Sí, finalizar consulta`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire("Datos de consulta registrados correctamente", '', 'success');
        }
    });
}