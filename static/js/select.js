$(document).ready(function(){
   $("#jobSelectBox").change(function(){
        if ($(this).val() == "other") {
            $("#jobOthersInput input").attr("required", "");
            $("#jobOthersInput").show();
        }
        else {
            $("#jobOthersInput input").removeAttr("required");
            $("#jobOthersInput").hide();
        }
    });
});
