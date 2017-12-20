<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Job {
    protected $defaultImageUrl;
    protected $jobCategory;
    protected $jobTitle;
    protected $jobDescription;
    protected $jobRequirement;
    protected $company;
    protected $salary;
    protected $benefit;
    protected $contactPointSubmission;
    protected $contactPointContributor;
    protected $jobImage;
    protected $jobDeadline;
    protected $prefix;

    public function __construct($fields = array()) {
        $this->CI =& get_instance();
        $this->CI->load->helper('static');
        $this->CI->lang->load('forms', 'english');
        $this->defaultImageUrl = array(
            'acc_aud' => 'images/job/accounting-auditing-min.jpg',
            'art_design' => 'images/job/arts-design-min.jpg',
            'bank_consultant' => 'images/job/banking-consulting-min.jpg',
            'civil_construction' => 'images/job/civil-construction-min.jpg',
            'electrical_electric' => 'images/job/electrical-electrics-min.jpg',
            'finance' => 'images/job/finance-min.jpg',
            'human_resource' => 'images/job/human-resources-min.jpg',
            'it' => 'images/job/it-min.jpg',
            'logistics' => 'images/job/logistics-supply-chain-min.jpg',
            'marketing' => 'images/job/marketing-min.jpg',
            'sale_cs' => 'images/job/other-min.jpg',
            'other' => 'images/job/sales-customer-services-min.jpg'
        );

        

        if(count($fields) > 0) {
            $this->jobCategory = $fields['jobCategory'];
            $this->jobTitle = $fields['jobTitle'];
            $this->jobDescription = $fields['jobDescription'];
            $this->jobRequirement = $fields['jobRequirement'];
            $this->company = $fields['company'];
            $this->salary = $fields['salary'];
            $this->benefit = $fields['benefit'];
            $this->contactPointSubmission = $fields['contactPointSubmission'];
            $this->contactPointContributor = $fields['contactPointContributor'];
            $this->jobImage = $fields['jobImage'];
            $this->jobDeadline = $fields['jobDeadline'];
        }
    }

     public function getCaption() {
        if(array_key_exists($this->jobCategory, $this->defaultImageUrl))
        {
            $jobCat = $this->CI->lang->line('job.fields.' . $this->jobCategory);
        }else{
            if(empty($this->jobCategory)){
                $jobCat = $this->CI->lang->line('job.fields.other');
            }else{
                $jobCat = $this->jobCategory;
            }
        }
        $fields = array(
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.field'), $jobCat),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.title'), $this->jobTitle),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.company'), $this->company),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.description'), $this->jobDescription),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.requirement'), $this->jobRequirement),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.salary'), $this->salary),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.benefit'), $this->benefit),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.resume'), $this->contactPointSubmission),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.deadline'), $this->jobDeadline),
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.yourcontact.back'), $this->contactPointContributor)
        );

        return join(chr(10).chr(10), $fields);
    }

    public function getJobImage() {

        if($this->jobImage == '') {
            if(!empty($this->jobCategory) && array_key_exists($this->jobCategory, $this->defaultImageUrl))
            {
                $jobCat = $this->jobCategory;
            }else{
                $jobCat = 'other';
            }
            $path = $this->defaultImageUrl[$this->jobCategory];
            return getContentPath($path);
        }


        return $this->jobImage;
    }

    private function getFieldWithPrefix($prefix, $value){
        if(!$value){
            return NULL;
        }

        if(!$prefix){
            return $value;
        }

        return sprintf('[%s]%c%s', $prefix, 10, $value);

    }
}
