# 拓展——多层嵌套循环、分支与循环嵌套

# 打印一个9*9 的方阵，由星号组成

# 9行

# 1     9
# for i in range(1, 10):  # i代表第i行
#     # 第i行做什么
#     # 打印9次 1 2    9
#     for j in range(1,10):
#         # j代表打印在第i行打印的第j次
#         print('*', end=' ')
#     print()

# 接收用户输入的一个字符串：h, w 代表矩形的高和宽，打印一个空心的矩形

# h = input('请输入高度：')
# w = input('请输入宽度：')
#
# h = int(h)
# w = int(w)
#
# for i in range(1, h+1):  # i代表第i行
#     # 第i行做什么
#     # 打印9次 1 2    9
#     for j in range(1,w+1):
#         # j代表打印在第i行打印的第j次
#         if i == 1 or i == h or j == 1 or j == w:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# 输出九九乘法口诀
# 1x1=1
# 1x2=2 2x2=4
#
#
#
# 1x9=9 2x9=18.。。。。。。 9x9=81

# for i in range(1,10): #i - 第i行
#     # 第i行做什么？打印i列
#     #         第1 2   第i列
#     for j in  range(1,i+1): #j代表第i行的第j列
#         # 第i行第j列做什么？打印
#         # 打印什么？
#         # 第3行第2列： 2x3=6
#         # 第i行第j列： jxi=j*i
#         print(f'{j}x{i}={j*i}',end='\t')
#     print()

# 计算从1加到100的和

# sum = 0
# for n in range(1,101):
#     sum += n
# print(sum)

# 接收用户输入的数字，计算该数字的阶乘
# n = input('请输入一个数字')
# n = int(n)
#
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# 接受用户输入的n, 计算1到n的阶乘之和
# 1 + 2*1 + 3*2*1 + 4*3*2*1 + 5*4*3*2*1 + ... + n*(n-1)*...*1

# n = 5
# sum = 0
# for i in range(1,n+1):
#     fact = 1
#     for j in range(1, i+1):
#         fact *= j
#     # print(fact)
#
#     sum += fact
#
# print(sum)

# 找1000以内最大平方数
#
# for n in range(1000, 0, -1):
#
#     flag = 0
#     for m in range(1, 1000):
#         if m ** 2 == n:
#             flag = 1
#             print(n)
#             break
#
#     if flag == 1:
#         break

# 让用户输入一个数， 判断在2-5之间能否有能整除它的数
# n = 10
#
#
# for i in range(2,6):
#     if n % i == 0:
#         print('有')
#         break
# else:
#     print('没有')
# #
#
# # result = []
# # for i in range(2,6):
# #     if n % i == 0:
# #         result.append(i)
# #
# # if result:
# #     print('有,是', result)
# # else:
# #     print('没有')
#
#
# # 给定一个字符串
# # target = 'hello huice'，从中找出第一个不重复的字符, 输出它是第几位
# # 只出现一次的字符
# target = 'hello huice'
#
# for i, char in enumerate(target):
#     if target.count(char) == 1:
#         print(f'第一个不重复字符是{char}，它在第{i+1}位')
#         break
#
# # 去除上一题中的重复字符，得到一个新的字符串
# res = []
# for char in target:
#     if target.count(char)==1:
#         res.append(char)
#
# print(''.join(res))

# *Pycharm断点调试


# 元组定义
# 方式一：
# a = (1,2,3)

# 方式二：
# a = 1,2,3

# 特别地：
# a = 1,
# a = (1,)
#
# print(type(a))


# 索引和分片
a = (1,6,4,8,3,5,6)

# 索引
# print(a[0])
# print(a[-1])

# 分片

# print(a[2:6:2])
# print(a[2:6:1])
# print(a[::-1])

# 删除元组
# del(a)
# print(a)

# 元组运算
# +  合并
# tup1=(1,2,3)
# tup2=(4,5,6)
#
# tup3 = tup1 + tup2
# print(tup3)
#
# # *N
# tup4 = tup1 * 3
# print(tup4)

# 内建函数作用于元组

# a = (300,2500,200)
# print(len(a))
# print(min(a))
# print(max(a))

#  将其他序列转为元组：
# t1 = tuple('hello')
# print(t1)
# # #
# t1 = tuple([3,4,5])
# print(t1)

# 元组对象的函数
T = ('aa',55,'aa',55,'a','b',33)
# print(T.index(55))
# print(T.count('a'))


# 多维元组
# tup = ((1, 2, 3), (4, 5, 6))
#
# # 取元素值
# # print(tup[0][2])
# # print(tup[1][1])
# # 对元素重新赋值
#
# tup[0][2] = 9

# tup = ([1, 2, 3], (4, 5, 6))
#
# tup[0][2] = 9
# print(tup)

