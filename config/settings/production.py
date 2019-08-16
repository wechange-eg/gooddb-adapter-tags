import random
import string

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa


INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': env('DJANGO_RAVEN_DSN'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    #'release': raven.fetch_git_sha(os.path.dirname(__file__)),
    'string_max_length': 12000,
    'list_max_length': 1200,
}

# whether to show SQL generated (is referenced below when configuring logging)

DEBUG = False

try:
    SECRET_KEY = env("DJANGO_SECRET_KEY")
except ImproperlyConfigured:
    SECRET_KEY = ''.join(
        [random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, '+-:$;<=>?@^_~')) for i in
         range(63)])
    with open('.env', 'a') as envfile:
        envfile.write('DJANGO_SECRET_KEY={}\n'.format(SECRET_KEY))
