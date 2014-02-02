import sys
from setuptools import setup, find_packages
from distutils.core import Command

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
        version='00.00.02',
        description='A long long time ago in a land far far away...',
        author='Brent Payne',
        author_email='brent.payne@gmail.com',
        license='All Rights Reserved',
        install_requires=requirements,
        packages=find_packages('.'),
        package_dir = {'': '.'},
        entry_points="""
            [console_scripts]
            create_phrase_dictionary = phrase.create_phrase_dictionary_from_folder:main
            create_word2vec_model = phrase.create_word2vec_model:main
        """
)
