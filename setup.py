
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

VERSION = '0.1'

setup(
    name = "nose-rage",
    version = VERSION,
    author = "WizzardX",
    author_email = "wizzardx@gmail.com",
    description = "Implements PEP712. Displays FFFFFFFUUUU for errors.",
    license = 'GNU LGPL',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General "
        "Public License (LGPL)"),
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        ],

    py_modules = ['nose_rage'],
    zip_safe = False,

    entry_points = {
        'nose.plugins': ['nose_rage = nose_rage:NoseRage']
        },
    install_requires = ['nose'],
)