<!DOCTYPE html>
<html>
<head>
	<title>Homepage</title>
	<?php $this->load->view('component/htmlhead'); ?>
</head>
<body>
	<div id="container" class="container">
		<?php $this->load->view('component/header'); ?>

		<?php $this->load->view($template); ?>

		<?php $this->load->view('component/footer'); ?>
	</div>

	<?php $this->load->view('component/htmlfooter'); ?>
</body>
</html>