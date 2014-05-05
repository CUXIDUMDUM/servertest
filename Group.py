#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Group(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_groupname(groupname)
    def __set_groupname(self, groupname):
        self.__groupname = groupname
    def __get_groupname(self):
        return self.__groupname
    def have_gid(self, gid):
        pass
    def exist(self)
        pass

if __name__ == '__main__':
    pass
