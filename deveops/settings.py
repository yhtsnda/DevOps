# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 09 13:49
# Author Yo
# Email YoLoveLife@outlook.com
"""
Django settings for devEops project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from __future__ import absolute_import
import os
import sys
import django.db.backends.mysql
from deveops import conf as DEVEOPS_CONF
ENVIRONMENT=DEVEOPS_CONF.ENVIRONMENT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1x$!#dwp2_6^tdgs1nv8pwgutbc#4m%#qaz!m!0h_f*%6fp+vt'

#ASGI
ASGI_APPLICATION = 'deveops.routing.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'utils.apps.UtilsConfig',
    'authority.apps.AuthorityConfig',
    # 'softlib.apps.SoftlibConfig',
    'manager.apps.ManagerConfig',
    'ops.apps.OpsConfig',
    'work.apps.WorkConfig',
    # 'application.apps.ApplicationConfig',
    # 'execute.apps.ExecuteConfig',
    # 'timeline.apps.TimelineConfig',
    # 'upload.apps.UploadConfig',
    'variable.apps.VariableConfig',
    'dashboard.apps.DashboardConfig',
    'dns.apps.DnsConfig',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    # 'bootstrap3',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    # 'djcelery', #celery
    # 'kombu.transport.django', #celery
    'channels',
]

#JWF
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_SECRET_KEY': SECRET_KEY,
}


REST_FRAMEWORK = {
    # 'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'deveops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'deveops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':DEVEOPS_CONF.DB_NAME,
        'USER':DEVEOPS_CONF.DB_USER,
        'PASSWORD':DEVEOPS_CONF.DB_PASSWD,
        'HOST':DEVEOPS_CONF.DB_HOST,
        'PORT':DEVEOPS_CONF.DB_PORT,
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

# FILE_CHARSET='gb18030'
#
DEFAULT_CHARSET='utf-8'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I18N translation
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = PROJECT_DIR + DEVEOPS_CONF.MEDIA_ROOT
MEDIA_URL = '/media/'

#Ops dir
OPS_ROOT = PROJECT_DIR + DEVEOPS_CONF.OPS_ROOT

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "DevOps/static"),
    os.path.join(PROJECT_DIR, "DevOps/media"),
    os.path.join(PROJECT_DIR, "workpsace"),
)

#LOGIN
LOGIN_URL='/validate/login'
AUTH_USER_MODEL='authority.ExtendUser'

#SESSION
SESSION_SAVE_EVERY_REQUEST=True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE=DEVEOPS_CONF.SESSION_COOKIE_AGE

#SSH
SSH_TIMEOUT=DEVEOPS_CONF.SSH_TIMEOUT

# LDAP
if ENVIRONMENT != 'TRAVIS':
    from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
    import ldap
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    AUTH_LDAP_SERVER_URI = DEVEOPS_CONF.LDAP_SERVER
    AUTH_LDAP_BIND_DN = "cn=tools,ou=Zabbix,ou=TEST,dc=zbjt,dc=com"
    AUTH_LDAP_BIND_PASSWORD = DEVEOPS_CONF.LDAP_PASSWD

    OU = DEVEOPS_CONF.LDAP_OU
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(objectClass=groupOfNames)")
    AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
    AUTH_LDAP_USER_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(&(objectClass=*)(sAMAccountName=%(user)s))")
    AUTH_LDAP_USER_ATTR_MAP = {
        "full_name": "cn",
        "description": "description",
        "first_name":"sn",
        "phone":"mobile",
    }
    AUTH_LDAP_ALWAYS_UPDATE_USER = True
    # AUTH_LDAP_MIRROR_GROUPS = True
else:
    pass


#CHANNEL
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(
                "redis://:{PASSWORD}@{HOST}:{PORT}/{SPACE}".format(
                    PASSWORD=DEVEOPS_CONF.REDIS_PASSWD,
                    HOST=DEVEOPS_CONF.REDIS_HOST,
                    PORT=DEVEOPS_CONF.REDIS_PORT,
                    SPACE=DEVEOPS_CONF.REDIS_SPACE)
            )],
        },
        # "ROUTING": "deveops.routing.routing",
    },
}


# CELERY
# import djcelery
# djcelery.setup_loader()
CELERY_BROKER_URL = 'redis://:{PASSWORD}@{HOST}:{PORT}/{SPACE}'.format(
    PASSWORD=DEVEOPS_CONF.REDIS_PASSWD,
    HOST=DEVEOPS_CONF.REDIS_HOST,
    PORT=DEVEOPS_CONF.REDIS_PORT,
    SPACE=DEVEOPS_CONF.REDIS_SPACE,
)
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERY_RESULT_EXPIRES = 3600
# CELERY_WORKER_LOG_FORMAT = '%(asctime)s [%(module)s %(levelname)s] %(message)s'
CELERY_WORKER_LOG_FORMAT = '%(message)s'
# CELERY_WORKER_TASK_LOG_FORMAT = '%(asctime)s [%(module)s %(levelname)s] %(message)s'
CELERY_WORKER_TASK_LOG_FORMAT = '%(message)s'
# CELERY_WORKER_LOG_FORMAT = '%(asctime)s [%(module)s %(levelname)s] %(message)s'
CELERY_TASK_EAGER_PROPAGATES = True
CELERY_REDIRECT_STDOUTS = True
CELERY_REDIRECT_STDOUTS_LEVEL = "INFO"
CELERY_WORKER_HIJACK_ROOT_LOGGER = False



#FileUpload
# FILE_UPLOAD_HANDLERS=(
#     "django.core.files.uploadhandler.MemoryFileUploadHandler",
#     "django.core.files.uploadhandler.TemporaryFileUploadHandler"
# )
# import django.core.files.uploadhandler


#DJANGO LOG
# if DEBUG == True:
#     LOGGING_LEVEL = 'DEBUG'
# else:
#     LOGGING_LEVEL = 'WARNING'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#        'standard': {
#            # 'format': '%(levelname)s-%(asctime)s-'
#            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'  #日志格式
#        }
#     },
#     'filters': {
#     },
#     'handlers': {
#         'default': {
#             'level':LOGGING_LEVEL,
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/django.log',     #日志输出文件
#             'maxBytes': 1024*1024*5,                  #文件大小
#             'backupCount': 5,                         #备份份数
#             'formatter':'standard',                   #使用哪种formatters日志格式
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default'],
#             'level': LOGGING_LEVEL,
#             'propagate': False
#         }
#     }
# }
#
# #PERSON LOG
# import logging
# import logging.config
# # logging.basicConfig(level=logging.DEBUG,
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# #                     datefmt='%a, %d %b %Y %H:%M:%S',
# #                     filename='logs/myapp.log',
# #                     filemode='w')
#
# logging.config.fileConfig('logging.ini')
# logger = logging.getLogger("deveops.api")
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')