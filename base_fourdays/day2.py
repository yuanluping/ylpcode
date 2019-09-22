# 1.练习：格式化输出以下字符串：
# '亲爱的小哪吒你好！你9月的话费是32.00元，余额是18.00元'
# 其中姓名、月份、话费、余额为可变的值。
# 用%?占位符、format()、f-string三种方法实现。

# name = '小哪吒'
# month = 9
# charge = 32.80
# balance = 17.20
#
# # 1
# info = '亲爱的%s你好！你%d月的话费是%.2f元，余额是%.2f元' % (name,month,charge,balance)
# print(info)
#
# # 2.1
# info = '亲爱的{}你好！你{}月的话费是{:.2f}元，余额是{:.2f}元'
# info = info.format(name,month,charge,balance)
# print(info)
#
# # 2.2
# info = '亲爱的{name}你好！你{month}月的话费是{charge:.2f}元，余额是{balance:.2f}元'
# info = info.format(name=name,
#             month=month,
#             charge=charge,
#             balance=balance)
# print(info)
#
# # 3
# info = f'亲爱的{name}你好！你{month}月的话费是{charge:.2f}元，余额是{balance:.2f}元'
# print(info)
#
# # 3.2变化
# info = F'亲爱的{name + "同学"}你好！你{month + 1}月的话费是{round(charge):.2f}元，余额是{round(balance):.2f}元'
# print(info)
#
# info = F'亲爱的{name + "同学"}你好！你{month + 1}月的{{话费是{round(charge):.2f}元，余额是{round(balance):.2f}元'
# print(info)
#
# # 2.输出一个get请求地址，形如：
# # http://192.168.2.111/huice/event/api/add?title=python大会&time=2018-01-06
# # 其中可变的内容为：
# # 	协议类型：形如http
# # 	主机名：形如192.168.2.111
# # 	地址：形如huice/event/api/add
# # 	参数：形如title=python大会&time=2018-01-06
#
# protocol = 'http'
# host='192.168.2.111'
# address = 'huice/event/api/add'
# paras = 'title=python大会&time=2018-01-06'
#
# url = F'{protocol}://{host}/{address}?{paras}'
# print(url)
#
# # 3.拼接一个动态函数，形如：
# #
# # def test_case01(self):
# # 	'测试用例一'
# # 	execute_case('id=1')
# #
# # 其中用例编号（case01），用例描述（测试用例一），execute_case方法参数内容（id=1）
# # 均为可变的内容。
#
# num = 'case01'
# desc = '测试用例一'
# content = 'id=1'
#
# dyn_fun = f'''def test_{num}(self):
# 	'{desc}'
# 	execute_case('{content}')'''
#
# print(dyn_fun)
#
# dyn_fun = '''def test_%s(self):
# 	'%s'
# 	execute_case('%s')''' % (num, desc, content)
# #
# print(dyn_fun)

# index out of range错误
# a = 'hellokitty'
# print(a[0])
# print(a[2])
# print(a[len(a)-1])
# print(a[-1])
# print(a[-2])

# print(a[10])
# print(a[-11])
# a = ''
# print(a[0])


# a = 'hellokitty'
# 第3个到第8个字符组成的子串
# # 'llokit'
# print(a[2:8])
#
# print(a[2:8:2])
# print(a[2:]) #取到末尾
# print(a[:8]) #从开头取
# b = a[:]
# print(b)  # 字符串拷贝

# a[::2]
# print(a[:-1])
# print(a[1:])
# print(a[::-1])


# 字符串连接
# a='hello'
# b='kitty'
#
# # +
# c = a + b
# print(c)
#
# # join
# print(''.join([a,b]))


# 非字符串不能与字符串连接
# a = 'hello'
# b = 123.0
# #
# print(a + str(b))
#
# 'xiaoming'
# 'xiaohong'
# 'xiaohua'
#
# 'xiaoming&xiaohong&xiaohua'
#
# # 'xiaoming' + '&' +
#
# lst = ['xiaoming', 'xiaohong', 'xiaohua', 'xiaoxxxx']
#
# # 通过一致的分隔符连接
#
# result = '&'.join(lst)
# print(result)
#
# print(' '.join(lst))
# print(''.join(lst))
# print('++'.join(lst))
#
# # '___'.join(lst)
# #
# # 'sdfasfasfd&sdfasf'.split('&')
#
#
# # 字符串拆分
# name_str = 'xiaoming&xiaohong&xiaohua'
#
# result = name_str.split('&')
# print(result)

# id  len type
# ()     系统内建函数


# 对象的函数
#
# 抽象   对象
#
# 类型
#
# 汽车  启动  加速  减速
#
# 人   吃饭  学习

# 数据 类型

# 字符串

# str = 'sdsd'
#
# 'sdf'.join([])
# 'sdfsf'.split()
#
# 'sdfsf{}sdfsfd'.format()
#
# str1='sdfsf{}sdfsfd'
# str1.format()

# 字符串对象的函数

a = 'helloworld'
# replace
# a = a.replace('o', '0', 1)
# print(a)
#
# a=a.replace('ll', 'L')
# print(a)

# 不可变数据类型

# find
# print('w是第%d个字符' % (a.find('w') + 1))
# print ('w是第{n}个字符'.format(n=(a.find('w')+1)))
#
#
# print(a.find('k', 1, 10))
print(a.index('e'))
print(a.find('e'))

# print(round(3.1415926535, 5))

