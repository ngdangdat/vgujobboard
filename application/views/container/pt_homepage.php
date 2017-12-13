<!DOCTYPE html>
<html>
<head>
	<title>Homepage</title>
	<?php $this->load->view('component/htmlhead'); ?>
</head>
<body>
	<div class="slider-loader"></div>
	<div id="container" class="container">
		<?php $this->load->view('component/header'); ?>
		<div class="inner">
			<?php $this->load->view($template); ?>
		</div>
		<?php $this->load->view('component/footer'); ?>
	</div>

	<?php $this->load->view('component/htmlfooter'); ?>
</body>
</html>