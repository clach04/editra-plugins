File read/write plugin.

Editra doesn't have support for file read/write plugins so this claims to be a theme.
NOTE for this to work ANY other plugin needs to be activated to ensure this gets activated.

Sample setup:

    editra -c /some/path # then quit, this creates undef conf directory
    cp egg /some/path/plugins
    editra -c /some/path # can now load/save files ending in .chi

Under Windows default plugin path copy:

    COPY dist\chi_readwrite-0.1-py2.7.egg "%USERPROFILE%"\AppData\Roaming\Editra\plugins

! NOTE chi_io (and dependencies) is expected to be available to Editra!

## Usage

Open file in Editra as per normal. If operating system environment variable `EDITRA_CHI_PASSWORD` is set, that is used as the password.
If `EDITRA_CHI_PASSWORD` is not set then a GUI prompt will pause for input.

NOTE any delay/pause (e.g. password prompt, error dialog) will result in timout dialog:

    Reload File?
    FILENAME has been modified by another application.

    Would you like to reload it?

Bug (I think rather than behavior) in Editra, fix available in
https://github.com/clach04/editra/commit/d70e1d0b12f09120cc9b921892015b38641cc7ab

NOTE write/save is UNTESTED!

## TODO

  * address all FIXME and TODO items
  * re-prompt for password if password is incorrect?
  * safe-save/backup support - see https://github.com/clach04/puren_tonbo/issues/134
  * New plugin - Puren Tonbo support https://github.com/clach04/puren_tonbo (see https://github.com/clach04/puren_tonbo/issues/10)
  * see if EditraBaseStc can be monkey patched (or fixed) for other file loaders (possibly via `FileInputOutout(plugin.Interface)`)
