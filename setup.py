import os

from setuptools import find_packages, setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from pip.req import parse_requirements


__dir__ = os.path.dirname(os.path.realpath(__file__))

requirements = [
    'gensim>=0.10.1',
    'nltk>=2.0.3'
]

test_requirements = [
    'nose>=1.3.3',
    'pytest-bdd>=2.3.1',
    'pytest>=2.6',
    'lettuce'
]

print requirements

def _post_install():
    # nltk may have just been installed, if so we cannot import it
    #  unless we first update our path by reloading the site package
    # thanks stack overflow: https://stackoverflow.com/questions/25384922/how-to-refresh-sys-path
    import site
    reload(site)
    # We can now safely import nltk, even if it was just installed
    import nltk
    nltk.download('punkt')


class my_install(install):
    def run(self):
        install.run(self)
        self.execute(_post_install, [],
                     msg="Running post install task")


class my_develop(develop):
    def run(self):
        develop.run(self)
        self.execute(_post_install, [],
                     msg="Running post develop task")

short_description='Phrase: generates phrases given a corpus'
long_description=short_description
with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='phrase',
    version='0.0.10',
    description=short_description,
    long_description=long_description,
    author='Brent Payne',
    author_email='brent.payne@gmail.com',
    url='http://www.github.com/brentpayne/phrase',
    install_requires=requirements,
    cmdclass={'install': my_install, 'develop': my_develop},
    entry_points="""
            [console_scripts]
            create_phrase_dictionary = phrase.create_phrase_dictionary_from_folder:main
        """,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    keywords=['phrase', 'noun phrase', 'verb phrase', 'nlp',
              'natural language processing', 'language', 'language processing',
              'phrases', 'nltk'
    ],
    classifiers=[
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Lesser General Public License v3" +
         " (LGPLv3)")
    ]
)
