# VGU Job Boards

## Set up front-end environment

To set up environment, make sure you have npm. You can download npm here: https://www.npmjs.com/

Next, install gulp and gulp dependencies by running following commands in command line:


```
npm install gulp -g
npm install

```


## Build commands

After setting up environment, you can start write SCSS in *sass* folder.

Build and watch commands:

```
gulp build
gulp watch
```

Add *--sourcemaps* as parameter of commands above to generate SCSS and CSS map.

## Set up back-end environment

We use CodeIgnigter as our framework to handle back-end logic. Prerequisites:

* PHP
* MySQL
* Apache HTTP server

Follow instructions in DigitalOcean to install a LAMP stack (including PHP, MySQL and Apache) on Ubuntu 16.04: https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04

After finishing LAMP installation, configure the *base_url* in *config.php* located at *application/config* to help CI know the main site URL on your machine. For example, the source locates at /var/www/html/intern/, the *base_url* should be *localhost/intern*.

Feel free to ask me any question at ngdangdat09 [at] gmail.com.