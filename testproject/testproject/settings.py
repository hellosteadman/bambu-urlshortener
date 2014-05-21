DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

SECRET_KEY = 'sm8apo4(o4ni9n=nsn7-3x8g@fkeuckm(#ixpk5lw3vrzq*ads'

INSTALLED_APPS = (
    'south',
    'bambu_urlshortener',
)