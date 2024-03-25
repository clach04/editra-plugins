###############################################################################
# Name: __init__.py                                                           #
# Purpose: Tombo encrypted *.chi file support for Editra                      #
# Author: Chris Clark <clach04@gmail.com>                                     #
# Copyright: (c) 2024 Chris Clark <clach04@gmail.com>                         #
# Licence: GPLv2 Licence                                                      #
###############################################################################
"""Tombo encrypted *.chi read/write support plugin for Editra

Build:

    python setup.py bdist_egg

    python setup.py --quiet bdist_egg
    python setup.py --quiet bdist_egg --dist-dir=../

Simply placing the egg into the plugins directory will allow read/write of chi
encrypted files.

NOTE the plugin manager has no idea about this plugin!
It's not listed and monkey patch always takes place.

This monkey patches ed_txt.EdFile.DoOpen()
I.e. the DoOpen() method of the ed_txt.EdFile class.

Ideally the EditraBaseStc class would allow control over the file loader,
which would remove the need for monkey patching.
"""
__author__ = "Chris Clark"
__version__ = "0.1"

print('[chi_readwrite] DEBUG pre import')
import os
"""
if os.environ.get("DEBUG_PLUGIN"):
    import pdb ; pdb.set_trace()
"""
import sys


# Editra (related) imports
import wx
import ed_txt
import plugin
from util import Log  # requires enabling view of Editra log. Menu; View -> Shelf -> Editra Log

# additional imports
# https://github.com/clach04/chi_io/
# https://pypi.org/project/chi-io/
import chi_io  # FIXME chi_io dependencies (in setup.py)


Log("[chi_readwrite] PlugIn code starts - post import")

class FileInputOutout(plugin.Interface):  # FIXME add to editra code base? Plugin manager has no idea about this
    pass


class TomboChiPlugin(plugin.Plugin):
    """Provides Tombo/chi encrypted file support"""
    plugin.Implements(FileInputOutout)


original_ed_txt_EdFile_DoOpen = ed_txt.EdFile.DoOpen
def DoOpen(self, mode):
    """Opens and creates the internal file object
    @param mode: mode to open file in
    @return: True if opened, False if not
    @postcondition: self._handle is set to the open handle

    """
    if not len(self._path):
        return False

    filename = self._path
    if not filename.lower().endswith('.chi'):
        # try/except for error handling needed here?
        return original_ed_txt_EdFile_DoOpen(self, mode)

    try:
        # mode check not required, as chi_io.ChiAsFile will check
        Log("[chi_readwrite] attempting to open Tombo chi file")
        if os.environ.get("DEBUG_PLUGIN_CHI"):
            import pdb ; pdb.set_trace()

        #password = "password" ## TODO for no, no GUI. FIXME hardcoded DEBUG Pick up from environ var..
        password = os.environ.get("EDITRA_CHI_PASSWORD")
        if not password:
            password = wx.GetPasswordFromUser("Password: ", "Password required")
        # rely on chi_io to handle password (encoding, etc.) NOTE for performance consider using caching password function
        file_h = chi_io.ChiAsFile(filename, password, mode)
    except (IOError, OSError, chi_io.ChiIO), msg:
        self.SetLastError(unicode(msg))
        return False
    else:
        self._handle = file_h
        self.open = True

        # Below is not required if GuessEncoding() does NOT open filename - see https://github.com/clach04/editra/commit/da28e8a0b8407a516a389de025f9b9cbc20a5e99
        # this is both a workaround and a real solution.
        # EdFile.DetectEncoding() will call GuessEncoding() which uses the file name (rather than a get on an already open file handle)
        #self.SetEncoding('utf-8')  # Why is the main editor code using 'utf_8' - what even is that!?
        #self.encoding = 'cp1252'
        # if wrong one picked, e.g. actually utf-8 end up in a loop with GUI prompt for "The correct encoding of ...." and "utf_8" (yes underbar) will NOT be accepted as valid!
        # conversely. if really cp1252, that's not accepted either so there is a bug in the raw mode of Editra where it gets confused (probably due to leading "0" that gets prefixed to each byte
        # better fix would be to update GuessEncoding() with buffer instead of repeatedly opening and reading from file
        return True

Log("[chi_readwrite] PlugIn about to monkey-patch ed_txt.EdFile.DoOpen")
ed_txt.EdFile.DoOpen = DoOpen  # monkey patch!
