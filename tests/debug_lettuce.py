__author__ = 'brentpayne'

__requires__ = 'lettuce==0.2.19'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('lettuce==0.2.19', 'console_scripts', 'lettuce')()
    )