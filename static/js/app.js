$(document).ready(function(){
	$('.slider-loader').fadeOut('slow');
});

$('form').on('submit', function(e){
	$('.slider-loader').show();
});