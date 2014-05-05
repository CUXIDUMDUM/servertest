#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class User(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_username(username)
    def __set_username(self, username):
        self.__username = username
    def __get_username(self):
        return self.__username
    def have_uid(self, uid):
        pass
    def exist(self)
        pass
    def belong_to_group(self, group):
        pass
    def have_home_directory(self, directory)
        pass
    def have_authorized_key(self, key)
        pass
    def have_login_shell(self, shell)
        pass

if __name__ == '__main__':
    pass
