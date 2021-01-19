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

    var activeSystemClass = $('.list-group-item.active');

    //something is entered in search form
    $('#system-search').keyup( function() {
       var that = this;
        // affect all table rows on in systems table
        var tableBody = $('.table-list-search tbody');
        var tableRowsClass = $('.table-list-search tbody tr');
        $('.search-sf').remove();
        tableRowsClass.each( function(i, val) {
        
            //Lower text for case insensitive
            var rowText = $(val).text().toLowerCase();
            var inputText = $(that).val().toLowerCase();
            if(inputText != '')
            {
                $('.search-query-sf').remove();
                tableBody.prepend('<tr class="search-query-sf"><td colspan="6"><strong>Searching for: "'
                    + $(that).val()
                    + '"</strong></td></tr>');
            }
            else
            {
                $('.search-query-sf').remove();
            }

            if( rowText.indexOf( inputText ) == -1 )
            {
                //hide rows
                tableRowsClass.eq(i).hide();
                
            }
            else
            {
                $('.search-sf').remove();
                tableRowsClass.eq(i).show();
            }
        });
        //all tr elements are hidden
        if(tableRowsClass.children(':visible').length == 0)
        {
            tableBody.append('<tr class="search-sf"><td class="text-muted" colspan="6">No entries found.</td></tr>');
        }
    });

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