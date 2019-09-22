# 1.接收用户输入一个年份，判断是否是闰年
# (判断闰年的方法是该年能被4整除并且不能被100整除，或者是可以被400整除)

# year = input('请输入一个年份')
#
# if year.isdigit():
#     year = int(year)
#     if (year %4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print('是闰年')
#     else:
#         print('不是闰年')
# else:
#     print('年份输入错误')

# 2.某电信公司的市内通话费计算标准如下：三分钟内0.2元，
# 三分钟后每增加一分钟增加0.1元，不足一分钟的按一分
#   钟计算。要求编写程序，给定一个通话时间（单位：秒），
# 计算出应收费金额。
# while True:
#     time = input('请输入时间（秒）')
#     fee = 0
#
#     # 若输入的为0、正整数或小数，则满足要求，可以转成float
#     if time.isdigit() or (time.count('.') == 1 and time.replace('.', '').isdigit()):
#         time = float(time)
#
#         if time == 0:
#             fee = 0
#
#         if time / 60 <= 3:
#             fee = 0.2
#
#         elif time % 60 != 0:
#             print(time % 60)
#             fee = 0.2 + (time // 60 - 3) * 0.1 + 0.1
#
#         else:
#             fee = 0.2 + (time // 60 - 3) * 0.1
#
#         print('应收费金额为：¥%.2f' % fee)
#
#     else:
#         print('时间输入错误')

# 3.某市的出租车计费标准为：3公里以内10元，3公里以后每0.5公里加收1元；
# 每等待5分钟加收1元；超过15公里的加收原价的50%为空驶费。
# 要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）
# 计算出应付车费

# distance = input('请输入里程数(公里):')
# wait_time = input('请输入等待时间(秒)：')
#
# # 车费初始值
# charge = 0
#
# distance = float(distance)
# wait_time = float(wait_time)
#
# # 起车费
# if distance > 0 or wait_time > 0:
#     charge = 10
#
# # 加上按照距离计算的费用
# if distance > 3:
#     charge += 1 * (distance - 3) // 0.5
#
# # 加上按等待时间计算的费用
# if wait_time > 0:
#     charge += 1 * wait_time // 300
#
# # 加上空驶费
# if distance > 15:
#     charge += charge *0.5
#
# print('应付车费：￥%.2f' % charge)

# 检查
# 20公里、3000秒  -> 81元
# 20.3公里、3001秒  -> 81元

# 4.以下列表中是按照销量高低排序的手机品牌名称
# ['OPPO', 'vivo', 'Apple', 'Huawei', 'HONOR', 'MI', 'MEIZU']
# 格式化输出为下面的形式：
# 第X名：xxxx
# 第X名：xxxx
# ... ...
# 第X名：xxxx

# brands = ['OPPO', 'vivo', 'Apple', 'Huawei', 'HONOR', 'MI', 'MEIZU']
#
# for i in range(len(brands)):
#     print(f'第{i+1}名: {brands[i]}')
#
# print('---------------------------------------------')
#
# for i,brand in enumerate(brands):
#     print(f'第{i+1}名: {brand}')

# 5.练习：给一个字符串，找出其中数字分别是第几个字符
# seq = '2Apples&3Pears&5bananas'
# 格式：
# 数字“x”：是第x个字符
# for i in range(len(seq)):
#     if seq[i].isdigit():
#         print('数字%s：是第%d个字符' % (seq[i], i+1))
#
# print('---------------------------------------------')
#
# for i,char in enumerate(seq):
#     if char.isdigit():
#         print('数字%s：是第%d个字符' % (char, i + 1))


# 6.根据输入的月份来输出，这个月有几天(默认2月有28天，不考虑闰年)。
# 重复执行，直至输入exit时，程序结束

# while True:
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
#     elif month == 'exit':
#         break


# 7.接收用户输入一组整数，输入负数时结束输入，
# 输出这组数字的和：格式--您输入的数字之和是：10

# sum = 0
# while True:
#     n=input('请输入一个整数')
#     if n.isdigit() or (n.startswith('-') and n[1:].isdigit()):
#         n = int(n)
#         if n >= 0:
#             sum += n
#         else:
#             break
#     else:
#         print('输入有误')
# print(f'您输入的数字之和是：{sum}')

# 8.一个5位数，判断它是不是回文数。
# 即12321是回文数，个位与万位相同，十位与千位相同
# a = 74347
#
# a = str(a)
#
# for i in range(len(a)//2):
#     if a[i] != a[-(i+1)]:
#         print('不是回文数')
#         break
# else:
#     print('是回文数')
#
# 9.打印出100-999中所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：
# 153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方

# for num  in range(100,1000):
#     bai = num // 100
#     shi = (num % 100) // 10
#     ge = num % 10
#
#     if bai ** 3 + shi ** 3 + ge ** 3 == num:
#         print(num)
#
# print('---------------------------------------------')
#
# for num  in range(100,1000):
#     num_str = str(num)
#
#     baiwei = int(num_str[0])
#     shiwei = int(num_str[1])
#     gewei = int(num_str[-1])
#
#     if baiwei ** 3 + shiwei ** 3 + gewei ** 3 == num:
#         print(num)