# employees = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# # 1.计算员工的平均工资
# # 2.输出工资最高的员工姓名
#
# sum = 0
# for person in employees:
#     sum += person[-1]
# avg = sum/len(employees)
# print(avg)
#
# max_salary = employees[0][-1]
# max_name = employees[0][1]
#
# for person in employees:
#     if person[-1] > max_salary:
#         max_salary = person[-1]
#         max_name = person[1]
#
# print(max_name)

########## 列表  #############

# 列表定义
# my_list = ['田老师', '刘老师', '张老师']
#
# # 列表元素赋值
# my_list[2] = '小张老师'

# print(my_list)

# 列表追加元素
a = [1,2,3]
# a.append(4)

# print(a)
#
b = [4,5,6]
# a.append(b)
# print(a)

# a.extend(b)
# print(a)
#
# a += b
# print(a)

# 插入数据到列表
# my_list = ['田老师', '刘老师', '张老师']
#
# my_list.insert(1, '红烧肉')
# #
# # print(my_list)
# my_list[1:1] = ['红烧肉']
#
# print(my_list)
#
#
# # 分片赋值
# my_list = ['田老师', '刘老师', '张老师']
# list2 = ['红烧肉', '鱼香肉丝', '鸭血粉丝汤']
#
# my_list[1:] = list2
# # print(my_list)
#
# my_list[1:2] = list2
# print(my_list)
#
# my_list[1:1]


# 批量删除数据 和 清空列表
# list2 = ['红烧肉', '鱼香肉丝', '鸭血粉丝汤', '肉夹馍']
# list2[1:3] = []
# print(list2)
# list2[:] = []
# print(list2)
#
# # 删除列表
# del(list2)
# print(list2)

#列表函数

# print(str1.count(sub))
# a=str1.count(sub)
# print(a)
#
# a=a.replace('.', ' ')
# print(a)

# a = [1,2,3]
# # b=a.append(4)
# # print(b)
#
# b=a.append(4)
# print(b)

# 有返回值和无返回值


# 字符串函数都有返回值

# 列表函数不一定
a = [1,1,2,3,1,4,1]
# count append

# insert
my_list = ['田老师', '刘老师', '张老师']


# print(my_list)

#pop

my_list = ['田老师', '刘老师', '张老师']
# a=my_list.pop()
# print(my_list)
# print(a)

# b = my_list.pop(0)
# print(my_list, b)

# remove

# my_list = ['田老师', '刘老师', '张老师']
# b = my_list.remove('张老师')
# print(my_list,b)

# reverse

# my_list = ['田老师', '刘老师', '张老师']
#
# my_list.reverse()
# print(my_list)


# sort
a = [1,5,2,4,3,6,7,0]

# 升序  降序
# a.sort()  #默认：升序排列
# print(a)
#
# # 降序
# a.sort(reverse=True)
# print(a)

#

a = ['Python', 'Java', 'C', 'PHP', 'Ruby', 'Go', 'JavaScript']

# # ASCII码顺序升序排列
# a.sort()
# print(a)
#
# # ASCII码顺序降序排列
# a.sort(reverse=True)
# print(a)
#
# # 字符串长度排列
# a.sort(key=len)
# print(a)
#
a.sort(key=len,reverse=True)
# print(a)

a = ['Python5', 'Java6', 'C2', 'PHP1', 'Ruby4', 'Go3', 'JavaScript7']

# 按照最后一个字符排序
# def my_sort(arg):
#     # print(f"########{arg}")
#     return arg[-1]

# a.sort(key=lambda x:x[-1], reverse=True)
# print(a)

# 匿名函数 lambda

a = ['Python5', 'Java6', 'C2', 'PHP1', 'Ruby4', 'Go3', 'JavaScript7']


# sorted(a)
# # a.sort()
# b=sorted(a, reverse=True, key=lambda x:x[-1])
# print(b)

# a = 'Hellokitty'
# b=sorted(a)
# print(b)

people = [[1, 'zhangsan', 3000], [2, 'lisi', 2500], [3, 'tiantian', 20000]]

# print(sorted(people, reverse=True, key=lambda x:x[-1])[0][1])

# 1.检查get请求的参数中是否包含sign,如果包含将参数值替换为空格，重新拼接为参数字符串
# source = 'title=华为春季新品发布会&sign=4&limit=100&status=0&address=国家会议中心&time=2018-03-28'
# para_lst = source.split('&')
# print(para_lst)
#
# for i, para in enumerate(para_lst):
#     if para.startswith('sign='):
#         para_lst[i] = para.replace(para.split('=')[-1], ' ')
#
# print('&'.join(para_lst))

# 练习：
# 			1.用python实现冒泡排序
# 			# [50,20,30,10]


# 			# 升序：谁大谁交换到后面
# 			# 降序：谁大谁交换到前面
# 			#
# 			# 以升序为例
# 			# 第1趟：
# 			# [20,50,30,10]
# 			# [20,30,50,10]
# 			# [20,30,10,50]
# 			# 第2趟：
# 			# [20,30,10,50]
# 			# [20,10,30,50]
# 			# 第3趟：
# 			# [10,20,30,50]
# 			#


