<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

if(!function_exists('getStaticPath'))
{
    /**
     * Get absolute static path for given path
     */
    function getStaticPath($path) {

        return (get_instance()->config->site_url(get_instance()->config->static_path() . '/' . $path));
    }
}

if(!function_exists('getContentPath'))
{
    /**
     * Get absolute path for content
     */
    function getContentPath($path){
        return (get_instance()->config->site_url(get_instance()->config->content_path() . '/' . $path));
    }
}