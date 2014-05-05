#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Host(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_hostname(hostname)
    def __set_hostname(self, hostname):
        self.__hostname = hostname
    def __get_hostname(self):
        return self.__hostname
    def be_resolvable(self):
        pass
    def be_reachable(self)
        pass
    def match_ipaddress(self, ipaddress)
        pass

if __name__ == '__main__':
    pass
