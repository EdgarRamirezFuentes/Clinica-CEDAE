var num = 0;
function agregarMedicamento(numero) {
    num = num + numero;
    var divParent = document.createElement("div");
    //------------------------------------------------------------------:
    var divDrug = document.createElement("div");
    var labelDrug = document.createElement("label");
    var labelDrugText = document.createTextNode("Medicamento");
    var selectDrug = document.createElement("select");
    var optionDrug = document.createElement("option");
    var optionDrug2 = document.createElement("option");
    var optionDrug3 = document.createElement("option");
    var optionDrugText = document.createTextNode("Paracetamol 200mg");
    var optionDrugText2 = document.createTextNode("Aspirina 200mg");
    var optionDrugText3 = document.createTextNode("Droga recia 200mg");
    //-----------------------------------------------------------------:
    var divIndications = document.createElement("div");
    var labelIndications = document.createElement("label");
    var labelIndicationsText = document.createTextNode("Indicaciones");
    var textAreaIndications = document.createElement("textarea");

    labelDrug.appendChild(labelDrugText);

    optionDrug.appendChild(optionDrugText);
    selectDrug.appendChild(optionDrug);

    optionDrug2.appendChild(optionDrugText2);
    selectDrug.appendChild(optionDrug2);

    optionDrug3.appendChild(optionDrugText3);
    selectDrug.appendChild(optionDrug3);

    selectDrug.className = "form-control";
    selectDrug.id = "med"+num;
    selectDrug.name = "med"+num;

    divDrug.appendChild(labelDrugText);
    divDrug.appendChild(selectDrug);
    divDrug.className = "form-group";
    
    divParent.appendChild(divDrug);
    //--------------------------------------------------:
    labelIndications.appendChild(labelIndicationsText);
    
    textAreaIndications.className = "form-control";
    textAreaIndications.id="ind"+num;
    textAreaIndications.name="ind"+num;

    divIndications.appendChild(labelIndications);
    divIndications.appendChild(textAreaIndications);
    divIndications.className = "form-group";

    divParent.appendChild(divIndications);

    divParent.id = "medicamento"+num;

    var element = document.getElementById("newDrug");
    element.appendChild(divParent);                     

}

function eliminarMedicamento(){
    idMed = 'medicamento'+num;
    var element = document.getElementById(idMed);
    element.remove();
    num = num - 1;
}

//obtener datos para la receta
var medicamento = []
var inst = []
for (let index = 1; index < num+1; index++) {
    medicamento.push(document.getElementById("med"+index))
    inst.push(document.getElementById("ind"+index))
}

function registrarReceta() {
    Swal.fire({
        title: '¿Los datos ingresados son correctos?',
        icon: 'question',
        showCancelButton: 1,
        confirmButtonText: `Sí, registrar receta`,
        cancelButtonText: 'Cancelar',
        cancelButtonColor: '#ff4d4d',
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById("recetaForm").submit();
        }
    });
}