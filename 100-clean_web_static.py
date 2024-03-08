#!/usr/bin/python3
'''Keep it clean! module'''
from fabric.api import env


env.hosts = ["ubuntu@54.197.110.80", "ubuntu@100.24.236.222"]


def do_clean(number=0):
    '''deletes out-of-date archives'''
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    number += 1
    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    loc = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'.format(loc, number))
