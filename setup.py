#!/usr/bin/env python
from setuptools import setup, find_packages
import keyvaluestore


setup(
    name="django-keyvaluestore",
    version=keyvaluestore.__version__,
    url='https://github.com/vikingco/django-keyvaluestore',
    license='BSD',
    description="A Key-Value store for Django",
    long_description=open('README.rst', 'r').read(),
    author='Unleashed NV',
    author_email='operations@unleashed.be',
    packages=find_packages('.'),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
