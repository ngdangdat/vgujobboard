<?php
defined('BASEPATH') OR exit('No direct script access allowed');

function timeCmp($a, $b) {
    if($a['weekday'] == $b['weekday']){

        $timeStrA = strtotime($a['time']);
        $timeStrB = strtotime($b['time']);
        if($timeStrA == $timeStrB){
            return 0;
        }

        return ($timeStrA < $timeStrB) ? -1 : 1;
    }

    return ($a['weekday'] < $b['weekday']) ? -1 : 1;
}

function getScheduledTimeString() {
    $timeMapping = array(
        'SUN' => 0,
        'MON' => 1,
        'TUE' => 2,
        'WED' => 3,
        'THU' => 4,
        'FRI' => 5,
        'SAT' => 6
    );


    $scheduleTime = ['TUE|12:00', 'WED|12:00'];
    $parsedTimeArr = array();
    foreach ($scheduleTime as $key => $val) {
        $parsedTime = explode("|", $val);
        $weekday = $timeMapping[$parsedTime[0]];
        $time = $parsedTime[1];
        array_push($parsedTimeArr, array(
            'weekday'   => $weekday,
            'time'      => $time
        ));
    }

    uasort($parsedTimeArr, 'timeCmp');

    $currTime = new DateTime();
    $currTime->setTimezone(new DateTimeZone('Asia/Ho_Chi_Minh'));
    $currTimeStamp = $currTime->getTimestamp();
    $currWeekDay = date('w', $currTimeStamp);

    $currentWeekDay = date('w', $currTimeStamp);
    $scheduledTime = NULL;
    for ($i=0; $i < count($parsedTimeArr); $i++) {
        if($currentWeekDay <= $parsedTimeArr[$i]['weekday']){
            if($currentWeekDay == $parsedTimeArr[$i]['weekday']){
                $deltaTimeStr = strtotime($parsedTimeArr[$i]['time'], $currTimeStamp) - $currTimeStamp;
                if($deltaTimeStr > 300){
                    $scheduledTime = $currTime;
                    $scheduledTime->setTimestamp(strtotime($parsedTimeArr[$i]['time'], $currTimeStamp));
                    break;
                }
            }else{
                $scheduledTime = $currTime;
                $scheduledTime->setTimestamp(strtotime($parsedTimeArr[$i]['time'], $currTimeStamp));
                $deltaDay = $parsedTimeArr[$i]['weekday'] - $currWeekDay;
                $scheduledTime->add(new DateInterval('P'.(string) $deltaDay . 'D'));
                break;
            }
        }
    }
    if(empty($scheduledTime)){
        $scheduledTime = $currTime;
        $scheduledTime->setTimestamp(strtotime($parsedTimeArr[0]['time'], $currTimeStamp));
        $deltaDay = 7 - ($currWeekDay - $parsedTimeArr[0]['weekday']);
        $scheduledTime->add(new DateInterval('P'.(string) $deltaDay . 'D'));
    }

    $expectedTimestring = $scheduledTime->getTimestamp();
    return $expectedTimestring;
}

class Handle extends CI_Controller {
    public function job() {
        $this->load->library('Form_validation');
        $this->load->library('Job');
        $this->load->helper('facebook');
        $this->load->helper('form');
        $exportedVars = array();
        if($this->form_validation->run('job') === FALSE) {
            $exportedVars['template'] = 'homepage';
        }else{
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
                    'jobImage' => 'https://boardsource.org/wp-content/uploads/2016/05/Board-Member-Job-Description.png'
                )
            );
            $caption = $job->getCaption();
            $image = $job->getJobImage();
            $postResult = postImageToFacebook($image, $caption, false, getScheduledTimeString());
            $exportedVars['postUrl'] = $postUrl;
            $exportedVars['template'] = 'jobpostsuccess';
        }
        $this->load->view('container/pt_homepage', $exportedVars);
    }
}
