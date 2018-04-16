$(document).ready(function(){
   $("#id_field").change(function(){
       var other_field_wrp = $("#id_other_field").parents('.form-row');
        if (!$(this).val()) {
            other_field_wrp.show();
        } else {
            other_field_wrp.hide();
        }
    });
    $("#id_field").trigger('change');
});
