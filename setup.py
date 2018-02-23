# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ahoy',
    version='0.0.1',
    description='Toy Project for Python Study',
    long_description=readme,
    author='GeekSaga',
    author_email='geeksaga@geeksaga.com',
    url='https://github.com/',
    license=license,
    packages=find_packages(exclude=('tests', 'data')),
    include_package_data=True,
    install_requires=[
        'flask',
        'SQLAlchemy',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
