$(document).ready(function () {

    var quantitiy = 0;
    $('.quantity-right-plus').click(function (e) {

        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#quantity').val());

        // If is not undefined

        $('#quantity').val(quantity + 1);


        // Increment

    });

    $('.quantity-left-minus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('#quantity').val());

        // If is not undefined

        // Increment
        if (quantity > 0) {
            $('#quantity').val(quantity - 1);
        }
    });

    let medicamentos = document.getElementsByClassName("medicamentosStock");
    console.log(medicamentos);

});

function agregarATicket(sku) {
    let medicamento = document.getElementById(sku);
    let boton = document.getElementById("btn"+sku);
    boton.innerText = "Eliminar del ticket";
    boton.setAttribute("onclick", "eliminarDeTicket(" + sku + ")");
    boton.className = "btn btn-danger";
    let ticketContainer = document.getElementById("ticketContainer");
    ticketContainer.append(medicamento);
}

function eliminarDeTicket(sku) {
    let medicamento = document.getElementById(sku);
    let boton = document.getElementById("btn"+sku);
    let medicamentosContainer = document.getElementById("medicamentosContainer");
    boton.setAttribute("onclick", "agregarATicket(" + sku + ")");
    boton.innerText = "Agregar a ticket";
    boton.className = "btn btn-primary";
    medicamentosContainer.append(medicamento);
}