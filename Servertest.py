#!/usr/bin/env python
# -*- coding: utf-8 -*-

import File

class Servertest():
    def __init__(self):
        self.platform = ""
    def file(self, filename):
        return File.File(filename)

if __name__ == '__main__':
    pass
