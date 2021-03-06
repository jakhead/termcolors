# -*- coding: utf-8 -*-

from os import makedirs
from os import listdir
from os.path import expanduser
from os.path import exists
from os.path import isdir

import re

HOME = expanduser('~')
RCFILE = HOME + '/.dotcolorsrc'
#THEMEDIR = HOME + '/.config/dotcolors/'

TEXT = """
#!/bin/sh
#
# ~/.dotcolorsrc
#
# Add this to your .xinitrc or .xprofile:
#
#    sh ~/.dotcolorsrc &
#

dotcolors_THEMEDIR='~/.config/dotcolors/'

xrdb -load ~/.config/dotcolors/** Not Set **
xrdb -merge ~/.Xresources

"""


def set_rcfile():
    if(exists( RCFILE )):
        return
    else:
        print "~/.dotcolorsrc not found, creating."
        outfile = open( RCFILE, 'w')
        outfile.write( TEXT )
        outfile.close()

def gset_themes_dir():
    if(exists( RCFILE )):
        infile = open( RCFILE ).read()
        themes_dir = re.findall('dotcolors_THEMEDIR[^\s]+', infile)[0].split("'")[1]
        if( len(themes_dir) > 0 ):
            themes_dir = expanduser( themes_dir )
        else:
            print "Theme directory not set, using default:\n"
            print "~/.config/dotcolors/\n"
            themes_dir = expanduser( "~/.config/dotcolors/" )


        if(isdir( themes_dir )):
            return themes_dir
        else:
            print "creating themes directory at %s" % themes_dir
            makedirs( themes_dir )
            return themes_dir


if __name__ == '__main__':
    set_rcfile()
    gset_themes_dir()
