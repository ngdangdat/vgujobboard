# VGU Job Boards

# Set up front-end environment

To set up environment, make sure you have package manager. You can download [npm](https://www.npmjs.com/) or [Yarn](https://yarnpkg.com/en/).

NPM
```bash
$ npm install
```

Yarn
```bash
$ yarn install
```

## Run command

Start development server for front-end side

NPM
```bash
$ npm run start
```

Yarn
```bash
$ yarn start
```

# Set up back-end environment

We use Django as our framework to handle back-end logic. Prerequisites:

* Python
* PostgreSQL

Setup virtual environment

```bash
$ pip install virtualenv
```

Create virtual environment with python3

```bash
$ virtualenv -p python3 env
```

Activate created virtual environment

```bash
$ source env/bin/activate
```

## Create database

PostgreSQL database create command
```sql
CREATE DATABASE vgu;
```

## Install required packages

Install all necessary packages

```bash
$ pip install -r requirements.txt
```

## Configure environment for Django

Copy `core/settings/local.env.sample` to `core/settings/local.env`. Configure `local.env` with your local machine variables (eg: database,...).

## Apply migrations

```bash
$ python manage.py migrate
```

## Facebook configuration
Get Facebook access token for your fan page to configure the key `FACEBOOK_ACCESS_TOKEN`.
Configure `FACEBOOK_ALBUM_ID` key with ID of the photo album that you want photos being posted to.

## Run the development server

Run development server
```bash
$ python src/manager.py runserver 8000
```

### References
- [How to get Facebook access token?](https://stackoverflow.com/questions/42663080/how-can-you-get-facebook-access-token)
- [How to get Facebook album ID?](https://stackoverflow.com/questions/18549744/how-do-i-get-facebook-album-id-from-url?rq=1)


Feel free to ask me any question at ngdangdat09 [at] gmail.com.
