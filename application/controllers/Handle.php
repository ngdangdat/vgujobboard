<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Handle extends CI_Controller {
    public function job() {
        $this->load->library('Job');
        $this->load->helper('facebook');

        $jobCat = $this->input->post('job_category');
        $jobTitle = $this->input->post('job_title');
        $company = $this->input->post('company');
        $jobDesc = $this->input->post('job_desc');
        $jobRequire = $this->input->post('job_require');
        $salary = $this->input->post('salary');
        $benefit = $this->input->post('benefit');
        $jobContactSubmit = $this->input->post('job_contact_submit');
        $deadline = $this->input->post('deadline');
        $jobContactContributor = $this->input->post('job_contact_contributor');
        $job = new Job(
            array (
                "jobCategory" => $jobCat,
                "jobTitle" => $jobTitle,
                "jobDescription" => $jobDesc,
                "jobRequirement" => $jobRequire,
                "company" => $company,
                "salary" => $salary,
                "benefit" => $benefit,
                "jobDeadline" => $deadline,
                "contactPointSubmission" => $jobContactSubmit,
                "contactPointContributor" => $jobContactContributor,
                "jobImage" => 'https://boardsource.org/wp-content/uploads/2016/05/Board-Member-Job-Description.png'
            )
        );
        $caption = $job->getCaption();
        $image = $job->getJobImage();
        $postUrl = postImageToFacebook($image, $caption, '672115002991670');
        $vars = array();
        $vars['postUrl'] = $postUrl;
        $vars['template'] = 'jobpostresult';
        $this->load->view('container/pt_homepage', $vars);
    }
}
