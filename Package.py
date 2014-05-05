#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Package(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_packagename(packagename)
    def __set_packagename(self, packagename):
        self.__packagename = packagename
    def __get_packagename(self):
        return self.__packagename
    def be_installed(self):
        pass
    def be_version(self, version):
        pass

if __name__ == '__main__':
    pass
