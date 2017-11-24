<?php

defined('BASEPATH') OR exit('No direct script access allowed');

require_once __DIR__ . '/Facebook/autoload.php';

class Facebook {
    protected $CI_Instance;

    protected $appId;
    protected $appSecret;
    protected $apiVersion;
    protected $accessToken;
    protected $apiRequest;
    protected $apiResponse;
    protected $FacebookApp;

    public function __construct()
    {
        $this->CI_Instance =& get_instance();
        $this->initialize();
    }

    private function initialize() {
        $config = $this->getApiConfig();
        $this->appId = $config['app_id'];
        $this->appSecret = $config['app_secret'];
        $this->apiVersion = $config['api_version'];
        $this->accessToken = $config['access_token'];
        $this->FacebookApp = new \Facebook\Facebook([
            'app_id' => $this->appId,
            'app_secret' => $this->appSecret,
            'default_graph_version' => 'v2.10',
            'default_access_token' => $this->accessToken
        ]);
    }

    private function getApiConfig() {
        return array(
            'app_id'        => '686552844887170',
            'app_secret'    => 'bfbaed420f1ec6142820c3bafd44fc41',
            'api_version'   => 'v2.10',
            'access_token'  => 'EAAJwaopwZAIIBANvVxssVAmnKi2f2Tb1Ddlcp95xQxvgGftVZBkm1xf4iwpC8R6H6hSTJDmDNENVFcU3O48oU1KfbbkzpK1Tub3LtdMdPLRZAV6F6S85RjkLDCy3l9hJi79aXamNKf2So4C5xiTSYhmaw808fbb64cbm6id4wZDZD',
        );
    }

    public function get($endpoint) {
        return $this->FacebookApp->get($endpoint)->getDecodedBody();;
    }

    public function post($endpoint, $params) {
        return $this->FacebookApp->post($endpoint, $params)->getDecodedBody();;
    }
}