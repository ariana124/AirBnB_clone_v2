#!/usr/bin/python3
"""
fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local, run


def do_pack():
    """ generates a .tgz archive from the contents of web_static """

    time = datetime.now().strf("%Y%m%d%H%M%S")
    archive = "versions/web_static{}.tgz".format(time)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive))

    if result.failed:
        return None
    else:
        return result
