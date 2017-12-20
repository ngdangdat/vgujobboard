<?php
    $this->lang->load('forms', 'english');
    echo form_open('handle/job');
?>
    <div class="row">
        <?php if(isset($formError) && $formError) { ?>
            <div class="form-post-error error">
                <span>
                    Error occured while processing your inputs. Please submit form again or contact us! Sorry!
                </span>
            </div>
        <?php } ?>
        <div class="job-category form-row col-12 col-m-12">
            <label for="job_category">
                <?php echo $this->lang->line('label.job.field'); ?><span class="required">*</span>
            </label>
            <?php echo form_dropdown(
                array(
                    'name'  => 'job_category',
                    'id'    => 'jobSelectBox',
                    'class' => 'input-select',
                    'value' => set_value('job_category')
                ),
                array(
                    'acc_aud' => $this->lang->line('job.fields.acc_aud'),
                    'art_design' => $this->lang->line('job.fields.art_design'),
                    'bank_consultant' => $this->lang->line('job.fields.bank_consultant'),
                    'civil_construction' => $this->lang->line('job.fields.civil_construction'),
                    'electrical_electric' => $this->lang->line('job.fields.electrical_electric'),
                    'finance' => $this->lang->line('job.fields.finance'),
                    'human_resource' => $this->lang->line('job.fields.human_resource'),
                    'it' => $this->lang->line('job.fields.it'),
                    'logistics' => $this->lang->line('job.fields.logistics'),
                    'marketing' => $this->lang->line('job.fields.marketing'),
                    'sale_cs' => $this->lang->line('job.fields.sale_cs'),
                    'other' => $this->lang->line('job.fields.other'),
                )
            ); ?>
        </div>
        <div class="job-category-others form-row col-12 col-m-12" id="jobOthersInput">
            <?php echo form_input(
                array(
                    'name' => 'job_category_others',
                    'placeholder' => 'Job Field is',
                    'class' => 'input-text',
                    'value' => set_value('job_category_others')
                )
            ); ?>
            <?php echo form_error('job_category_others'); ?>
        </div>
        <div class="job-title form-row <col-12 col-m-12">
            <label for="job_title">
                <?php echo $this->lang->line('label.job.title'); ?><span class="required">*</span>
            </label>
            <?php echo form_input(
                array(
                    'name' => 'job_title',
                    'class' => 'input-text',
                    'value' => set_value('job_title')
                )
            ); ?>
            <?php echo form_error('job_title'); ?>
        </div>
        <div class="company form-row col-12 col-m-12">
            <label for="company">
                <?php echo $this->lang->line('label.job.company'); ?><span class="required">*</span>
            </label>
            <?php echo form_input(
                array(
                    'name' => 'company',
                    'class' => 'input-text',
                    'value' => set_value('company')
                )
            );?>
            <?php echo form_error('company'); ?>
        </div>
        <div class="job-desc form-row col-12 col-m-12">
            <label for="job_desc">
                <?php echo $this->lang->line('label.job.description'); ?>
            </label>
            <?php echo form_textarea(
                array(
                    'name' => 'job_desc',
                    'class' => 'input-textarea',
                    'value' => set_value('job_desc')
                )
            );?>
            <?php echo form_error('job_desc'); ?>
        </div>
        <div class="job-require form-row col-12 col-m-12">
            <label for="job_require">
                <?php echo $this->lang->line('label.job.requirement'); ?><span class="required">*</span>
            </label>
            <?php echo form_textarea(
                array(
                    'name' => 'job_require',
                    'class' => 'input-textarea',
                    'value' => set_value('job_require')
                )
            );?>
            <?php echo form_error('job_require'); ?>
        </div>
        <div class="salary form-row col-12 col-m-12">
            <label for="salary">
                <?php echo $this->lang->line('label.job.salary'); ?>
            </label>
            <?php echo form_input(
                array(
                    'name' => 'salary',
                    'class' => 'input-text',
                    'value' => set_value('salary')
                )
            );?>
            <?php echo form_error('salary'); ?>
        </div>
        <div class="benefit form-row col-12 col-m-12">
            <label for="benefit">
                <?php echo $this->lang->line('label.job.benefit'); ?>
            </label>
            <?php echo form_textarea(
                array(
                    'name' => 'benefit',
                    'class' => 'input-textarea',
                    'value' => set_value('benefi')
                )
            );?>
            <?php echo form_error('benefit'); ?>
        </div>
        <div class="job-contact-submit form-row col-12 col-m-12">
            <label for="job_contact">
                <?php echo $this->lang->line('label.job.resume'); ?><span class="required">*</span>
            </label>
            <?php echo form_input(
                array(
                    'name' => 'job_contact_submit',
                    'class' => 'input-text',
                    'value' => set_value('job_contact_submit')
                )
            );?>
            <?php echo form_error('job_contact_submit'); ?>
        </div>
        <div class="deadline form-row col-12 col-m-12">
            <label for="deadline">
                <?php echo $this->lang->line('label.job.deadline'); ?><span class="required">*</span>
            </label>
            <?php echo form_input(
                array(
                    'type' => 'text',
                    'name' => 'deadline',
                    'class' => 'input-text',
                    'id' => 'datepicker',
                    'value' => set_value('deadline'),
                    'readonly' => 'true'
                )
            );?>
            <?php echo form_error('deadline'); ?>
        </div>
        <div class="job-contact-contributor form-row col-12 col-m-12">
            <label for="job_contact">
                <?php echo $this->lang->line('label.job.yourcontact.front'); ?>
            </label>
            <?php echo form_input(
                array(
                    'name' => 'job_contact_contributor',
                    'class' => 'input-text',
                    'value' => set_value('job_contact_contributor')
                )
            );?>
            <?php echo form_error('job_contact_contributor'); ?>
        </div>
        <div class="job-image form-row col-12 col-m-12">
            <label for="job_image">
                <?php echo $this->lang->line('label.job.image'); ?>
            </label>
            <div class="uploadcare-wrapper">
                <div class="uploadcare_image" style="display: none;">
                    <img class="image_preview">
                </div>
                <input type="hidden" role="uploadcare-uploader" name="job_image" data-images-only="true" />
            </div>
        </div>
        <div class="form-row btn">
            <button type="submit" class="submit-btn">
                <svg version="1.1" class="send-icn" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="100px" height="36px" viewBox="0 0 100 36" enable-background="new 0 0 100 36" xml:space="preserve">
                    <path d="M100,0L100,0 M23.8,7.1L100,0L40.9,36l-4.7-7.5L22,34.8l-4-11L0,30.5L16.4,8.7l5.4,15L23,7L23.8,7.1z M16.8,20.4l-1.5-4.3 l-5.1,6.7L16.8,20.4z M34.4,25.4l-8.1-13.1L25,29.6L34.4,25.4z M35.2,13.2l8.1,13.1L70,9.9L35.2,13.2z"/>
                </svg>
                <small><?php echo $this->lang->line('button.submit'); ?></small>
            </button>
        </div>
    </div>
<?php echo form_close(); ?>
