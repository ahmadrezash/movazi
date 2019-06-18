"""
Django settings for movazi project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# import debug_toolbar

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# Location and Language
#import locale
#locale.setlocale(locale.LC_ALL, "fa_IR")

LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

ROOT_URLCONF = 'movazi.urls'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, "static")),
)

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "movazi/static"),
    os.path.join(BASE_DIR, "movazi/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$r2in^f=j!7t%$$u08#50rz!qage05iqr4m0w1!orhawrljqew'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
COMPRESS_ENABLED = True

# CACHES = {
#    'default': {
#       'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#       'LOCATION': '/var/tmp/django_cache',
#    }
# }

ALLOWED_HOSTS = ['localhost','894573f8.ngrok.io','127.0.0.1','movazi1.liara.run','movazi2.liara.run','mowazi.ir']

JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [ # prefix address is 'admin/'
            'js/django_jalali.min.js',
            # or
            'jquery.ui.datepicker.jalali/scripts/jquery-1.10.2.min.js',
            'jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            'jquery.ui.datepicker.jalali/scripts/calendar.js',
            'jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            'jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            'js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}
# Application definition

INSTALLED_APPS = [
    # 'bootstrap4',
    'crispy_forms',
    'compressor',
    # 'debug_toolbar',
    'django_jalali',
    'jalali_date',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'panel',
    # 'django_comments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
#     'django.middleware.cache.UpdateCacheMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
]





def show_toolbar(request):
  return True
DEBUG_TOOLBAR_CONFIG = {
  "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'movazi/templates')],
        # 'DIRS':  [os.path.join(BASE_DIR, '')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'zinnia.context_processors.version',  # Optional
            ],
        },
    },
]

WSGI_APPLICATION = 'movazi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'media/db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/panel/'
LOGOUT_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# AUTH_USER_MODEL = 'blog.MyUser'
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/


USE_I18N = True

USE_L10N = True

USE_TZ = True




# VERSATILEIMAGEFIELD_SETTINGS = {
#     # The amount of time, in seconds, that references to created images
#     # should be stored in the cache. Defaults to `2592000` (30 days)
#     'cache_length': 2592000,
#     # The name of the cache you'd like `django-versatileimagefield` to use.
#     # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
#     # provided, the 'default' cache will be used instead.
#     'cache_name': 'versatileimagefield_cache',
#     # The save quality of modified JPEG images. More info here:
#     # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
#     # Defaults to 70
#     'jpeg_resize_quality': 70,
#     # The name of the top-level folder within storage classes to save all
#     # sized images. Defaults to '__sized__'
#     'sized_directory_name': '__sized__',
#     # The name of the directory to save all filtered images within.
#     # Defaults to '__filtered__':
#     'filtered_directory_name': '__filtered__',
#     # The name of the directory to save placeholder images within.
#     # Defaults to '__placeholder__':
#     'placeholder_directory_name': '__placeholder__',
#     # Whether or not to create new images on-the-fly. Set this to `False` for
#     # speedy performance but don't forget to 'pre-warm' to ensure they're
#     # created and available at the appropriate URL.
#     'create_images_on_demand': True,
#     # A dot-notated python path string to a function that processes sized
#     # image keys. Typically used to md5-ify the 'image key' portion of the
#     # filename, giving each a uniform length.
#     # `django-versatileimagefield` ships with two post processors:
#     # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
#     #    md5 hash of `image_key`.
#     # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
#     #    of the 32 character md5 hash of `image_key`.
#     # By default, image_keys are unprocessed. To write your own processor,
#     # just define a function (that can be imported from your project's
#     # python path) that takes a single argument, `image_key` and returns
#     # a string.
#     'image_key_post_processor': None,
#     # Whether to create progressive JPEGs. Read more about progressive JPEGs
#     # here: https://optimus.io/support/progressive-jpeg/
#     'progressive_jpeg': False
# }
