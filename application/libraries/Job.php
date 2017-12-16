<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Job {
    const DEFAULT_IMAGE_URL = 'https://boardsource.org/wp-content/uploads/2016/05/Board-Member-Job-Description.png';

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
        $this->CI->lang->load('forms', 'english');

        

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
        $fields = array(
            $this->getFieldWithPrefix($this->CI->lang->line('label.job.field'), $this->jobCategory),
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
            return static::DEFAULT_IMAGE_URL;
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
