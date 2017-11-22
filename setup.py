"""Django Material Widgets Package Setup

"""
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-material-widgets',
    version='1.0.0b3',
    packages=find_packages('src', exclude=['demo', 'config',]),
    package_dir={'':'src'},
    include_package_data=True,
    license='Apache Software License',
    description=(
        'Django widgets styled with Material Components for the Web.'
        ),
    long_description=README,
    keywords='django material widgets forms modelforms',
    url='https://github.com/ooknosi/django_material_widgets',
    author='Edison KOO',
    #author_email='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
