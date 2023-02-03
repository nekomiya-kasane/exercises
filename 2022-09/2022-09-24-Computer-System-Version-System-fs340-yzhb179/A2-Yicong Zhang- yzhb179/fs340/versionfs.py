#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import with_statement
from filecmp import cmpfiles

import logging

import os, sys
import errno

import re
import filecmp, shutil, argparse

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from yaml import parse

MAX_VERSIONS = 6

#versioned_re = re.compile(r'\.__swp__\.(\d+)$')
versioned_re = re.compile(r'\.(\d+)$')
#nonversioned_re = re.compile(r'^(.*?)(\.__swp__\.\d+)?$')
nonversioned_re = re.compile(r'^(.*?)(\.\d+)?$')

def is_versioned(path):
    res = versioned_re.search(path)
    return -1 if not res else int(res[1])

class VersionFS(LoggingMixIn, Operations):
    def __init__(self):
        # get current working directory as place for versions tree
        self.root = os.path.join(os.getcwd(), '.versiondir')
        # check to see if the versions directory already exists
        if os.path.exists(self.root):
            print ('Version directory already exists.')
        else:
            print ('Creating version directory.')
            os.mkdir(self.root)

        #self.version_midfix = ''#'__swp__'

        self.is_move = {}

    # Helpers
    # =======

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    def _get_versioned_path(self, filename, version):
        return '.'.join([
                filename, 
                #self.version_midfix,
                str(version)]
                )

    def _get_nonversioned_filename(self, filename):
        match = nonversioned_re.match(filename)
        return match[1] if match else ''

    # Filesystem methods
    # ==================

    def access(self, path, mode):
        print ("access:", path, mode)
        full_path = self._full_path(path)
        if not os.access(full_path, mode):
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        print ("chmod:", path, mode)
        full_path = self._full_path(path)
        return os.chmod(full_path, mode)

    def chown(self, path, uid, gid):
        print ("chown:", path, uid, gid)
        full_path = self._full_path(path)
        return os.chown(full_path, uid, gid)

    def getattr(self, path, fh=None):
        print ("getattr:", path)
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))

    def readdir(self, path, fh):
        print ("readdir:", path)
        full_path = self._full_path(path)

        dirents = ['.', '..']
        if os.path.isdir(full_path):
            dirs = list(filter(lambda x: is_versioned(x) < 0, os.listdir(full_path)))
            dirents.extend(dirs)  # type: ignore
        for r in dirents:
            yield r

    def readlink(self, path):
        print ("readlink:", path)
        pathname = os.readlink(self._full_path(path))
        if pathname.startswith("/"):
            # Path name is absolute, sanitize it.
            return os.path.relpath(pathname, self.root)
        else:
            return pathname

    def mknod(self, path, mode, dev):
        print ("mknod:", path, mode, dev)
        return os.mknod(self._full_path(path), mode, dev)

    def rmdir(self, path):
        print ("rmdir:", path)
        full_path = self._full_path(path)
        return os.rmdir(full_path)

    def mkdir(self, path, mode):
        print ("mkdir:", path, mode)
        return os.mkdir(self._full_path(path), mode)

    def statfs(self, path):
        print ("statfs:", path)
        full_path = self._full_path(path)
        stv = os.statvfs(full_path)
        return dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
            'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files', 'f_flag',
            'f_frsize', 'f_namemax'))

    def unlink(self, path):
        print ("unlink:", path)
        full_path = self._full_path(path)
        if os.path.basename(path)[0] != '.':
            self.remove_old_versions(full_path) # remove history files if the original file's removed.
        return os.unlink(full_path)

    def symlink(self, name, target):
        print ("symlink:", name, target)
        return os.symlink(target, self._full_path(name))

    def rename(self, old, new):
        print ("rename:", old, new)
        return os.rename(self._full_path(old), self._full_path(new))

    def link(self, target, name):
        print ("link:", target, name)
        return os.link(self._full_path(name), self._full_path(target))

    def utimens(self, path, times=None):
        print ("utimens:", path, times)
        return os.utime(self._full_path(path), times)

    # File methods
    # ============

    def open(self, path, flags):
        print ('** open:', path, '**')
        full_path = self._full_path(path)
        return os.open(full_path, flags)

    def create(self, path, mode, fi=None):
        print ('** create:', path, '**')
        full_path = self._full_path(path)
        return os.open(full_path, os.O_WRONLY | os.O_CREAT, mode)

    def read(self, path, length, offset, fh):
        print ('** read:', path, '**')
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        print ('** write:', path, '**')
        os.lseek(fh, offset, os.SEEK_SET)

        self.is_move[path] = False

        if os.path.basename(path)[0] == '.':
            return os.write(fh, buf) # skip version system for hidden files

        res = os.write(fh, buf)

        self.versionlog(path) # versioning

        return res  

    def truncate(self, path, length, fh=None):
        print ('** truncate:', path, '**')
        full_path = self._full_path(path)
        with open(full_path, 'r+') as f:
            f.truncate(length)

    def flush(self, path, fh):
        print ('** flush', path, '**')
        if (os.path.basename(path)[0] != '.') and (path not in self.is_move):
            self.is_move[path] = True
        return os.fsync(fh)

    def release(self, path, fh):
        print ('** release', path, '**')
        if os.path.basename(path)[0] != '.':
            not_wroten = self.is_move[path]
            del self.is_move[path]
            if not_wroten: # file flushed but not written
                self.versionlog(path) # versioning
        return os.close(fh)

    def fsync(self, path, fdatasync, fh):
        print ('** fsync:', path, '**')
        return self.flush(path, fh)
    
    # Version Methods
    # ===========================
    def versionlog(self, path):
        full_path = self._full_path(path)
        n = self.append_version(path)
        if n > 0:
            print("created version {} for {}".format(n, path))
            shutil.copy2(full_path, self._full_path(self._get_versioned_path(path, n)))
        else:
            print('file has no modification.')

    def remove_old_versions(self, path):
        arr = self.get_all_version(path)
        for e in arr:
            os.remove(self._get_versioned_path(path, e))

    def get_all_version(self, path):
        dirents = []
        if os.path.isdir(self.root):
           dirents.extend(os.listdir(self.root))

        filename = os.path.basename(path)

        dirents = list(filter(lambda x: self._get_nonversioned_filename(x) == filename, dirents))
        return list(filter(lambda x: x > -1, map(is_versioned, dirents)))

    def append_version(self, filename):
        arr = self.get_all_version(filename)
        n = len(arr)
        if n and filecmp.cmp(self._full_path(self._get_versioned_path(filename, n)), self._full_path(filename)):
            return -1 # same, create no version log
        if len(arr) == MAX_VERSIONS:
            self.shift_version(filename, arr)
            return n
        return n + 1

    def shift_version(self, filename, versions):
        versions.sort()
        path = self._full_path(filename)
        if len(versions):
            os.remove(self._get_versioned_path(path, 1))
            del versions[0]
        for version in versions:
            old_path = self._get_versioned_path(path, version)
            os.rename(old_path, self._get_versioned_path(path, version - 1))
    
def main(mountpoint):
    FUSE(VersionFS(), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            print('Trying to umount {}'.format(path))
            os.system("fusermount -u {}".format(path))
        if os.path.exists(path):
            main(path)
            exit(0)
    print("\033[01;34mUsage: python versionfs.py [mount dir]\033[0m")
