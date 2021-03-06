from django.core.management import setup_environ
import optparse
import sys
import settings

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

setup_environ(settings)

from django.contrib.auth.models import User


def main():
    p = optparse.OptionParser()
    p.set_usage("""Usage: %prog [options]""")
    p.add_option('--username', '-u', dest='username',
                 help="""Username for the superuser.""")
    p.add_option('--password', '-p', dest='password',
                 help="""Password for the superuser.""")

    options, arguments = p.parse_args()

    if (username_present(options.username)):
        sys.exit(0)
    else:
        sys.exit(1)


def username_present(username):
    if User.objects.filter(username=username).count():
        return True

    return False


if __name__ == '__main__':
    main()
