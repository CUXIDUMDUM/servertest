#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Resource_base:
    def __init__(self):
        self.__anti = False
    def should(self):
        self.__anti = False
        return self
    def should_not(self):
        self.__anti = True
        return self
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    def is_should_not(self):
        return self.__anti
    def switch_return(self, rtn):
        if self.is_should_not() == False:
            return rtn
        else:
            return not rtn

if __name__ == '__main__':
    pass
