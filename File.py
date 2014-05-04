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

if __name__ == '__main__':
    sv_file = File('/etc/hoge')
    print sv_file.be_file()
    assert sv_file.should().be_file()
    #print(dir(sv_file))
    help(sv_file)
    #pass
