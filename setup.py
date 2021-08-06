from setuptools import setup

setup(
    name='p-gen',
    version='',
    packages=['password_generator'],
    url='',
    license='',
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
