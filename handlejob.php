<?php
    require_once __DIR__ . '/Facebook/autoload.php';
    require __DIR__ . '/lib/Job.php';
    
    $configsInFile = file_get_contents('config.json');
    $configJson = json_decode($configsInFile, true);

    $fb = new \Facebook\Facebook([
        'app_id' => $configJson['app_id'],
        'app_secret' => $configJson['app_secret'],
        'default_graph_version' => 'v2.10',
        'default_access_token' => $configJson['access_token']
    ]);

    $jobImage = $_POST["job_image"];
    $jobCategory = $_POST["job_category"];
    $jobTitle = $_POST["job_title"];
    $jobDescription = $_POST["job_desc"];
    $jobRequirement = $_POST["job_requirement"];
    $company = $_POST["company"];
    $salary = $_POST["salary"];
    $benefit = $_POST["benefit"];
    $contactSubmit = $_POST["job_contact_submit"];
    $contactContributor = $_POST["job_contact_contributor"];
    $job = new Job([
        "jobCategory" => $jobCategory,
        "jobTitle" => $jobTitle,
        "jobDescription" => $jobDescription,
        "jobRequirement" => $jobRequirement,
        "company" => $company,
        "salary" => $salary,
        "benefit" => $benefit,
        "contactPointSubmission" => $contactSubmit,
        "contactPointContributor" => $contactContributor,
        "jobImage" => $jobImage
    ]);

    try {
        $response = $fb->post(
            '/672115002991670/photos',
            array(
                'url' => $job->getJobImage(),
                'caption' => $job->getCaption()
            )
        );
        $parsed_post_response = $response->getDecodedBody();
        if(array_key_exists('post_id', $parsed_post_response)) {
            $post_id = $parsed_post_response['post_id'];
            $endpoint = $post_id . '?fields=permalink_url';
            $get_post_response = $fb->get(
                $endpoint
            );
            $parsed_get_post_response = $get_post_response->getDecodedBody();

            echo '<a href="'.$parsed_get_post_response['permalink_url'].'" target="_blank">View Post</a>';
        }
    } catch(\Facebook\Exceptions\FacebookResponseException $e) {
        // When Graph returns an error
        echo 'Graph returned an error: ' . $e->getMessage();
        exit;
    } catch(\Facebook\Exceptions\FacebookSDKException $e) {
        // When validation fails or other local issues
        echo 'Facebook SDK returned an error: ' . $e->getMessage();
        exit;
    }
?>