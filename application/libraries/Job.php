<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Job {
    const PREFIXES = [
        'jobCategory' => 'Internship',
        'jobTitle' => 'Job Title',
        'jobDescription' => 'Job Description',
        'jobRequirement' => 'Job Requirements',
        'company' => 'Company',
        'salary' => 'Salary',
        'benefit' => 'Benefit',
        'contactPointSubmission' => 'Contact To CV Submission',
        'contactPointContributor' => 'Contact To Contributor',
        'jobDeadline' => 'Deadline'
    ];
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

    public function __construct(array $fields = []) {
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

    public function getCaption() {
        $fields = array(
            $this->getFieldWithPrefix(static::PREFIXES['jobCategory'], $this->jobCategory),
            $this->getFieldWithPrefix(static::PREFIXES['jobTitle'], $this->jobTitle),
            $this->getFieldWithPrefix(static::PREFIXES['jobDescription'], $this->jobDescription),
            $this->getFieldWithPrefix(static::PREFIXES['jobRequirement'], $this->jobRequirement),
            $this->getFieldWithPrefix(static::PREFIXES['company'], $this->company),
            $this->getFieldWithPrefix(static::PREFIXES['salary'], $this->salary),
            $this->getFieldWithPrefix(static::PREFIXES['benefit'], $this->benefit),
            $this->getFieldWithPrefix(static::PREFIXES['contactPointSubmission'], $this->contactPointSubmission),
            $this->getFieldWithPrefix(static::PREFIXES['contactPointContributor'], $this->contactPointContributor),
            $this->getFieldWithPrefix(static::PREFIXES['jobDeadline'], $this->jobDeadline)
        );

        return join(chr(10).chr(10), $fields);
    }

    public function getJobImage() {
        if(!$this->jobImage) {
            return static::DEFAULT_IMAGE_URL;
        }

        return $this->jobImage;
    }

    private function getFieldWithPrefix($prefix, $value){
        if(!$value){
            return '';
        }

        if(!$prefix){
            return $value;
        }

        return sprintf('[%s]%c%s', $prefix, 10, $value);

    }
}
