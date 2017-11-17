<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Home extends CI_Controller {
    public function index()
    {
        $this->load->helper('form');
        $var = array();
        $vars['template'] = 'homepage';
        $this->load->view('container/pt_homepage', $vars);
    }
}
