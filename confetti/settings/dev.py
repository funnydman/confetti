try:
    from .base import *
except ImportError:
    raise ImportError(
        "Cannot find the file with basic settings. Did you import it?"
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST_NAME', 'localhost'),
        'PORT': int(os.environ.get('POSTGRES_PORT', 5432)),
    }
}

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']

# Just for local development/testing, this key doesn't used in production!
SECRET_KEY = '^pde$1h8cem*ao%n)p=$ep5dv8#)xl#w)))7^l3^%a0q!!_b)a'
