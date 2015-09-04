# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para info_ita
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import scrapertools
from core import logger
from core import config
from core.item import Item
from servers import servertools

__channel__ = "info_ita"
__category__ = "F,S"
__type__ = "generic"
__title__ = "Info_ita (IT)"
__language__ = "IT"

def isGeneric():
    return True

def mainlist( item ):
    logger.info( "[info_ita.py] mainlist" )

    itemlist = []

    itemlist.append( Item( channel=__channel__, title="[COLOR azure]Italian Channels for Pelisalacarta[/COLOR]", thumbnail="http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png" ) )
    itemlist.append( Item( channel=__channel__, title="Original code by Jesus",thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png" ) )

    return itemlist


