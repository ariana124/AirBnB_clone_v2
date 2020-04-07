#!/usr/bin/python3
"""
fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ generates a .tgz archive from the contents of web_static """
    try:
        time = datetime.now().strf("%Y%m%d%H%M%S")
        archive = "versions/web_static{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive))
        return archive

    except:
        return None
