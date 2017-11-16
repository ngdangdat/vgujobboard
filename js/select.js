function checkIfOthersSelected() {
    var selectBox = document.getElementById("jobSelectBox");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
	var othersInput = document.getElementById("jobOthersInput");

    if (selectedValue == "Others")
    	othersInput.style.display = "block";
    else
    	othersInput.style.display = "none";
}
