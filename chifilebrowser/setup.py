# -*- coding: utf-8 -*-
# Setup script to build the FileBrowser plugin. To build the plugin
# just run 'python setup.py' and an egg will be built and put into 
# the plugin directory
"""Setup file for creating the filebrowser pluginr"""

import sys
try:
    from setuptools import setup
except ImportError:
    print "You must have setup tools installed in order to build this plugin"
    setup = None

__author__ = "Cody Precord"

if setup != None:
    setup(
        name='FileBrowser',
        version='2.2',
        description=__doc__,
        author=__author__,
        author_email="cprecord@editra.org",
        license="wxWindows",
        url="http://editra.org",
        platforms=["Linux", "OS X", "Windows"],
        package_data={'filebrowser' : ['locale/*/LC_MESSAGES/*.mo']},
        packages=['filebrowser'],
        entry_points='''
        [Editra.plugins]
        FileBrowser = filebrowser:FileBrowserPanel
        '''
        )
