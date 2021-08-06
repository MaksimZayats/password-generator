from setuptools import setup

setup(
    name='p-gen',
    version='0.0.1',
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
