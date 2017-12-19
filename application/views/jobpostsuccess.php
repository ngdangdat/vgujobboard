<div class="success-message">
	<?php if($isPostScheduled) { ?>
		<p>You job is scheduled successfully. If the content is valid, it will be published at <?php echo date_format($scheduledTime, 'H:i d-m-Y'); ?>.</p>
	<?php }else{ ?>
		<p> Your post is posted successfully. Kindly click this <a href="<?php echo $postUrl; ?>">link</a> to view </p>
	<?php } ?>
</div>