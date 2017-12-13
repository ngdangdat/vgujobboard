'use strict';

var uploadcareWrapper = $('.uploadcare-wrapper');
var previewSize = '300x300';

function uploadcareHandler(){
	var uploader = $('[role="uploadcare-uploader"]');
	var widget = uploadcare.Widget(uploader);

	widget.onUploadComplete(function(info){
		var url = info.originalUrl;
		var previewUrl = url + '-/preview/' + previewSize + '/';
		uploadcareWrapper.find('.uploadcare_image').show();
		uploadcareWrapper.find('.image_preview').attr('src', previewUrl);
	});
}

function initializeEvents(){
	if($('[role="uploadcare-uploader"]').length){
		uploadcareHandler();
		$(document).on('click', '.uploadcare--widget__button_type_remove', function(){
			uploadcareWrapper.find('.uploadcare_image').hide();
		});
	};
}

initializeEvents();