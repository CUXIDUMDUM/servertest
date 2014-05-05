#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class File(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_filename(filename)
    def __set_filename(self, filename):
        self.__filename = filename
    def __get_filename(self):
        return self.__filename
    def be_file(self):
        isfile_result = os.path.isfile(self.__get_filename())
        return self.switch_return(isfile_result)
    def exist(self)
        pass
    def be_directory(self)
        pass
    def be_link(self)
        pass
    def be_socket(self)
        pass
    def contain(self, word)
        pass
    def be_owned_by(self, owner)
        pass
    def be_mode(self, mode)
        pass
    def be_grouped_into(self, group)
        pass
    def be_linked_to(self, filename)
        pass
    def be_readable(self)
        pass
    def be_writable(self)
        pass
    def be_executable(self)
        pass
    def be_mounted(self, directory)
        pass
    def match_md5checksum(self, checksum)
        pass
    def match_sha256checksum(self, checksum)
        pass

if __name__ == '__main__':
    sv_file = File('/etc/hoge')
    print sv_file.be_file()
    assert sv_file.should().be_file()
    #print(dir(sv_file))
    help(sv_file)
    #pass
