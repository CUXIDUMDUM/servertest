#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Interface(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_interfacename(interfacename)
    def __set_interfacename(self, interfacename):
        self.__interfacename = interfacename
    def __get_interfacename(self):
        return self.__interfacename
    def be_setted_speed(self, speed):
        pass
    def have_ipv4_address(self, ipaddress)
        pass
    def have_ipv6_address(self, ipaddress)
        pass

if __name__ == '__main__':
    pass
