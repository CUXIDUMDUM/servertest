#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Servertest
import unittest

sv = Servertest.Servertest()

def assert_func(func):
    assert func()

def add_func_to_suite(suite, func):
    suite.addTest(unittest.FunctionTestCase(func))

sf = sv.file('/etc/hosts')
with sf as it:
    it.should().be_file()
    it.should_not().be_file()

suite = unittest.TestSuite()
add_func_to_suite(suite, sv.file('/etc/hosts').should().be_file)
add_func_to_suite(suite, sv.file('/etc/hosts').should_not().be_file)
unittest.TextTestRunner(verbosity=2).run(suite)
