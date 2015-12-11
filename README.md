# sitrep-api
This is the API that is used for sitrep


## Getting Started
The app is run using **gunicorn** and the server.py script. The default
port it is run on is 8000. You can change the port by passing in the
environment variable `PORT`

### Installing
```sh
vagrant up
vagrant ssh
cd /repo
make install
```

### Starting server
```sh
make serve-start
```

### Hitting the API
```sh
curl 192.168.93.10:8000
```

### Stoping the server
```sh
make serve-stop
```

## Debugging
You can run the app in debug mode by directly running the `server.py`. This is
ran on port 5000

```sh
APPLICATION_ENV=developement python server.py
```

## Going production
This app will work on **Heroku** using the `heroku/python` buildpack
