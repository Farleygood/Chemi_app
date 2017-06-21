#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

from basePage import BasePage

class Swipetest(BasePage):

    def __init__(self):
        pass

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 向上滑动，x轴不变，y轴从大变小
    def swipeUp(self,t):
        w_size = self.getSize()
        x1 =int(w_size[0] * 0.5)
        y1 = int(w_size[1] * 0.8)
        y2 = int(w_size[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2,t)

    # 向下滑动，x轴不变，y轴从小变大
    def swipeDown(self,t):
        w_size = self.getSize()
        x1 = int(w_size[0] * 0.5)
        y1 = int(w_size[1] * 0.2)
        y2 = int(w_size[1] * 0.8)
        self.driver.swipe(x1, y1 ,x1 ,y2, t)

    # 向左滑动，y轴不变，x从大变小
    def swipeLift(self,t):
        w_size = self.getSize()
        x1 = int(w_size[0] * 0.8)
        x2 = int(w_size[0] * 0.05)
        y1 = int(w_size[1] * 0.5)
        self.driver.swipe(x1 ,y1 ,x2 ,y1 ,t)

    # 向右滑动，y轴不变，x从小变大
    def swipeRight(self,t):
        w_size = self.getSize()
        x1 = int(w_size[0] * 0.05)
        x2 = int(w_size[0] * 0.8)
        y1 = int(w_size[1] * 0.5)
        self.driver.swipe(x1, y1, x2, y1, t)
