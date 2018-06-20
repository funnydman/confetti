try:
    from .base import *
except ImportError:
    raise ImportError(
        "Can't find the file with basic settings. Did you import?")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'teleadmin'),
        'USER': os.environ.get('POSTGRES_USER', 'teleadmin'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'teleadmin'),
        'HOST': os.environ.get('POSTGRES_HOST_NAME', 'teleadmin'),
        'PORT': '',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']

# Just for local development/testing, this key doesn't used in production!
SECRET_KEY = '^pde$1h8cem*ao%n)p=$ep5dv8#)xl#w)))7^l3^%a0q!!_b)a'
