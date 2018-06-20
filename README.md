# CONFETTI
The way to start a django project with docker

<p align="center"> <img src="https://preview.ibb.co/eDU9Zd/conf.png"></p>

## Technology Stack

* Docker v17.04
* Docker-compose v1.21
* Django v2.0

## Getting Started

1. First of all clone this git repository to your local machine. 

2. Install ```docker``` and ```docker-compose``` using official documentation.

3. Add user to the docker group to run commands without sudo

``` 
sudo usermod -aG docker $USER
```

4. Go to the project directory and run

```
docker-compose up
``` 

5. Create django superuser in the container

```
docker exec -it web bash
```

```
python manage.py createsuperuser
```
Happy coding :blush:
