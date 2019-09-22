#
# # def chufa(a, b):
# #     if b != 0:
# #         print(a / b)
# #     else:
# #         print('除数不能为0')
# #
# # chufa(1, 0)
#
#
#
# # 封装到一个函数里去
# #
# # def 函数名称  (参数列表):
# #     缩进
# #     xxx
# #     xxx
# #     xxx
# #
# # java 字母与字母之间  分割开  love beijing  loveBeijingTiananmen  小驼峰命名
# # python _分割  love_beijing_tiananmen
#
#
# #没有类的情况下， 函数要先定义再使用。
#
#
# # 两部分：  入参  出参    参数 返回
# #
# # 输入：
# # def a ()
# #
# # 无初始值参数 --- 必填项
# # 有初始值的参数 --- 用户不填 系统帮你写一个  默认值
#
# # 入学登记  一年  6  姓名 年龄 班级
#
# # 1. 没有默认值的往前放
# # def sign_up(name,  age=6, classes=1, info=[]):
# #     print(name)
# #     print(age)
# #
# #
# # sign_up(age=7, name='张', classes=2)
#
#
# # def extendList(val, list=None):
# #     if not list:
# #         list = []
# #     list.append(val)
# #     return list
# #
# #
# # list1 = extendList(10)
# # list2 = extendList(123, [])
# # list3 = extendList('a')
# #
# # print("list1 = %s" % list1)
# # print("list2 = %s" % list2)
# # print("list3 = %s" % list3)
#
#
# # 2. 不知道 会传几个？  不定长参数
# # def sign_up(name, age=6, *infos):
# #     print(name)
# #     print(age)
# #     for i in infos:
# #         print(i)
# #
# # sign_up('张三', 7)
# # sign_up('张si', 7, '男', '北京')
#
# #3 不知道 会传几个？  不定长参数 key
# # def sign_up(name, age=6, **infos):
# #     print(name)
# #     print(age)
# #     for x, y in infos.items():
# #         print(x, y)
# #
# # sign_up('张三', 7)
# # sign_up('张si', 7, sex='男', city='北京')
#
#
# #原地操作 赋值操作
# # a = [2,4,1,5,7,8]
# # print(a[0])
# # print(sorted(a))
#
#
# # def sign_up(name, age=6, **infos):
# #     d = {}
# #     d['name'] = name
# #     d['age'] = age
# #     for x, y in infos.items():
# #         d[x] = y
# #     return d
# #
# # print(sign_up('张si', 7, sex='男', city='北京'))
#
#
# # def huice(a, b, c):
# #     return (a,b,c)
# #
# # print(huice(1,2,3))
#
#
# # 编写一个生成get请求地址的函数，上游传递过来的参数有hostname=“”,url=“”,   data={}，
# # 	  请根据以上参数返回一个get请求的完整链接，其中data和url有可能不传
# #
# # return http：//主机名:url?a=1&b=2&c=3
#
#
# # def create_url(hostname, url, **data):
# #     result = 'http://{hostname}/{url}'.format(hostname=hostname, url=url)
# #     if data:
# #         list = []
# #         for k, v in data.items():
# #             d = '{k}={v}'.format(k=k, v=v)
# #             list.append(d)
# #         result = result + '?' + '&'.join(list)
# #     return result
# #
# # print(create_url(hostname='192.168.1.2', url='huice/python', a=123, b=456))
#
#
# #高阶函数   面向函数 编程    函数的入参是函数
# def A(a, b, x):
#    return x(a, b)
#
# # def x(a, b):
# #     return a/b
# #
# # def x2(a, b):
# #     return a+b
# #
# # print(A(3, 2, x))
# # print(A(3, 2, x2))
#
# # 匿名函数
# # lambda 参数 :返回值
# # print(A(3,2, lambda a,b:a+b))
#
#
#
# #高阶函数应用
# # l = ['java', 'python', 'c', 'php']
# # a = sorted(l, key=len)
# # print(a)
#
# # l = ['java', 'python', 'c', 'php']
# # a = []
# # map()
# # for i in l:
# #     a.append(i+'_huice')
# # print(a)
#
# # print(list(map(lambda x:x+'_huice', l)))
#
#
# # a = [1,2,3,4,6,7,9,11]
# # def my(x):
# #     if x % 2 == 0:
# #         return True
# #     else:
# #         return False
# #
# # print(list(filter(my, a)))
#
#
# # citys = ['北京', '成都', '上海', '武汉', '北京', '成都', '西安']
# #
# #
# # print(sorted(list(set(citys)), key=citys.index))
#
#
# # d = {'张三': 90, '李四': 75, '田老师': 100}
#
# # def my(a):
# #     return a[1]
#
# # print(sorted(d.items(), key=lambda i:i[1], reverse=True))
#
# # (('张三', 90), ('李四', 75), ('田老师', 100))
# # 类的初始化--- 属性 赋初值
# # 实例属性 实例变量
# # 类变量 static
# class Student:
#     # 析构函数--构造函数--对象在创建的过程中，执行的函数
#     #self--当前对象 自己?
#     school = '慧测'
#     def __init__(self, name, age, sex, shengao):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.shengao = shengao
#
#     def talk(self):
#         print('我的名字叫:'+self.name)
#
#     @classmethod
#     def my_school(cls):
#         print('我的学校是：'+cls.school)
#
# a = Student('张三', 19, '男', 170)
# b = Student('李四', 20, '男', 185)
# a.talk()
# b.talk()
# a.my_school()
# b.my_school()
# Student.my_school()



