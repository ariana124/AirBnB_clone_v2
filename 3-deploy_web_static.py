#!/usr/bin/python3
"""
fabric script that distributes an archive to your web servers, using
the function do_deploy:
"""
from datetime import datetime
from fabric.api import env, local, put, run
import os


env.hosts = ["35.196.72.218", "18.207.121.172"]
env.user = "ubuntu"


def do_pack():
    """ generates a .tgz archive from the contents of web_static """

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_file))

    if result.failed:
        return None
    else:
        return archive_file


def do_deploy(archive_path):
    """ distributes an archive to my web servers """
    if os.path.exists(archive_path) is not True:
        return False

    filename = os.path.basename(archive_path)
    fname, ext = os.path.splitext(filename)
    rel_dir = "/data/web_static/releases"

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/{}".format(rel_dir, fname))
        run("sudo tar -xzf /tmp/{} -C {}/{}".format(filename, rel_dir, fname))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv {}/{}/web_static/* {}/{}".format(rel_dir, fname,
                                                      rel_dir, fname))
        run("sudo rm -rf {}/{}/web_static".format(rel_dir, fname))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/{}/ /data/web_static/current".format(rel_dir,
                                                                fname))
        return True
    except:
        return False


def deploy():
    """ packs and deploys an archive to my web servers """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
