###############################################################################
# Name: __init__.py                                                           #
# Purpose: Provides gzip compressed file support for Editra                   #
# Author: Chris Clark <clach04@gmail.com>                                     #
# Copyright: (c) 2023 Chris Clark <clach04@gmail.com>                         #
# Licence: GPLv2 Licence                                                      #
###############################################################################
"""gzip compressed read/write support plugin for Editra

Build:

    python setup.py bdist_egg

    python setup.py --quiet bdist_egg
    python setup.py --quiet bdist_egg --dist-dir=../

Simply placing the egg into the plugins directory will allow read/write of gzip
compressed files.

NOTE the plugin manager has no idea about this plugin!
It's not listed and monkey patch always takes place.
"""
__author__ = "Chris Clark"
__version__ = "0.1"


import gzip
import os
import sys


# Editra imports
import ed_txt
import plugin


class FileInputOutout(plugin.Interface):  # FIXME add to editra code base? Plugin manager has no idea about this
    pass


class GzipPlugin(plugin.Plugin):
    """Provides gzip compressed file support"""
    plugin.Implements(FileInputOutout)


def DoOpen(self, mode):
    """Opens and creates the internal file object
    @param mode: mode to open file in
    @return: True if opened, False if not
    @postcondition: self._handle is set to the open handle

    """
    if not len(self._path):
        return False

    try:
        print(self.__class__)
        print(self.__class__.__name__)
        filename = self._path
        if filename.lower().endswith('.gz'):
            if mode in ('rb', 'wb'):
                # hack time
                #fileptr = open(filename, mode)
                #file_h = gzip.GzipFile(os.path.basename(filename), 'rb', fileobj=fileptr)
                file_h = gzip.GzipFile(filename, mode)
            else:
                # FIXME raise IOError()
                self.SetLastError(unicode('%s gz plugin : mode %r not supported for compress gz files.' % (self.__class__.__name__, mode)))
        else:
            # FIXME call super instead
            file_h = open(self._path, mode)
    except (IOError, OSError), msg:
        self.SetLastError(unicode(msg))
        return False
    else:
        self._handle = file_h
        self.open = True
        return True

ed_txt.EdFile.DoOpen = DoOpen  # monkey patch!
