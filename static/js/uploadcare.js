'use strict';

function uploadcareHandler(){
	var uploader = $('[role="uploadcare-uploader"]');
	var widget = uploadcare.Widget(uploader);

	widget.onUploadComplete(function(info){
		console.log(info);
	});
}

function initializeEvents(){
	if($('[role="uploadcare-uploader"]').length){
		uploadcareHandler();
	};
}

initializeEvents();