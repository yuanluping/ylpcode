# import demo
#
# demo.my_print()

# 缩进
# a = 1
#
# if a > 0:
#     print('1')
# else:
#     print('xixi')
#     print('haha')


# 换行显示
# a = 'sddfsfsfsdfsdfsdfsdf' \
#     'sadfffffffffffffff' \
#     'fffffffffffffffffffffffff' \
#     'ffffffffffffffffffff' \
#     'ffffffffffffffffffff'
#
# print(a)

# a = 1+\
#     2\
#     +3+4\
#     +5+\
#     6
#
# print(a)
#
# a = [1,
#      2,
#      3,4,
#      5,6,
#      'dsfsafd',
#      'sdfsadfsfd']
# print(a)

# 多行字符串
# poet = """两个黄鹂鸣翠柳，
# 一行白鹭上青天，
# 窗含西岭千秋雪，
# 门泊东吴万里船。"""
#
# print(poet)


# a = 'hello world'
# print(a)
#
# a = "hello world"
# print(a)

# 单引号、双引号都可以表示字符串，根据实际情况选用
# a  = "I'm OK"
# print(a)
#
# a = 'I"m ok'
# print(a)
#

#
#
#

# 注释

# 单行
# 定义一个xxx函数

# def abc():
#     '函数的功能是xxxx'
#
#     return None
#
# # 多行
#
# # 定义一个xxx函数
#
# # safdsafasdfsa
# # safdsadfsadfsafdsadf
# # safdsadfsadf
#
# def abc(x,y):
#     '''函数的功能是xxxx
#        x-xxcvxcvxz
#        y-sfdsafd
#        返回值sdfsfd'''
#     return None


# print('dsfasfd')

# Hello = 3
# print(hello)

# 赋值
# a = 'safdasfd'
# print(a)
#
# a = 1
# b = a
# print(b)
#
# a = 1
# b = a+1
#
# a = 1
# a = a + 1
# print(a)
#
# def add(x,y):
#     return x+y
#
# a = add(3, 4)
# print(a)

# 整型 int
# a = 1
# print(a)
# print(type(a))
#
# # 浮点型 float
# a = 3.14
# print(a)
# print(type(a))
# #
# # 字符串  str
# a = '士大夫士大夫'
# print(a)
# print(type(a))
#
# # 布尔型 bool
# a = True
# b = False
# print(a)
# print(type(a))
#
# # 列表 list
# a = [1,2,3,4]
# print(a)
# print(type(a))
#
# # 元组 tuple
# a = (1,2,3,4)
# print(a)
# print(type(a))
#
# # 字典 dict
# a = {'name':'zhangsan', 'age':18}
#
# print(a)
# print(type(a))

# dictionary

# 空类型 NoneType
# a = None
# print(type(a))

# a = 4
# b = 2
# c= a / b
# print(type(c))

# 整型之间
# 加减乘
# 除

# a = 4
# b = 2.0
# c= a * b
# print(type(c))

# 整型   浮点型  结果都是浮点型

# 自动类型转换

# int
# float

# 强制类型转换

# a = 4
# b = 2.0
# c = a + int(b)
# print(c)

# a = 5
# print(float(a))

# a = '12345.343'
# # print(float(a)/2)
# # b = 12345.999
# # print(int(b))
# # print(int(float(a)))
#
# print(id(a))

# a = 'Mary said, "I\'m OK"'
# print(a)

# 转义字符
# 第一类： 消除字符的特殊含义，使它变成普通字符

# 第二类
# print('t n r')

# 原来没有特殊含义
# \t
# \n
# \r
# 有特殊含义
#
# print('\r \t \n')
# \n  换行

# print('两个黄鹂鸣翠柳\n\t\t一行白鹭上青天')
# print('两个黄鹂鸣翠柳\r一行白鹭上青天')

# print('\\')

# a = '''Bob said
# I'm OK.'''
#
# print(a)
#
# a = "Bob said\nI'm OK."
# print(a)
#
# a = "div[@id='goodItem']/a"
# print(a)
#
# a = '''Bob said "I'm OK".'''
# print(a)
#
# a='"C:\\Program Files\\fnord\\foo\\bar\\baz\\frozz"'
# print(a)
#
# a= r'"C:\Program Files\fnord\foo\bar\baz\frozz"'
# print(a)
#
# a = r'^test/\d{n,}/$'
# print(a)


# a = 1
# print(id(a))
#
# a += 1
# print(id(a))

# 不可变数据类型：整数  浮点型  布尔型  空值  元组

# a = (1,2,3)
# print(id(a))
# a += (4,5)
# print(id(a))
# print(a)

# 可变数据类型： 列表 字典 对象
# a = [1,2,3]
# print(id(a))
# a += [4,5]
# # a = a + [4,5]  重新赋值，会创建出新的对象
# print(id(a))
# print(a)

# 另一个特点
# a = 1
# b = 1
# print(id(a))
# print(id(b))

# c = None
# d = None
# print(id(c))
# print(id(d))

# a = [1,2,3]
# b = [1,2,3]
# print(id(a))
# print(id(b))
# a += [4,5]

# print(11.99999 // 3)

# print(-10 // 3)

# a = 2
#
# print(a != 3)

# a is b
# id(a) == id(b)


# a = [1,2,3]
# b = [1,2,3]
# print(a is b)

# a = [1,2,3]
# b = a          # 传递赋值： 传递的是地址
# print(a is b)
# a += [4,5]
# print(b)

# 可变数据类型，不要使用传递赋值
# a=b=c=d=[1,2,3,4]
# a +=['哈哈']
# print(b)

# a += 1

# a -= 1
# a = a -1
#
# a *= 2
# a /= 2

# %=  //=  **=

# a,b,c = 1,2,3

# a = 3
# b = 10
# a,b = b,a
#
# print(a)
# print(b)
#
# if None:
#     print('A')

# 相当于False： 0 0.0 空字符串 [] （） {} None
# 相当于True:  非零数值 非空字符串、字典、元组、列表

# account = '5678'
# month = 2
# day = 10
# salary = 2000.00
# adver = '招行祝您新年快乐'

# 第一种方式
# %?占位符  %d - 十进制整数   %s - 字符串， %.nf -浮点数，保留n位小数

# msg = "您账户%s于%d月%d日入账工资，人民币%.2f，%s" % (account,
#                                                    month,
#                                                    day,
#                                                    salary,
#                                                    adver)
# print(msg)

# 第二种方式
# str.format()

# msg = "您账户{account}于{month}月{day}日入账工资，人民币{salary:.2f}，{adver}"
# msg = msg.format(adver=adver,
#                  salary=salary,
#                  month=month,
#                  day=day,
#                  account=account)
#
# print(msg)

# 第三种方式
# f-string
# msg = f"您账户{account}于{month}月{day}日入账工资，人民币{salary:.2f}，{adver}"
#
# print(msg)

# type('sadfas')
# id(a)
#
# 函数   -   输入 输出
# a = 'hellosdfasfdsafdsadfsafdsafdsafdsdfsadf'

# 长度
# print(len(a))

# 序列  有序的队列
# 正索引
# 负索引