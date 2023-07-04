# -*- coding: utf-8 -*-
# Setup script to build gzip plugin. To build the plugin
# just run 'python setup.py' and an egg will be built and put into 
# the plugin directory
"""
TODO
"""
__author__ = "Chris Clark"

import sys
try:
    from setuptools import setup
except ImportError:
    print("You must have setup tools installed in order to build this plugin")
    print("Under Debian/Ubunut (with Python 2)")
    print("    sudo apt install python-setuptools")
    setup = None

if setup != None:
    setup(
        name='gz_compression',
        version='0.1',
        description=__doc__,
        author=__author__,
        author_email="clach04",
        license="GPLv2",
        url="http://editra.org",
        platforms=["Linux", "OS X", "Windows"],
        packages=['gz_compression'],
        #package_data={'gz_compression' : ['pixmaps/AUTHORS', 'pixmaps/COPYING',]},
        entry_points='''
        [Editra.plugins]
        gzip = gz_compression:HumilityTheme
        '''
        )
