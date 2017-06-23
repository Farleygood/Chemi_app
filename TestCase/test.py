#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'
'''
tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
	tour.append(hei)
	hei /= 2
	height.append(hei)

print('总高度：tour = %s'%(sum(tour)))
print('第10次反弹高度：height = %s'%(height[-1]))


n = 1
for i in range(1,10):
	n = (n * 2) + 2
	i += 1
print n

for i in range(ord('x'),ord('z') + 1):
	for j in range(ord('x'),ord('z') + 1):
		if i != j:
			for k in range(ord('x'),ord('z') + 1):
				if (i != k) and (j != k):
					if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
						print 'order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k))


for i in range(1,8):
	if i % 2 == 0:
		continue
	else:
		print (i * '* ').center(13,' '),'\n'

for j in reversed(range(1,6)):
	if j % 2 == 0:
		continue
	else:
		print (j * '* ').center(13,' '),'\n'


a = 2
b = 1
k = []
for i in range(1,21):
	n = float(a) / float(b)
	k.append(n)
	a += a
	b += b
	i += 1
print sum(k)


n = 0
s = 0
t = 1
for n in range(1,21):
	t *= n
	s += t
print '1! + 2! + 3! + ... + 20! = %d' % s


def output(s, l):
	if l == 0:
		return
	print (s[l - 1])
	output(s, l - 1)

s = raw_input('Input a string:')
l = len(s)
output(s, l)



a = int(raw_input(u'请输入一个数字：\n'))
x = str(a)
flag = True

for i in range(len(x)/2):
	if x[i] != x[-i-1]:
		flag = False
		break

if flag:
	print u'%s是一个回文数'%x
else:
	print u'%s不是一个回文数'%x


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.WARNING + "警告字体颜色" + bcolors.ENDC
print u'这是新的一行'
'''

'''
import hashlib

def get_md5_value(arg):
    myMd5 = hashlib.md5()
    myMd5.update(arg)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


def get_sha1_value(arg):
    mySha1 = hashlib.sha1()
    mySha1.update(arg)
    mySha1_Digest = mySha1.hexdigest()
    return mySha1_Digest


if __name__ == '__main__':
    src = 'aaa'
    result_md5_value = get_md5_value(src)
    result_sha1_value = get_sha1_value(src)
    print 'source string: ', src
    print 'MD5: ', result_md5_value
    print 'SHA1: ', result_sha1_value

'''

'''
import requests
import json

# 获取设备最新版本
url1 = 'http://device.che-mi.net/rest/device/getlatestversion.do'
param = {"prodtype":"720"}
# 为什么一定要使用json.dumps把参数转换为字符串类型？------发送json数据，所以如果不用json.dumps会报错
# respone = requests.request('post',url1,data = json.dumps(param))
respone = requests.post(url1,data = json.dumps(param))
print u'this is respone code:',respone.status_code
print u'this is respone text:',respone.text
responeTest = respone.text
for key,value in json.loads(responeTest).iteritems():
    if key == 'code' and value == 200:
        print u'成功获取设备最新版本'
    if key == 'msg' and value != u'执行成功':
        print key,value

print '-' * 20

# 检测新版本
url2 = 'http://device.che-mi.net/rest/device/setversion.do'
param1 = {
          "prodtype":"1005",\
          "version":"30"\
          }
respone1 = requests.request('post',url2,data = json.dumps(param1))
# print respone1.headers['Content-Type']
respone1Test = respone1.text

for key,value in json.loads(respone1Test).iteritems():
    if key == 'result':
        if value:
            #value非空
            print u'接口执行成功，result为: %s' %value
        if not value:
            # value为空
            print u'接口执行失败，result为: %s' %value, u' 请检查version参数'

'''
'''
from Tkinter import *
import requests
import re

class App(Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.grid()
        self.ent = Entry(frame,show = "*")
        self.ent.grid(row = 0,column = 0,sticky = W)
        self.button = Button(frame)
        self.button["text"] = "submit"
        self.button["command"] = self.subm
        self.button.grid(row = 0,column = 1,sticky = W)
        self.txt = Text(frame,width = 35,height = 5,wrap = WORD)
        self.txt.grid(row = 3,column = 0,columnspan = 2,sticky = W)

    def subm(self):
        context = self.ent.get()
        # url = self.getUrlByCode(code)
        # response = requests.get(url)
        # context = response.text
        # context = context.encode('utf-8')
        # print context
        if context == "hello":
            message = "confirm"
        else:
            message = "sorry"
        self.txt.delete(0.0,END)
        self.txt.insert(0.0,message)  #用context显示查询的结果

    def getStockInfo(self,url):
        """根据url获取信息"""
        stockList = []
        response = requests.get(url)
        stockStr = response.text
        stockList = stockStr.split(',')
        return stockList

    def printStock(self,List):
        """打印相关信息"""
        print '***********name******************', List[0]
        print '***********price*****************' + List[1]
        print '***********float_price***********' + List[2]
        print '***********float_perct***********' + List[3] + '%'
        print '***********succ_unit*************' + List[4] + ' shou'
        print '***********succ_price************' + List[5]

    def getUrlByCode(self,code):
        """根据代码获取详细的url"""
        url = ''
        stockCode = ''
        if code == 'sh':
            url = 'http://hq.sinajs.cn/list=s_sh000001'
        elif code == 'sz':
            url = 'http://hq.sinajs.cn/list=s_sz399001'
        elif code == 'cyb':
            url = 'http://hq.sinajs.cn/list=s_sz399006'  # 创业板
        else:
            pattern = re.compile(r'^60*')
            match = pattern.match(code)
            if match:
                stockCode = 'sh' + code
            else:
                stockCode = 'sz' + code
            url = 'http://hq.sinajs.cn/list=s_' + stockCode
        return url

root = Tk()
root.title("Stock_price")
app = App(root)
root.mainloop()

'''

'''
class A(object):
    def __init__(self,xing,gender):
        self.namea = 'aaa'
        self.xing = xing
        self.gender = gender

    def funca(self):
        print 'function a :%s'%self.namea

class B(A):

    def __init__(self,xing,gender,age):
        super(B,self).__init__(xing,gender)   #这里应该是gender,写成age也不报错
        self.nameb = 'bbb'
        self.namea = 'ccc'
        #self.xing = xing.upper()
        self.age = age + 1
        # self.gender = gender.upper()

    def funcb(self):
        print 'function b: %s'%self.nameb

b = B('lin','nv',100)
c = A('daa','Age')
print b.gender ,'b.gender'

'''

'''
import json
import requests
url = "http://httpbin.org/post"
payload = {'some':'data'}
headers = {'content-type':'application/json'}
r = requests.post(url,data=json.dumps(payload),headers=headers)
print r.status_code
print r.text
print r.headers
'''
print 'test'
dict1 = {"ecode":0,"msg":"SUCCESS","data":[{"$id":"55d43d077f8b9ad56b8b4576","page_id":115323,"page_order":0}]}
print dict1['data'][0]['page_id']

print 'add dev1'

print 'add dev'

print 'add dev again'