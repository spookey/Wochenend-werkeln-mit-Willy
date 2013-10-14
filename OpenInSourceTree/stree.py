#!/usr/bin/env python
# -.- coding: utf-8 -.-

from os import path, listdir, curdir
from subprocess import Popen, PIPE
from sys import argv
'''
working inside a git repository you need a quick overview?
type stree from anywhere within the repository to open it in SourceTree
'''


def  walk_up(bottom):
    '''
    i walk up from bottom to top
    https://gist.github.com/zdavkeos/1098474
    '''

    try:
        names = listdir(bottom)
    except Exception as e:
        print e
        return

    dirs, nodirs = [], []
    for name in names:
        if path.isdir(path.join(bottom, name)):
            dirs.append(name)
        else:
            nodirs.append(name)

    yield bottom, dirs, nodirs

    new_path = path.realpath(path.join(bottom, '..'))

    if new_path == bottom:
        return

    for x in walk_up(new_path):
        yield x

def launch_stree(folderarg):
    proc = Popen(['open', '-a', '/Applications/SourceTree.app', folderarg], stdin=PIPE)
    print '😺'

if __name__ == '__main__':

    if len(argv) > 1:
        if path.exists(path.realpath(argv[-1])):
            curdir = path.realpath(argv[-1])
    for current, folders, files in walk_up(path.realpath(curdir)):
        print current,
        if '.git' in folders:
            print '😻'
            launch_stree(current)
            break
        else:
            print '🙀'


