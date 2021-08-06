import os

from setuptools import setup


VERSION = "0.0.4"


def readme():
    """ Load the contents of the README file """
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "r") as f:
        return f.read()


setup(
    name='p-gen',
    description="A console utility that allows you to generate passwords based on code phrases and a secret key (seed).",
    long_description=readme(),
    long_description_content_type='text/markdown',
    version=VERSION,
    packages=['password_generator'],
    url='https://github.com/MaximZayats/password-generator',
    author='Maxim',
    author_email='maximzayats1@gmail.com',
    entry_points={
        'console_scripts': [
            'pgen = password_generator.generator:main',
            'p-gen = password_generator.generator:main',
            'pass-gen = password_generator.generator:main'
        ]
    }
)
