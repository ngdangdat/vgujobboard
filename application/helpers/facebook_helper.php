<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

if(!function_exists(('postImageToFacebook'))) {
    /**
     * @param string Image URL
     * @param string Caption of the photo
     * @param string Album ID
     * @return string Post URL
     */
    function postImageToFacebook($imageUrl, $caption, $albumId) {
        if(empty($imageUrl) || empty($albumId)) return NULL;

        $CI_instance = get_instance();
        $CI_instance->load->library('Facebook');
        $postImageEndpoint = '/' . $albumId . '/photos';
        $caption = $caption ? $caption || '';

        try {
            $facebookServ = new Facebook();
            $postImageResp = $facebookServ->post(
                $endpoint,
                array(
                    'url' => $imageUrl,
                    'caption' => $caption
                )
            );
            if(array_key_exists('post_id', $postImageResp)) {
                $postId = $postImageResp['post_id'];
                $postUrl = getPostUrlFromId($postId);
                if(!empty($postUrl)) {
                    return $postUrl;
                }
            }
        }catch (Exception $e){
            return NULL;
        }
        
        return NULL;
    }
}

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
            $getPostResponse = $this->FacebookApp->get($getPostEndpoint);
            if(array_key_exists('permalink_url', $getPostResponse)) {
                return $getPostResponse['permalink_url'];
            }
        }catch(Exception $e){
            return NULL;
        }
        

        return NULL;
    }
}
