#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import unittest
from appium import webdriver
import os
PATH = lambda p:os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class AppTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'm2note'
        desired_caps['appPackage'] = 'com.chemi'
        desired_caps['appActivity'] = 'com.chemi.ui.activity.StartActivity'
        # 屏蔽手机自带的默认输入法，使用appium自带的输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['app'] = PATH('C:/Users/Administrator/Desktop/1.8.6.1.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # def test_001(self):
    #     '''获取手机分辨率'''
    #     print u'分辨率为：',self.driver.get_window_size()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

