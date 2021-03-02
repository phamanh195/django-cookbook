from __future__ import absolute_import, unicode_literals
import os
import environ

environ.Env.read_env('environments.env')

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'dev':
	from m