# find和index
# print(a.find('k')) #找不到返回-1
# index()

# print(a.index('w',0,6))

# a = 'helloworld'
# print(a.startswith('Hello'))

# a = '  hello  world       '
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
#
# print(a.replace(' ', ''))

# print('hello worlld'.count('ll'))

#
# a = 1
# b = 2
# c = 3
#
# print(a, b, c, sep='￥')
#
# print(a, end=' ')
# print(b, end=' ')
# print(c, end=' ')
#
# print(a, b, c, file=open('./1.txt', 'w'))


# 接收一个姓名，并把它打印出来

# a = input('请输入一个姓名：')
# print(a)

# 等待输入
# 接收输入的内容，并把输入内容返回
# 输出一个提示信息

# 会把输入的任何内容作为字符串处理

# a = input('请输入一个整数：')
# print(a)
# print(type(a))
#
# 例： 接收一个数字，把这个数字加1再输出出来

# a = input('请输入一个数字：')
#
# a = int(a)
# print(a + 1)

# 1.
# 接收用户输入的一个字符串，判断是否为纯数字

# a = input('请输入：')
#
# if a.isdigit():
#     print('是纯数字')
# else:
#     print('不是纯数字')


# 2.
# 接收用户输入的一个整数，判断能否被3整除
# a = input('请输入一个整数：')
#
# if a.isdigit() or (a.startswith('-') and a[1:].isdigit()):
#     a = int(a)
#     if a % 3 == 0:
#         print('能整除')
#     else:
#         print('不能整除')
# else:
#     print('输入错误')

# 接受用户输入的一个字符串，如果是正整数, 就判断是否能同时被3和7整除

# a = input('请输入一个字符串')
#
# if a.isdigit():
#     a = int(a)
#     if a > 0:
#         if a % 3 == 0 and a % 7 == 0:
#             print('能同时整除')
#         else:
#             print('不能同时整除')
#     else:
#         print('不是正整数')
# else:
#     print('不是正整数')
#
# 2.
# 根据输入的月份来输出，这个月有几天(默认2月有28天，不考虑闰年)，
# 要求输出格式：xx月有xx天！

a = 5

# 死循环
# while a > 0:
#
#     # 用户输入
#     month = input('请输入月份')
#
#     # 纯数字
#     if month.isdigit():
#         month = int(month)
#         if 1 <= month <= 12:
#             if month in [1,3,5,7,8,10,12]:
#                 print(f'{month}月有31天')
#
#             elif month in [4,6,9,11]:
#                 print(f'{month}月有30天')
#
#             else:
#                 print(f'{month}月有28天')
#         else:
#             print('月份有误')
#     else:
#         print('月份有误')
#
#     a -= 1


# while表达式里没有：
# 1、初始条件
# 2、值的变化
# 3、结束条件
# 4、执行次数

# 基于条件的循环

# 范围的循环

# 一筐苹果
#
# 每一个苹果尝一口
#
# 循环 模拟
#
# 一次 取 一个     操作    所有取完  完成

# while

# for 基于范围

# for xxx in yyy:
# #     print('*')

# 取出字符串中所有字母并打印
# for c in 'Hello':
#     print(c)

# a = 'Hello'
# for c in a:          #  变量赋值  自动改变   自动结束  执行次数
#     print(c)

# for c in 'Hello':
#     print('*')

# lst = [1,5,2,4,9]
# for e in lst:
#     print(e**3)

# a = 'sdfsafd 7857sd中文中文ffds778   ^&*&^'
#
# counter_a = 0
# counter_d = 0
# counter_s = 0
# counter_o = 0
#
# for c in a:
#     if c.encode('utf-8').isalpha():
#         counter_a += 1
#     elif c.isdigit():
#         counter_d += 1
#     elif c.isspace():
#         counter_s += 1
#     else:
#         counter_o += 1
#
# print(f'''字母有{counter_a}个，
# 数字有{counter_d}个，
# 空格有{counter_s}个，
# 其他字符有{counter_o}个''')


# 打印旋转小风车 来模拟一个等待图标
# import time
#
# chars = '-/|\\'
#
# while True:
#     for c in chars:
#         print(c, end='')
#         time.sleep(0.1)
#         print('\r', end='')


# for n in [1,2,3,4,5]:
#     print(n)

# print(range(1,100))

# for num in range(1,101):
#     print(num)

# 连续的数值范围   range

# 打印1-100间所有的偶数
# for n in range(1,101):
#     if n % 2 == 0:
#         print(n)

# n = 1
# while n <= 100:
#     if n % 2 == 0:
#         print(n)
#     n += 1

# 序列
animals = '牛猪马羊狗猫'
# 马是第几个字

# for a in animals:
#     if a == '马':
#         print(animals.index(a) + 1)


# 0 1 2 ... len-1
#
# 连续的数值范围
# animals[2]

# for i in range(len(animals)):
#     if animals[i] ==  '马':
#         print(i+1)

# for i, v in enumerate(animals):
#     print('%d=%s' % (i, v))

# for num in range(100, 0, -1):
#     print(num)


# for i in range(1, 6):
#
#     if i == 3:
#         break       # 跳出循环
#
#     print(i)


# for i in range(1, 6):
#
#     if i == 3:
#         continue      # 终止本次循环，直接开始下次循环
#
#     print(i)

# a = 0
#
# if a > 0:
#     pass
#
# sdf=1





