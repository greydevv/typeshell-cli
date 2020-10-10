from setuptools import setup

setup(
    name = 'typeshell-cli',
    version = '0.1.0',
    packages = ['typeshell'],
    entry_points = {
        'console_scripts': [
            'typeshell = typeshell.__main__:main'
        ]
    })