a = [50, 20, 30, 10, 25, 15]

# new = []
# for n in a:
#     new.append(n**2)
# print(new)

# print([n ** 2 for n in a])
#
# a=[1,2,3]
# b=['zhangsan','lisi','wangwu']
# c=[2000,2500,3000]
#
# d = zip(a,b,c)
# print(d)

# for e in d:
#     print(e)


# a = [1, 2, 3, 4, 5, 6]
# 一行代码实现对a中的偶数位置的元素进行加3后，组成的新列表
# new = []
# for num in a:
#     new.append(num + 3)
# print(new)
#
# print([num + 3 for num in a])

# a = [1,2,3]
# b = [4,5,6]
# a=a+b
# print(a)
# a += b

# ids = [1,2,3]
# names = ['zhang', 'li', 'wang']
# sals = [2000, 3500, 20000]
# res = zip(ids, names, sals)
# for ele in res:
#     print(ele)

# print(list('hello'))

# str1 = '{1:2,3:4}'
# print(type(eval(str1)))

# a = [1,2,3,1,2,5,6,1]
# print(a)

# new = []
# for n in a:
#     if n not in new:
#         new.append(n)
# print(new)

# set 集合
# a = {1,5,2,3,1,3,5}
# print(a)
# print(type(a))

# a = {1,5,3,2}
# print(a)         #无序

a = [3, 2, 1, 1, 2, 7, 6, 1]
b = list(set(a))
print(b)

# [1, 2, 3, 6, 7]
# 2  4  0

# [3, 2, 1, 7, 6]
b.sort(key=lambda x:a.index(x))
print(b)

#
# new = []
# for ele in a:
#     if ele not in new:
#         new.append(ele)
# print(new)


# a = {3,4,1,2,4,3,4,2}
# # print(type(a))
#
# print(a)


# a = set([1,2,3])
# print(a)

# a = [2, 5, 3, 9, 7, 3, 6, 9, 2]

# [2,5,3,9,7,6]
# new = list(set(a))
# print(new)

# 剩余元素要与原列表中出现顺序一致。
# new.sort(key=lambda x: a.index(x))
# print(new)



# 字典
# a = {'name':'张三', 'age': 18, 'height':170}
# print(type(a))
#
# # 键 - 值 对
#
# # 键： 字符串 整数   Key
#
# a = {1:'zhangsan', 2:'李四' }
#
# # 值：任意数据类型   Value
#
# a = {'name':'张三', 'age': 18, 'height':170}

# print(a['name'])
# print(a.get('name'))

# 没有索引，不能分片
# print(a['sex'])
# print(a.get('sex'))

# a['name'] = '张三丰'
# # print(a)

# a['sex'] = '男'
# print(a)
# a = {}
# a['school'] ='huice'
# print(a)

# a = {}
# print(type(a))


# 1、把字符串”k1:1|k2:2|k3:3”处理成 python 字典的形式:
# {'k1': 1, 'k2': 2, 'k3': 3}

# a = 'k1:1|k2:2|k3:3'
# dic = {}
# lst1 = a.split('|')
# for ele in lst1:
#     lst2 = ele.split(':')
#     dic[lst2[0]] = int(lst2[1])
# print(dic)
#
# del(dic['k1'])
# print(dic)
#
# del(dic)
#
a = {'name':'张三', 'age': 18, 'height':170}
# #
# print(a.values())
# print(a.keys())
# print(a.items())


# print(a.keys())
# print(a.values())
# print(a.items())
#
# e = a.pop('age')
# print(a)
# print(e)

# a = ['name', 'age', 'province']
# dic={}.fromkeys(a)
# print(dic)
#
# a = {'k1': 1, 'k2': 2}
# b = {'k1': 100, 'k3': 5}
# #
# a.update(b)
# print(a)


# a = {'name':'张三', 'age': 18, 'height':170}
# #
# for k in a.keys():
#     print(k)
# #
# for v in a.values():
#     print(v)
# #
# for k, v in a.items():
#     print(k + '是' + str(v))

# a = {'k3': 3, 'k2': 2, 'k1': 1}
# #
# lst = []
# for k, v in a.items():
#     lst.append(k + ':' + str(v))
#
# print('|'.join(sorted(lst)))

# 编写一组数据，记录组内每个人的语文成绩
# data = {
#     'ZhaoLiYing': 60,
#     'FengShaoFeng': 75,
#     'TianLaoShi': 99,
#     'TangYan': 88,
#     'LuoJin': 35,
#     'LiuLaoShi': 100
# }
# # a.算出平均分
# # b.再找出学霸
#
# print(sum(data.values())/len(data))
#
# for name, score in data.items():
#     if score == max(data.values()):
#         print(name)
