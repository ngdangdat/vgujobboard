<!DOCTYPE html>
<html>
<head>
	<title></title>
	<?php $this->load->view('component/htmlhead'); ?>
</head>
<body>

	<?php $this->load->view('component/header'); ?>

	<?php $this->load->view($template); ?>

	<?php $this->load->view('component/footer'); ?>

	<?php $this->load->view('component/htmlfooter'); ?>
</body>
</html>