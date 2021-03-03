import os
import environ

environ.Env.read_env('environment.env')

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'production':
	from .production import *
elif ENVIRONMENT == 'staging':
	from .staging import *
elif ENVIRONMENT == 'test':
	from .test import *
else:
	from .dev import *
