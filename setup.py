#!/usr/bin/env python
from setuptools import setup, find_packages

METADATA = dict(
        name='django-appetizer',
        version='0.1',
        author='Luke Crouch',
        author_email='luke.crouch@gmail.com',
        description='Automatically creates Open Web Application manifests for django sites. https://apps.mozillalabs.com/',
        long_description=open('README.rst').read(),
        url='http://github.com/groovecoder/django-appetizer',
        keywords='django open web apps',
        install_requires=[],
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Environment :: Web Environment',
            'Topic :: Internet',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
        ],
        packages=find_packages(),
        package_data={'appetizer': ['templates/appetizer/*.json'],}
)

if __name__ == '__main__':
    setup(**METADATA)
