chifilebrowser an Editra Python 2.x plugin

chifilebrowser is based on filebrowser 2.2 by Cody Precord

NOTE it requires chi support, aka Tombo (puren tonbo) support
from https://github.com/clach04/editra/tree/tombo_chi

Rough notes:

    git clone https://github.com/clach04/editra.git
    cd editra
    git checkout tombo_chi
    cd plugins
    git clone https://github.com/clach04/editra-plugins.git
    git checkout chifilebrowser
    cd ..
    cd src
    TODO get chi_io.py  -- https://github.com/clach04/chi_io
    cd ..
    TODO get dependencies (wx, PyCrypto, ...)
    c:\Python27\python editra


Known to work with:

Python 2.7.10 win32 and wxMSW 2.8.12.1

Looks like was working at one point with older chi_io.py from
https://hg.sr.ht/~clach04/pytombo/browse/src/pytombo/chi_io.py?rev=tip
Circa
 * December 8, 2019, 11:16:13 AM  - https://hg.sr.ht/~clach04/pytombo/rev/9f2a1239ed91ea9c399cab2a9713f1dcbff55ef0
 * September 6, 2020, 12:21:58 PM  - https://hg.sr.ht/~clach04/pytombo/rev/8699465a3c6f5c11c52be8b7400c52b1aa11162b
untested with https://github.com/clach04/chi_io


## Build Notes

To build the plugin run:

    python setup.py

an egg will be built and put into the plugin directory.
