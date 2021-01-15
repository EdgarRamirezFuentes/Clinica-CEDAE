var num = 0;
function agregarMedicamento(numero, listaMeds) {
    num = num + numero;
    var divParent = document.createElement("div");
    //------------------------------------------------------------------:
    var divDrug = document.createElement("div");
    var labelDrug = document.createElement("label");
    var labelDrugText = document.createTextNode("Medicamento");
    var selectDrug = 0;
    var selectDrugGod = document.getElementById("medSelect")

    selectDrug = selectDrugGod.cloneNode(true); //este es el datalist

    var inputSelectDrug = document.createElement("input"); //input para el datalist

    //-----------------------------------------------------------------:
    var divIndications = document.createElement("div");
    var labelIndications = document.createElement("label");
    var labelIndicationsText = document.createTextNode("Indicaciones");
    var textAreaIndications = document.createElement("textarea");

    labelDrug.appendChild(labelDrugText);

    inputSelectDrug.style = "";
    inputSelectDrug.className = "form-control";
    inputSelectDrug.id = "med"+num;
    inputSelectDrug.name = "med"+num;
    inputSelectDrug.setAttribute('list', "datalist"+num);

    selectDrug.style = "";
    selectDrug.id = "datalist"+num;

    divDrug.appendChild(labelDrugText);
    divDrug.appendChild(inputSelectDrug);
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