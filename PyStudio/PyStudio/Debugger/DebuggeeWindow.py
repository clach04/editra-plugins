# -*- coding: utf-8 -*-
# Name: DebugResultsList.py
# Purpose: Debugger plugin
# Author: Mike Rans
# Copyright: (c) 2010 Mike Rans
# License: wxWindows License
###############################################################################

"""Editra Shelf display window"""

__author__ = "Mike Rans"
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#----------------------------------------------------------------------------#
# Imports
import wx

# Editra Libraries
import eclib

# Local Imports
from PyStudio.Common.PyStudioUtils import PyStudioUtils
from PyStudio.Debugger.RpdbDebugger import RpdbDebugger

# Globals
_ = wx.GetTranslation

#----------------------------------------------------------------------------#

class DebuggeeWindow(eclib.OutputBuffer,
                       eclib.ProcessBufferMixin):
    """Debuggee Window"""
    
    DEBUGGEEFINISHEDTEXT = _("\n\nDebuggee finished.")
    
    def __init__(self, *args, **kwargs):
        eclib.OutputBuffer.__init__(self, *args, **kwargs)
        eclib.ProcessBufferMixin.__init__(self)
        self.calldebugger = None
        self.restoreautorun = None
        
    def set_mainwindow(self, mw):
        self._mainw = mw

    def DoProcessStart(self, cmd=''):
        """Override this method to do any pre-processing before starting
        a processes output.
        @keyword cmd: Command used to start program
        @return: None

        """
        if self.calldebugger:
            wx.CallAfter(self.calldebugger)

    def DoProcessExit(self, code=0):
        """Override this method to do any post processing after the running
        task has exited. Typically this is a good place to call
        L{OutputBuffer.Stop} to stop the buffers timer.
        @keyword code: Exit code of program
        @return: None

        """
        self.AppendUpdate(self.DEBUGGEEFINISHEDTEXT)
        self.restoreautorun()
        self.Stop()
        RpdbDebugger().debugbuttonsupdate()
        