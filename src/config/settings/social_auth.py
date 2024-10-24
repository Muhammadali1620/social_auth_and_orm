import os

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.environ['CLIENT_ID'],
            'secret': os.environ['SECRET'],
        }
    }
}

SOCIALACCOUNT_LOGIN_ON_GET = True