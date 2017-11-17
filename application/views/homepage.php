<? $this->load->helper('form'); ?>

<form id="postJob" class="post-job-form" action="handlejob.php" method="POST" accept-charset="UTF-8">
	<div class="job-category form-row">
		<label for="job_category">Job Field</label>
		<select name="job_category" id="jobSelectBox" onchange="checkIfOthersSelected();">
			<option value="IT-SW">IT - Software</option>
			<option value="IT-HW">IT - Hardware/Networking</option>
			<option value="Electrical">Electrical/Electronics</option>
			<option value="Finance">Finance</option>
			<option value="Accounting">Finance</option>
			<option value="Administration">Administration</option>
			<option value="Marketing">Marketing</option>
			<option value="Banking">Banking</option>
			<option value="Sales">Sales</option>
			<option value="Translator">Interpreter/Translator</option>
			<option value="Others">Others</option>
		</select>
	</div>
	<div class="job-category-others form-row" id="jobOthersInput">
		<input name="job_category_others" type="text" placeholder="Job Field is"/>
	</div>
	<div class="job-title form-row">
		<label for="job_title">Job Title</label>
		<input name="job_title" type="text" />
	</div>
	<div class="company form-row">
		<label for="company">Company Name</label>
		<input name="company" type="text" />
	</div>
	<div class="job-desc form-row">
		<label for="job_desc">Job Description</label>
		<textarea rows="6" name="job_desc" ></textarea>
	</div>
	<div class="job-require form-row">
		<label for="job_require">Job Requirements</label>
		<textarea rows="6" name="job_require"></textarea>
	</div>
	<div class="salary form-row">
		<label for="salary">Salary</label>
		<input name="salary" type="text" />
	</div>
	<div class="benefit form-row">
		<label for="benefit">Benefits</label>
		<textarea rows="6" name="benefit"></textarea>
	</div>
	<div class="job-contact-submit form-row">
		<label for="job_contact">Contact to CV Submission</label>
		<textarea rows="6" name="job_contact_submit"></textarea>
	</div>
	<div class="deadline form-row">
		<label for="deadline">Deadline</label>
		<input name="deadline" type="date" />
	</div>
	<div class="job-contact-contributor form-row">
		<label for="job_contact">Contact to Contributor</label>
		<textarea rows="6" name="job_contact_contributor"></textarea>
	</div>
	<div class="job-image form-row">
		<label for="job_image">Image</label>
		<input name="job_image" id="jobImage" type="file">
	</div>
	<div class="form-row btn">
		<button type="submit" class="submit-btn">
			<svg version="1.1" class="send-icn" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="100px" height="36px" viewBox="0 0 100 36" enable-background="new 0 0 100 36" xml:space="preserve">
				<path d="M100,0L100,0 M23.8,7.1L100,0L40.9,36l-4.7-7.5L22,34.8l-4-11L0,30.5L16.4,8.7l5.4,15L23,7L23.8,7.1z M16.8,20.4l-1.5-4.3 l-5.1,6.7L16.8,20.4z M34.4,25.4l-8.1-13.1L25,29.6L34.4,25.4z M35.2,13.2l8.1,13.1L70,9.9L35.2,13.2z"/>
			</svg>
			<small>Submit</small>
		</button>
	</div>
</form>
</div>