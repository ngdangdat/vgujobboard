<?= form_open('job/process'); ?>
    <div class="job-category form-row">
        <label for="job_category">Job Field</label>
        <?= form_dropdown(
            array(
                'name'  => 'job_category',
                'id'    => 'jobSelectBox',
                'onchange' => 'checkIfOthersSelected();'
            ),
            array(
                'IT-SW' => 'IT - Software',
                'IT-HW' => 'IT - Hardware/Networking',
                'Electrical' => 'Electrical/Electronics',
                'Finance' => 'Finance',
                'Accounting' => 'Finance',
                'Administration' => 'Administration',
                'Marketing' => 'Marketing',
                'Banking' => 'Banking',
                'Sales' => 'Sales',
                'Translator' => 'Interpreter/Translator',
                'Others' => 'Others'
            )
            ); ?>
    </div>
    <div class="job-category-others form-row" id="jobOthersInput">
        <?= form_input(
            array(
                'name' => 'job_category_others',
                'placeholder' => 'Job Field is'
            )
        ); ?>
    </div>
    <div class="job-title form-row">
        <label for="job_title">Job Title</label>
        <?= form_input('job_title'); ?>
    </div>
    <div class="company form-row">
        <label for="company">Company Name</label>
        <?= form_input('company'); ?>
    </div>
    <div class="job-desc form-row">
        <label for="job_desc">Job Description</label>
        <?= form_textarea('job_desc'); ?>
    </div>
    <div class="job-require form-row">
        <label for="job_require">Job Requirements</label>
        <?= form_textarea('job_require'); ?>
    </div>
    <div class="salary form-row">
        <label for="salary">Salary</label>
        <?= form_input('salary'); ?>
    </div>
    <div class="benefit form-row">
        <label for="benefit">Benefits</label>
        <?= form_textarea('benefit'); ?>
    </div>
    <div class="job-contact-submit form-row">
        <label for="job_contact">Contact to CV Submission</label>
        <?= form_textarea('job_contact_submit'); ?>
    </div>
    <div class="deadline form-row">
        <label for="deadline">Deadline</label>
        <?= form_input(
            array(
                'type' => 'date',
                'name' => 'deadline'
            )
        ); ?>
    </div>
    <div class="job-contact-contributor form-row">
        <label for="job_contact">Contact to Contributor</label>
        <?= form_textarea('job_contact_contributor'); ?>
    </div>
    <div class="job-image form-row">
        <label for="job_image">Image</label>
        <?= form_upload(
            array(
                'name' => 'job_image',
                'id'   => 'jobImage'
            )
        ); ?>
    </div>
    <div class="form-row btn">
        <button type="submit" class="submit-btn">
            <svg version="1.1" class="send-icn" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="100px" height="36px" viewBox="0 0 100 36" enable-background="new 0 0 100 36" xml:space="preserve">
                <path d="M100,0L100,0 M23.8,7.1L100,0L40.9,36l-4.7-7.5L22,34.8l-4-11L0,30.5L16.4,8.7l5.4,15L23,7L23.8,7.1z M16.8,20.4l-1.5-4.3 l-5.1,6.7L16.8,20.4z M34.4,25.4l-8.1-13.1L25,29.6L34.4,25.4z M35.2,13.2l8.1,13.1L70,9.9L35.2,13.2z"/>
            </svg>
            <small>Submit</small>
        </button>
    </div>
<?= form_close(); ?>