'''
class class_method():
    def __init__(self, phone='mi'):
        self.phone = phone
        print(self.phone)

    @classmethod
    def changePay(self, city='beijing', new_pay=2):
        self.city = city
        self.new_pay = new_pay
        if city == 'beijing':
            self.new_pay = 1
        elif city == 'chongqing':
            self.new_pay = 2
        else:
            self.new_pay = 3

    def changephone(self):
        if self.new_pay == 1:
            self.phone = 'iphone'
        elif self.new_pay == 2:
            self.phone = 'mi'
        elif self.new_pay == 3:
            self.phone = 'redMi'
        else:
            self.phone = 'other'
        print(self.phone)


clsMe = class_method()
clsMe.changePay('chongqing')
clsMe.changephone()
clsMe.changePay('chengdu')
clsMe.changephone()
'''

'''
def info(aha):
    print('this is 函数装饰器')

    def noname(*args):
        print('---代码块之前---')
        aha(*args)
        print('---代码块之后---')
    return noname


@info
def beizhuansi(a, c):
    print('这是一个调用函数')
    print('a的值为： ', a)
    print('b的值为： ', c)


beizhuansi(4, 5)
'''
'''函数装饰器'''

'''
def decorate(fn):
    print('this is a decorate')

    def trueMethod(*args):
        print('front')
        fn(*args)
        print('back')
    return trueMethod


@decorate
def aha(a, b):
    print('this is A', a)
    print('this is B', b)


aha('hello', 'world')
'''


# property定义方法
'''

class rectangle_A:
    def __init__(self, chang=10, kuan=20):
        self.chang = chang
        self.kuan = kuan

    def getarea(self):
        return self.chang * self.kuan

    def setarea(self, area_prameter):
        self.chang = area_prameter[0]
        self.kuan = area_prameter[1]

    def getperimete(self):
        return (self.chang + self.kuan) * 2

    def setperimete(self, perimete_prameter):
        self.chang = perimete_prameter[0]
        self.kuan = perimete_prameter[1]

    area = property(fget=getarea, fset=setarea, doc='获取面积')
    perimeter = property(fget=getperimete, fset=setperimete, doc='获取周长')


r = rectangle_A(30, 40)
# 获取area
print(r.area)
# 获取perimete
print(r.perimeter)
r.area = (0, 1)
r.perimeter = (2, 3)
print(r.area)
print(r.perimeter)
'''


# 封装和隐藏
"""
class Demo():
    def __init__(self, subject='语文', score=100):
        self.__subject = subject
        self.__score = score

    def getSubject(self):
        return self.__subject

    def setSubject(self, subject):
        self.__subject = subject

    def getScore(self):
        return self.__score

    def setScore(self, score):
        if isinstance(score, int) and 0 < score <= 100:
            self.__score = score
        else:
            print('信息错误')

    subject = property(fget=getSubject, fset=setSubject)
    scroe = property(fget=getScore, fset=setScore)


d = Demo()
print(d.scroe)
d.scroe = 59
print(d.scroe)
"""

# 重写和继承
'''


class bird:
    def fly(self):
        print("we can fly")


class Penguin(bird):
    def fly(self):
        print("sorry, i can`t fly but i can swimming")


P = Penguin()
P.fly()
'''

# 调用父类被重写的方法

'''
class exercise:
    def __init__(self, ball, how):
        self.ball = ball
        self.how = how

    def palyBsaketball(self):
        print('we have ', self.ball, 'i can ', self.how)


class swimming(exercise):
    def __init__(self, how):
        super().__init__(how)

    def swimming(self):
        print('i can ', self.how)
'''


# io流读写文件
'''
try:
    f = open(site, 'r+', 1, 'utf-8')
    for i in f:
        print(i)
except IOError as e:
    print(e)
finally:
    f.close()

for i in linecache.getlines('ahaha.py'):
    print(i, end='')
'''
# with 子句的用法

'''
class fkpy:
    def __init__(self, fk):
        print('构造器')
        self.fk = fk

    def __enter__(self):
        print('该资源的fk', self.fk)
        return 'fkjava'

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if ex_traceback:
            print('expect to close')
        else:
            print('正常关闭')


with fkpy('crazyit') as f:
    print('f 的值为', f)
    try:
        raise Exception(20, 'aha')
    except OSError as e:
        print('aha', e)
    finally:
        pass
'''
'''
# sys.stdin
import sys

for line in sys.stdin:
    print(line)
'''
# 写文件



'''
a = 5
b = 3
st = print('crazyIt'), 'a大于b' if a > b else 'a 不大于 b'
print(st)
'''


'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
'''

'''
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(type(nowTime))
print(nowTime)
'''

'''

def gena_gen(value):
    i = 0
    out_val = None
    while True:
        if out_val is not None:
            out_val = yield out_val ** 2
            print('-------%d' % out_val)
        else:
            yield i**2
            i += 1
'''

'''
# 生成器
sg = gena_gen(10)
print(sg.send(None))
print(next(sg))
print(next(sg))
print('----------')
print(sg.send(9))
print(next(sg))
print(next(sg))
print(next(sg))
'''
