import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-easy-currencies',
    version='0.1',
    packages=['currencies'],
    include_package_data=True,
    license='BSD License',    
    description='Currency, exchange rate and conversions support for django projects',
    long_description=README,
    url='https://github.com/bashu/django-easy-currencies',
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
        'django-classy-tags',
        'openexchangerates',
    ],      
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',          
    ],
)
