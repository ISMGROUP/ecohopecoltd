from pathlib import Path
import os

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9ha&__jcf^(f6x=bvkv5=1lifh4x^##x4$)j4ij=z8@@b&&(va'

# Debug settings
DEBUG = True
ALLOWED_HOSTS = ['ecohopecoltd.onrender.com']

# Installed apps
INSTALLED_APPS = [
    'jazzmin',
     'ecohope',
     'taggit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_URL = 'http://127.0.0.1:8000'  # or your real domain


# URLs and WSGI
ROOT_URLCONF = 'eco.urls'
WSGI_APPLICATION = 'eco.wsgi.application'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static Files Configuration
STATIC_URL = '/static/'

# Include app static folders (like ecohope/static/ecohope/css/styles.css)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ecohope', 'static')
]

# Collect static files here when you run collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ecohopeuganda@gmail.com'
EMAIL_HOST_PASSWORD = 'rdfr whag xhvc yiqc'  # Gmail app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

JAZZMIN_SETTINGS = {
    'site_title': 'EcoHope Admin',
    'site_header': 'EcoHope Administration',
    'site_brand': 'EcoHope',
    'site_icon': 'images/logo.png',
    'user_avatar': 'images/sanga.jpg',
    'custom_css': 'css/admin-custom.css',

    'welcome_sign': 'Welcome to EcoHope Admin',
    'search_model': 'auth.User',
    'navigation_expanded': True,

    # Custom footer text
    'copyright': '© 2025 EcoHope Co. Ltd. All rights reserved.',

    # Remove the "Powered by Jazzmin"
    'show_ui_builder': False,

    'sidebar_links': [
        {
            'name': 'Job Postings',
            'url': 'admin:ecohope_jobposting_changelist',
            'icon': 'fa fa-briefcase',
        },
        {
            'name': 'Services',
            'url': 'admin:ecohope_service_changelist',
            'icon': 'fa fa-cogs',
        },
    ],
}
