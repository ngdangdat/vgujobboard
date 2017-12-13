<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Handle extends CI_Controller {
    public function job() {
        $this->load->library('Form_validation');
        $this->load->library('Job');
        $this->load->helper('facebook');
        $this->load->helper('time');
        $this->load->helper('form');
        $this->lang->load('forms', 'english');

        $exportedVars = array();
        if($this->form_validation->run('job') === FALSE) {
            $exportedVars['template'] = 'homepage';
        }else{
            $jobCat                 = $this->input->post('job_category');
            $jobTitle               = $this->input->post('job_title');
            $company                = $this->input->post('company');
            $jobDesc                = $this->input->post('job_desc');
            $jobRequire             = $this->input->post('job_require');
            $salary                 = $this->input->post('salary');
            $benefit                = $this->input->post('benefit');
            $jobContactSubmit       = $this->input->post('job_contact_submit');
            $deadline               = $this->input->post('deadline');
            $jobContactContributor  = $this->input->post('job_contact_contributor');
            $jobImage               = $this->input->post('job_image');

            if($jobCat == 'other'){
                $jobCat = $this->input->post('job_category_others');
                if(empty($jobCat)){
                    $jobCat = $this->lang->line('job.fields.other');
                }
            }else{
                $jobCat = $this->lang->line('job.fields.' . $jobCat);
            }

            $job = new Job(
                array (
                    'jobCategory' => $jobCat,
                    'jobTitle' => $jobTitle,
                    'jobDescription' => $jobDesc,
                    'jobRequirement' => $jobRequire,
                    'company' => $company,
                    'salary' => $salary,
                    'benefit' => $benefit,
                    'jobDeadline' => $deadline,
                    'contactPointSubmission' => $jobContactSubmit,
                    'contactPointContributor' => $jobContactContributor,
                    'jobImage' => $jobImage
                )
            );

            $caption                    = $job->getCaption();
            $image                      = $job->getJobImage();
            $scheduledTimestamp         = getScheduledTimeString();
            $postResult                 = postImageToFacebook($image, $caption, false, $scheduledTimestamp);
            $isPostSuccess              = $postResult['isSuccess'];
            if($isPostSuccess){
                $exportedVars['template']   = 'jobpostsuccess';
                $isPostScheduled            = $postResult['isScheduled'];
                $exportedVars['isPostScheduled']   = $isPostScheduled;
            }else{
                $exportedVars['template']   = 'homepage';
                $exportedVars['formError'] = TRUE;
            }
        }
        $this->load->view('container/pt_homepage', $exportedVars);
    }
}
