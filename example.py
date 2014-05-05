#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Servertest
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.sv = Servertest.Servertest()

    def test_hosts_should_not_be_file(self):
        assert self.sv.file('/etc/hosts').should_not().be_file()

    def test_hosts_should_be_file(self):
        assert self.sv.file('/etc/hosts').should().be_file()

    def test_of_hosts_file(self):
        sf = self.sv.file('/etc/hosts')
        with sf as it:
            self.assertTrue(it.should().be_file())
            self.assertTrue(it.should_not().be_file())

if __name__ == '__main__':
    unittest.main()
