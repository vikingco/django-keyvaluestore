#!/usr/bin/env python
from setuptools import setup, find_packages
import keyvaluestore

setup(
    name="django-keyvaluestore",
    version=keyvaluestore.__version__,
    url='https://github.com/citylive/django-keyvaluestore',
    license='BSD',
    description="A Key-Value store for Django",
    long_description=open('README.rst', 'r').read(),
    author='Ingo Berben, City Live nv',
    packages=['keyvaluestore'],
    zip_safe=False, # Don't create egg files, Django cannot find templates in egg files.
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)