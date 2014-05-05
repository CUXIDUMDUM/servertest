#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Kernel_module(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_modulename(modulename)
    def __set_modulename(self, modulename):
        self.__modulename = modulename
    def __get_modulename(self):
        return self.__modulename
    def be_loaded(self, modulename):
        pass

if __name__ == '__main__':
    pass
