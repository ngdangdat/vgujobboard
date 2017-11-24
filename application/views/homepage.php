<?= form_open('handle/job'); ?>
    <div class="row">
        <div class="job-category form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_category">Job Field</label>
            <?= form_dropdown(
                array(
                    'name'  => 'job_category',
                    'id'    => 'jobSelectBox',
                    'class' => 'col-9 col-m-12'
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
            <?= form_input(
                array(
                    'name' => 'job_category_others',
                    'placeholder' => 'Job Field is',
                    'class' => 'col-9 col-m-12'
                )
            ); ?>
        </div>
        <div class="job-title form-row <col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_title" class='col-9 col-m-12'>Job Title</label>
            <?= form_input(
                array(
                    'name' => 'job_title',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="company form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="company">Company Name</label>
            <?= form_input(
                array(
                    'name' => 'company',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="job-desc form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_desc">Job Description</label>
            <?= form_textarea(
                array(
                    'name' => 'job_desc',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="job-require form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_require">Job Requirements</label>
            <?= form_textarea(
                array(
                    'name' => 'job_require',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="salary form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="salary">Salary</label>
            <?= form_input(
                array(
                    'name' => 'salary',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="benefit form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="benefit">Benefits</label>
            <?= form_textarea(
                array(
                    'name' => 'benefit',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="job-contact-submit form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_contact">Contact to CV Submission</label>
            <?= form_textarea(
                array(
                    'name' => 'job_contact_submit',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="deadline form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="deadline">Deadline</label>
            <?= form_input(
                array(
                    'type' => 'date',
                    'name' => 'deadline',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="job-contact-contributor form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_contact">Contact to Contributor</label>
            <?= form_textarea(
                array(
                    'name' => 'job_contact_contributor',
                    'class' => 'col-9 col-m-12'
                )
            );?>
        </div>
        <div class="job-image form-row col-12 col-m-12">
            <label class="col-3 col-m-12" for="job_image">Image</label>
            <?= form_upload(
                array(
                    'name' => 'job_image',
                    'id'   => 'jobImage',
                    'class' => 'col-9 col-m-12'
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
    </div>
<?= form_close(); ?>