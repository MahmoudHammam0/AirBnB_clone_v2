#!/usr/bin/python3
'''Full deployment module'''
import os
from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_dep = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ["ubuntu@54.197.110.80", "ubuntu@100.24.236.222"]


def deploy():
    '''calls the two functions of do_pack and do_deploy'''
    res = do_pack()
    if os.path.exists(res):
        pass
    else:
        return False
    end = do_dep(res)
    return end
