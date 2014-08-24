import os

from setuptools import find_packages, setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from pip.req import parse_requirements


__dir__ = os.path.dirname(os.path.realpath(__file__))

install_reqs = parse_requirements(__dir__ + "/requirements.txt")
requirements = [str(ir.req) for ir in install_reqs]

test_requirements = [
    'nose>=1.3.3',
    'pytest-bdd>=2.3.1',
    'pytest>=2.6',
    'lettuce'
]

print requirements

def _post_install():
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


setup(
    name='phrase',
    version='0.0.8',
    description='Phrase: generates phrases given a corpus',
    author='Brent Payne',
    author_email='brent.payne@gmail.com',
    url='http://www.github.com/brentpayne/phrase',
    install_requires=requirements,
    cmdclass={'install': my_install, 'develop': my_develop},
    entry_points="""
            [console_scripts]
            create_phrase_dictionary = phrase.create_phrase_dictionary_from_folder:main
        """,
    packages=[
        'phrase',
    ],
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
