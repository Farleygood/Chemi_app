
#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

from selenium.webdriver.support.expected_conditions import NoSuchElementException
import time as t

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_Element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except (NoSuchElementException, KeyError, ValueError, Exception),e:
            print "Error details:%s"%(e.args[0:])

    @property
    def wait(self):
        t.sleep(3)



