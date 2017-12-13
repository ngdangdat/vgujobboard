<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

if(!function_exists(('postImageToFacebook'))) {
    /**
     * @param string Image URL
     * @param string Caption of the photo
     * @param string Album ID
     * @return array
     */
    function postImageToFacebook($imageUrl, $caption, $isPublished = TRUE, $scheduledTime = FALSE) {
        $albumId = getFacebookPostAlbumId();
        $CI_instance = get_instance();
        $CI_instance->load->library('Facebook');
        $postImageEndpoint = '/' . $albumId . '/photos';
        $caption = $caption ? $caption : '';

        $param = array(
            'url' => $imageUrl,
            'caption' => $caption
        );

        if(!$isPublished && !empty($scheduledTime))
        {
            $param['published'] = FALSE;
            $param['scheduled_publish_time'] = $scheduledTime;
        }

        try {
            $facebookServ = new Facebook();
            $postImageResp = $facebookServ->post(
                $postImageEndpoint,
                $param
            );
            if(array_key_exists('post_id', $postImageResp)) {
                $postId = $postImageResp['post_id'];
                $postUrl = getPostUrlFromId($postId);
                if(!empty($postUrl)) {
                    return array(
                        'isSuccess' => TRUE,
                        'isScheduled' => FALSE,
                        'postUrl' => $postUrl
                    );
                }
            }elseif (array_key_exists('id', $postImageResp)) {
                return array(
                    'isSuccess' => TRUE,
                    'isScheduled' => TRUE
                );
            }else{
                return array(
                    'isSuccess' => FALSE
                );
            }
        }catch (Exception $e){
            return NULL;
        }
        
        return NULL;
    
}}

if(!function_exists('getPostUrlFromId')) {
    /**
     * @param string ID of the post
     * @return string Permanent URL of given post ID
     */
    function getPostUrlFromId($postId = '') {
        if(empty($postId)) return NULL;

        $CI_instance = get_instance();
        $CI_instance->load->library('Facebook');

        try {
            $facebookServ = new Facebook();
            $getPostEndpoint = $postId . '?fields=permalink_url';
            $getPostResponse = $facebookServ->get($getPostEndpoint);
            if(array_key_exists('permalink_url', $getPostResponse)) {
                return $getPostResponse['permalink_url'];
            }
        }catch(Exception $e){
            return NULL;
        }
        

        return NULL;
    }
}

if(!function_exists('getFacebookPostAlbumId')){
    /**
     * @return string
     */
    function getFacebookPostAlbumId(){
        return '672115002991670';
    }
}
