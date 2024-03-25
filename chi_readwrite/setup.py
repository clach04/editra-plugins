# -*- coding: utf-8 -*-
# Setup script to build chi/Tombo plugin. To build the plugin
# just run 'python setup.py bdist_egg' and an egg will be built and put into
# the plugin directory

__author__ = "Chris Clark"

import sys
try:
    from setuptools import setup
except ImportError:
    print("You must have setup tools installed in order to build this plugin")
    print("Under Debian/Ubuntu (with Python 2)")
    print("    sudo apt install python-setuptools")
    setup = None

if len(sys.argv) <= 1:
    print("""
Suggested setup.py parameters:

    * bdist_egg

""")

# install_requires experiment
install_requires = ['chi_io', ]
# optional 'pycryptodome'
"""End up with error:
[18:42:52][pluginmgr][info] Found plugin: chi-readwrite
[18:42:52][pluginmgr][err] Couldn't Load chi: The 'chi_io' distribution was not found and is required by the application
"""
if setup != None:
    setup(
        name='chi_readwrite',
        version='0.1',
        description=__doc__,
        author=__author__,
        author_email="clach04",
        license="GPLv2",
        url="https://github.com/clach04/editra-plugins/",
        platforms=["Linux", "OS X", "Windows"],
        #install_requires=install_requires,  # disabled as this does not work
        packages=['chi_readwrite'],  # FIXME chi_io dependencies
        #package_data={'chi_readwrite' : ['pixmaps/AUTHORS', 'pixmaps/COPYING',]},
        entry_points='''
        [Editra.plugins]
        chi = chi_readwrite:HumilityTheme
        '''
        )
