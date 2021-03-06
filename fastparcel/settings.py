import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mzlkisl5#lfe4isx%&y6hx3uu#r=n)jdd7zq4rq(ko68ny!281'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',
    'social_django',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ProfileMiddleware',
]

ROOT_URLCONF = 'fastparcel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'fastparcel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/sign-in/'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
  'social_core.backends.facebook.FacebookOAuth2',
  'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = "194292166204226"
SOCIAL_AUTH_FACEBOOK_SECRET = "b488514eeb7437e1550da91abeb8f4e1"
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jura.shchur0605@gmail.com'
EMAIL_HOST_PASSWORD = 'CEZAR_159753'
DEFAULT_FROM_EMAIL = 'FastParcel <no-reply@fastparcel.localhost>'

FIREBASE_ADMIN_CREDENTIAL = os.path.join(BASE_DIR, "firebase-private-key.json")

STRIPE_API_PUBLIC_KEY = "pk_test_51Jw8y9LjLov63KmGnDpC9d80WyuKKwNpNHD6WVit8WtbswHra9OaDidimXDg47nhO273H0UDAS3FoQOcVrNyOuC7007HPkUPLy"
STRIPE_API_SECRET_KEY = "sk_test_51Jw8y9LjLov63KmGgD5Ly9MGHBFxt5a6f6H0P3UeyHU2YP0Da0b1hAVDklGiHinDHuddrj0aORvCxhHLlzEMwIkc00wwPmwuqy"

GOOGLE_MAP_API_KEY = "AIzaSyC-zzFWPQZUbwJC7qcBlLTPRvVVfOQTw4g"