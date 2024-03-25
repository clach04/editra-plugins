From 

sample setup:

    editra -c /some/path # then quit, this creates undef conf directory
    cp egg /some/path/plugins
    editra -c /some/path # can now load/save files ending in gz

Under Windows default plugin path copy:

    COPY dist\gz_compression-0.1-py2.7.egg "%USERPROFILE%"\AppData\Roaming\Editra\plugins

## TODO

  * address all FIXME and TODO items
