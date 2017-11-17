<!DOCTYPE html>
<html>
<head>
	<title>Homepage</title>
	<?php $this->load->view('component/htmlhead'); ?>
</head>
<body>
	<div id="container" class="container">
		<? $this->load->view('component/header'); ?>

		<? $this->load->view($template); ?>

		<? $this->load->view('component/footer'); ?>
	</div>

	<? $this->load->view('component/htmlfooter'); ?>
</body>
</html>