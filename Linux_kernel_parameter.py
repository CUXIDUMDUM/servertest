#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import Resource_base

class Linux_kernel_parameter(Resource_base.Resource_base):
    def __init__(self, filename):
        Resource_base.Resource_base.__init__(self)
        self.__set_parameter(parameter)
    def __set_parameter(self, parameter):
        self.__parameter = parameter
    def __get_parameter(self):
        return self.__parameter
    def have_value(self, value):
        pass
    def have_value_greater_than(self, value):
        pass
    def have_value_less_than(self, value):
        pass

if __name__ == '__main__':
    pass
