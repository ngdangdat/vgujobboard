<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

if(!function_exists('getStaticPath')) {
    /**
     * Get absolute static path for given path
     */
    function getStaticPath($path) {

        return (get_instance()->config->site_url(get_instance()->config->static_path() . '/' . $path));
    }
}