# 练习：
# 	1.设计一个汽车类Auto（构造函数一个参数  品牌名称），
# 	  有速度属性speed，启动start、加速speedup(1次速度+10)和停止stop(1次速度-30)方法；


# class Auto:
#     a = 4
#     def __init__(self, name):
#         self.name = name
#         self.speed = 0
#
#     def start(self):
#         self.speed = 1
#
#     def speedup(self):
#         self.speed += 10
#
# a = Auto('BMW')
# b = Auto('QQ')
# a = Auto('BMW')
#
#
# 重写
#
# a.start()
# a.speedup()
# print(a.speed)
#
# 继承 --复用  父类的
#
# 多态


# try:
#     a = 10
#     b = 0
#     c =None
#     print(c[0])
# except Exception as e:
#     print(e)
#     print('出错啦！')
#     raise (Exception())


# def sub(a, b):
#     if b == 0:
#         raise Exception('除数为0')
#     else:
#         return a/b
#
# sub(2, 0)


# a = input('请输入')
# b = 'string'
# print(a[0])



# s = 'ab13419ff7w'
# count = 0
# for i in s:
#     if i.isdigit():
#         count+=1
# print(count)


# count = 0
# for i in s:
#     try:
#         sxxxx
#         try:
#             sxxxx
#             sxxxx
#             sxxxx
#             sxxxx
#             sxxxx
#         except:
#            print(1)
#     except:
#         print(2)
#
#     finally:
#         .close()
#
#

# str = '1234rtyu#690'
# count = 0
# for i in str:
#     try:
#         i =int(i)
#         count += 1
#     except:
#         # raise Exception('含有字母了')
#         pass
# print (count)


# str = '1234rtyu#690'
# count = 0
# for i in str:
#     if i == int(i):
#         count += 1
#     else:
#         raise Exception('含有字母了')
# print (count)

# 练习：
# 	1.设计一个汽车类Auto（构造函数一个参数  品牌名称），
# 	  有速度属性speed，启动start、加速speedup(1次速度+10)和停止stop(1次速度-30)方法；
class Auto:

    def __init__(self,name):
        self.name = name
        self.speed = 0
    def start(self):
        self.speed = 1

    def speedup(self):
        self.speed += 10
        return self.speed

    def stop(self):
        self.speed -= 30
        return self.speed

A=Auto("宝马")
print(A.speed)
A.start()
A.speedup()
print(A.speed)
