#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Process(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_process(process)
    def __set_process(self, process):
        self.__process = process
    def __get_process(self):
        return self.__process
    def be_running(self):
        pass

if __name__ == '__main__':
    pass
