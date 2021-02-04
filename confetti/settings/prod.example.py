try:
    from .base import *
except ImportError:
    raise ImportError(
        "Can't find the file with basic settings. Did you import?"
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST_NAME'],
        'PORT': int(os.environ['POSTGRES_PORT']),
    }
}

DEBUG = False

ALLOWED_HOSTS = ['your_host']

# Just for local development/testing, this key doesn't used in production!
SECRET_KEY = 'very_strong_key!'
