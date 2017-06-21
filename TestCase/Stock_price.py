#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import requests
import re
from Tkinter import *

def getStockInfo(url):
    """根据url获取信息"""
    stockList = []
    response = requests.get(url)
    stockStr = response.text
    stockList = stockStr.split(',')
    return stockList


def printStock(List):
    """打印相关信息"""
    print '***********name******************' , List[0]
    print '***********price*****************' + List[1]
    print '***********float_price***********' + List[2]
    print '***********float_perct***********' + List[3] + '%'
    print '***********succ_unit*************' + List[4] + ' shou'
    print '***********succ_price************' + List[5]


def getUrlByCode(code):
    """根据代码获取详细的url"""
    url = ''
    stockCode = ''
    if code == 'sh':
        url = 'http://hq.sinajs.cn/list=s_sh000001'
    elif code == 'sz':
        url = 'http://hq.sinajs.cn/list=s_sz399001'
    elif code == 'cyb':
        url = 'http://hq.sinajs.cn/list=s_sz399006'   # 创业板
    else:
        pattern = re.compile(r'^60*')
        match = pattern.match(code)
        if match:
            stockCode = 'sh' + code
        else:
            stockCode = 'sz' + code
        url = 'http://hq.sinajs.cn/list=s_' + stockCode
    return url

count = 0
while (count <= 100):
    code = raw_input('please input a stockCode: ')
    # 打印该code的信息
    url = getUrlByCode(code)
    stockInfo = getStockInfo(url)
    printStock(stockInfo)

    top = Tk()
    top.geometry('160x160+1650+870')
    listtab = Listbox(top)
    for item in stockInfo:
        listtab.insert(0,item)
    listtab.pack()
    count += 1
    top.mainloop()
