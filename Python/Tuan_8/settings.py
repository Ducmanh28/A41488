ALLOWED_HOST = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app2',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'hotel_booking_app',
        'USER': 'admin',
        'PASSWORD': '28072003',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}