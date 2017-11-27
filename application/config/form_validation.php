<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$config = array(
	'job' => array(
		array(
			'field' => 'job_category',
			'label' => 'Job Field',
			'rules' => 'required'
		),
		array(
			'field' => 'job_title',
			'label' => 'Job Title',
			'rules' => 'required',
			'errors' => array(
				'required' => '%s is required.',
			)
		),
		array(
			'field' => 'company',
			'label' => 'Company Name',
			'rules' => 'required',
		),
		array(
			'field' => 'job_require',
			'label' => 'Job Requirement',
			'rules' => 'required',
		),
		array(
			'field' => 'job_contact_submit',
			'label' => 'Contact to CV Submission',
			'rules' => 'required',
		),
		array(
			'field' => 'deadline',
			'label' => 'Deadline',
			'rules' => 'required',
		)
	)
);