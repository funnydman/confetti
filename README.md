# CONFETTI
> The way to start a Django project with Docker

<p align="center"> <img src="https://preview.ibb.co/eDU9Zd/conf.png"></p>

## Technology Stack

* Docker v20.x
* Docker-compose v1.28
* Django v3.x

## Getting Started

### Development

1. Clone this git repository to your local machine. 

2. Install ```docker``` and ```docker-compose``` using official documentation.

3. Add user to the docker group to run commands without sudo: 
```
sudo usermod -aG docker $USER
```
4. Update settings in `dev.env` and `confetti/settings/prod.py`(recommended).

5. Go to the project root and run:
```
docker-compose up
``` 

6. Create Django superuser in the container(in the second shell):
```
docker-compose exec web python manage.py createsuperuser 
```

7. Run tests(optional):
```
docker-compose exec web python manage.py test 
```

8. Navigate to `http://localhost:8000/`.

# Production 

1. Create and fill `.env` and `confetti/settings/prod.py`.

2. Run application: 
 ```
docker-compose -f docker-compose.prod.yml up
```
3. Generate certificates(see next section).

4. Navigate to `https://localhost/`.

## Tips
How to generate ssl certificates? [Follow this guide.](https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)

The simplest way with less headaches:
1. ssh to the server and go to the project root, assume that you configured domains properly: 
```
docker-compose -f docker-compose.prod.yml exec nginx sh
```
2. Install certbot:
```
apk update && apk add certbot certbot-nginx
```
3. Generate certificates, we use volumes so we don't need to copy certs manually,
 don't forget to commit them or even better exclude them from git tracking: 
```
certbot certonly --nginx # follow instructions
```

4. Update data in `deployment/nginx/app.conf`, and then:
```
docker-compose -f docker-compose.prod.yml up --build
```

Ad Hoc docker/docker-compose commands (put in .bash_aliases):
```
alias dcubn=docker-compose build --no-cache
alias dcub=docker-compose up --build
alias dcu=docker-compose up
```

Happy coding :blush:
