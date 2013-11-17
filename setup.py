import sys
from setuptools import setup, find_packages
from distutils.core import Command

class DisabledCommands(Command):
    user_options = []

    def initialize_options(self):
        raise Exception('This command is disabled')

    def finalize_options(self):
        raise Exception('This command is disabled')

osx_requirements = [
]

other_requirements = [
]

requirements = [
    'nltk'
]

if sys.platform == 'darwin':
    requirements.extend(osx_requirements)
else:
    requirements.extend(other_requirements)

setup(name='phrase',
        version='0.0.1',
        description='A long long time ago in a land far far away...',
        author='Brent Payne',
        author_email='brent.payne@gmail.com',
        license='All Rights Reserved',
        install_requires=requirements,
        packages=find_packages('.'),
        package_dir = {'': '.'},
        cmdclass = {'register': DisabledCommands,
                    'upload': DisabledCommands}
        )
