#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Port(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_port(port)
    def __set_port(self, port):
        self.__port = port
    def __get_port(self):
        return self.__port
    def be_listening(self):
        pass
    def be_listening_with(self, process):
        pass

if __name__ == '__main__':
    pass
