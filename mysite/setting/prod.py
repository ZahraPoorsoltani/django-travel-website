from mysite.settings import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b1m0%%ww9to92i*kb9#n$5f@$*zh5a(*gpa=0eqt64y)ny_+gk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost',
  '127.0.0.1',]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# STATICFILES_DIRS = [
#      BASE_DIR/"website/static",
# ]




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_PROD_NAME'),                      
#         'USER':  config('DB_PROD_USER'),
#         'PASSWORD': config('DB_PROD_PASSWORD'),
#         'HOST': '',
#         'PORT': config('DB_PROD_PORT',cast = int),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#sites framework
SITE_ID = 3

# CSRF_COOKIE_SECURE = True
