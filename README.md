# VGU Job Boards

# Set up front-end environment

To set up environment, make sure you have npm. You can download npm here: https://www.npmjs.com/

Next, install gulp and gulp dependencies by running following commands in command line:

```
$ npm install gulp -g
$ npm install
```

## Build commands

After setting up environment, you can start write SCSS in *sass* folder.

Build command:

```
$ gulp build
```

Add *--sourcemaps* as parameter of commands above to generate SCSS and CSS map.

# Set up back-end environment

We use Django as our framework to handle back-end logic. Prerequisites:

* Python
* Gunicorn
* PostgreSQL

Setup virtual env

```
$ [sudo] pip install virtualenv
```

Create VE with python3

```
$ virtualenv -p python3 env
```

Use created virtual environment

```
$ source env/bin/activate
```

## Clone source and configure
- Clone this repository.
- Create a database for project.
- Copy `core/settings/local.env.sample` to `core.settings.local.env`.
- Replace `DATABASE_URL` key with your local database credentials. You can use Postgres, MySQL,...

**Notes:** For mysql MSDB, please make sure your database chartset is support utf8. `CREATE DATABASE vgualumni CHARACTER SET utf8 COLLATE utf8_general_ci;`

## Facebook configuration
Get Facebook access token for your fan page to configure the key `FACEBOOK_ACCESS_TOKEN`.
Configure `FACEBOOK_ALBUM_ID` key with ID of the photo album that you want photos being posted to.

## Run at localhost
Install all necessary packages

```
$ pip install -r requirements.txt
```

Apply migrations

```
$ python manage.py migrate
```

Run server

```
$ python src/manager.py runserver 8002
```


### References
- [How to get Facebook access token?](https://stackoverflow.com/questions/42663080/how-can-you-get-facebook-access-token)
- [How to get Facebook album ID?](https://stackoverflow.com/questions/18549744/how-do-i-get-facebook-album-id-from-url?rq=1)


Feel free to ask me any question at ngdangdat09 [at] gmail.com.
