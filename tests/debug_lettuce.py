__author__ = 'brentpayne'

__requires__ = 'lettuce'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('lettuce', 'console_scripts', 'lettuce')()
    )