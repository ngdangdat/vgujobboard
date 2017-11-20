function checkIfOthersSelected() {
    var selectBox = document.getElementById("jobSelectBox");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
	var othersInput = document.getElementById("jobOthersInput");

    if (selectedValue == "Others") {
        othersInput.childNodes[1].setAttribute("required","");
        othersInput.style.display = "block";
    }
    else {
        othersInput.childNodes[1].removeAttribute("required");
        othersInput.style.display = "none";
    }
}
