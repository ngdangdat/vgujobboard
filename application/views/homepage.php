<?php echo form_open('handle/job'); ?>
    <div class="row">
        <div class="job-category form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_category">Job Field</label>
            <?php echo form_dropdown(
                array(
                    'name'  => 'job_category',
                    'id'    => 'jobSelectBox',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_category')
                ),
                array(
                    'acc_aud' => 'Accounting/Auditing',
                    'art_design' => 'Arts/Design',
                    'bank_consultant' => 'Banking/Consulting',
                    'civil_construction' => 'Civil/Construction',
                    'electrical_electric' => 'Electrical/Electrics',
                    'finance' => 'Finance',
                    'human_resource' => 'Human Resources',
                    'it' => 'IT',
                    'logistics' => 'Logistics/Suply Chain',
                    'marketing' => 'Marketing',
                    'sale_cs' => 'Sales/ Customer Services',
                    'other' => 'Other',
                )
            ); ?>
        </div>
        <div class="job-category-others form-row col-12 col-m-12" id="jobOthersInput">
            <?php echo form_input(
                array(
                    'name' => 'job_category_others',
                    'placeholder' => 'Job Field is',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_category_others')
                )
            ); ?>
            <?php echo form_error('job_category_others'); ?>
        </div>
        <div class="job-title form-row <col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_title" class='col-10 col-m-12'>Job Title</label>
            <?php echo form_input(
                array(
                    'name' => 'job_title',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_title')
                )
            ); ?>
            <?php echo form_error('job_title'); ?>
        </div>
        <div class="company form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="company">Company Name</label>
            <?php echo form_input(
                array(
                    'name' => 'company',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('company')
                )
            );?>
            <?php echo form_error('company'); ?>
        </div>
        <div class="job-desc form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_desc">Job Description</label>
            <?php echo form_textarea(
                array(
                    'name' => 'job_desc',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_desc')
                )
            );?>
            <?php echo form_error('job_desc'); ?>
        </div>
        <div class="job-require form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_require">Job Requirements</label>
            <?php echo form_textarea(
                array(
                    'name' => 'job_require',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_require')
                )
            );?>
            <?php echo form_error('job_require'); ?>
        </div>
        <div class="salary form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="salary">Salary</label>
            <?php echo form_input(
                array(
                    'name' => 'salary',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('salary')
                )
            );?>
            <?php echo form_error('salary'); ?>
        </div>
        <div class="benefit form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="benefit">Benefits</label>
            <?php echo form_textarea(
                array(
                    'name' => 'benefit',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('benefi')
                )
            );?>
            <?php echo form_error('benefit'); ?>
        </div>
        <div class="job-contact-submit form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_contact">Contact to CV Submission</label>
            <?php echo form_textarea(
                array(
                    'name' => 'job_contact_submit',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_contact_submit')
                )
            );?>
            <?php echo form_error('job_contact_submit'); ?>
        </div>
        <div class="deadline form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="deadline">Deadline</label>
            <?php echo form_input(
                array(
                    'type' => 'date',
                    'name' => 'deadline',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('deadline')
                )
            );?>
            <?php echo form_error('deadline'); ?>
        </div>
        <div class="job-contact-contributor form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_contact">Contact to Contributor</label>
            <?php echo form_textarea(
                array(
                    'name' => 'job_contact_contributor',
                    'class' => 'col-9 pull-right col-m-12',
                    'value' => set_value('job_contact_contributor')
                )
            );?>
            <?php echo form_error('job_contact_contributor'); ?>
        </div>
        <div class="job-image form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_image">Image</label>
            <?php echo form_upload(
                array(
                    'name' => 'job_image',
                    'id'   => 'jobImage',
                    'class' => 'col-9 pull-right col-m-12'
                )
            ); ?>
            <?php echo form_error('job_image'); ?>
        </div>
        <div class="form-row btn">
            <button type="submit" class="submit-btn">
                <svg version="1.1" class="send-icn" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="100px" height="36px" viewBox="0 0 100 36" enable-background="new 0 0 100 36" xml:space="preserve">
                    <path d="M100,0L100,0 M23.8,7.1L100,0L40.9,36l-4.7-7.5L22,34.8l-4-11L0,30.5L16.4,8.7l5.4,15L23,7L23.8,7.1z M16.8,20.4l-1.5-4.3 l-5.1,6.7L16.8,20.4z M34.4,25.4l-8.1-13.1L25,29.6L34.4,25.4z M35.2,13.2l8.1,13.1L70,9.9L35.2,13.2z"/>
                </svg>
                <small>Submit</small>
            </button>
        </div>
    </div>
<?php echo form_close(); ?>