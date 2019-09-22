# 1.用循环打印如下图形
#       *
#     * * *
#    * * * * *
#  * * * * * * *

# 4行   第1 ... 第4 即range(1,5)
# for i in range(1,5):
#     # i代表第i行
#     # 第i行做什么 ？ 打印
#     # 第1行   3个空格  1个星号
#     # 第2行   2个空格  3个星号
#     # 第3行   1个空格  5个星号
#     #
#     # 总结出规律：
#     # i + 空格数 = 4  空格数=4-i
#     # 星号数= 2i - 1

#     # 第i行   4-i个空格  i*2-1个星号

#     # 空格： 第1个  第2 个 ... 第4-i个  range(1, 4-i+1)
#     # 星号：第1个 第2个...第i*2-1个 range(1, i*2)
#     for j in range(1, 4-i+1):
#         print(' ', end=' ')
#     for k in range(1, i*2):
#         print('*', end=' ')
#     print()

# 2.用python实现冒泡排序
# 	# [50,20,30,10]
# 	#
# 	# 升序：谁大谁交换到后面
# 	# 降序：谁大谁交换到前面
# 	#
# 	# 以升序为例
# 	# 第1趟：
# 	# [20,50,30,10]
# 	# [20,30,50,10]
# 	# [20,30,10,50]
# 	# 第2趟：
# 	# [20,30,10,50]
# 	# [20,10,30,50]
# 	# 第3趟：
# 	# [10,20,30,50]

# for i in range(1, len(a)):
#     for j in range(1, len(a) - i + 1):
#         if a[j - 1] < a[j]:
#             a[j - 1], a[j] = a[j], a[j - 1]
# print(a)


# 3.用python实现选择排序
# 	# 定义：选择法排序指每次选择所要排序的数组中的最大值（由小到大排序则选择最小值）的数组元素，
# 	# 将这个数组元素的值与最前面没有进行排序的数组元素的值互换
# 	# 以升序为例：
# 	#
# 	# 原始：
# 	# lst = [50, 30, 10, 20]
# 	# 比较：
# 	# 第一趟：[10, 30, 50, 20]
# 	# 第二趟：[10, 20, 50, 30]
# 	# 第三趟：[10, 20, 30, 50]

# 4个元素，共比较了3趟
# 如果有len(lst)个元素， 会比较len(lst)-1趟。即第1趟~第len(lst)-1趟，也就是range(1, len(lst))
# 所以可以写出循环条件：for i in range(1, len(lst))

# 其中 i 代表的是第i趟
# 那么第i趟做什么呢？
# 以升序为例，举例：第1趟：从第1个到最后一个中找出最小的，跟第1个交换
#                 第2趟：从第2个到最后一个中找出最小的，跟第2个交换
#            结论：第i趟：从第i个到最后一个中找出最小的，跟第i个交换
# 怎么找最小的呢？
# 先假定范围内的第1个为为最小的，然后从范围内的第2个（也就是第i+1个）开始，直到最后一个,找到最小的，并记录它的下标
#           （整个范围内的第1个，也就是整个列表中的第i个,下标为i-1）
#           （整个范围内的第2个，也就是整个列表中的第i+1个,下标为i）  --内层循环的起点
#           （最后一个，就是整个列表中的最后一个，下标为len(lst)-1)  --内层循环的终点，写到range里要加1
# lst = [50, 30, 10, 20, 40]
#
# for i in range(1, len(lst)):
#     min_value = lst[i-1]                #记录最小值。这里的i-1是下标
#     min_index = i-1               #记录最小值对应的下标
#     for j in range(i, len(lst)):  #这里的数值范围，指的也是下标，j也是下标
#         if lst[j] < min_value:
#             min_value = lst[j]
#             min_index = j
#
#     lst[i-1], lst[min_index] = lst[min_index], lst[i-1]    #把最小的跟第i个交换
# print(lst)

# 4.接收用户输入的数字，输入负数时结束输入。存入一个列表
# 然后找出用户所输入的所有数字中最大的数，最小的数，再将所有数字从小到大排序输出

# lst = []
# while True:
#     num = input('请输入一个数字：')
#     if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
#         num = int(num)
#         if num >= 0:
#             lst.append(num)
#         else:
#             break
#     else:
#         print('输入错误')
# print(lst)
#
# print(max(lst), min(lst), sorted(lst))

# 5.列表合并(用你能想到所有方法实现)
# 	[1, 2, 3, 5, 6]    [0, 2, 5, 7]
# 	要求结果：[0, 1, 2, 3, 5, 6, 7]

# # 方法一：
# lst_1 = [1, 2, 3, 5, 6]
# lst_2 = [0, 2, 5, 7]
#
# new = []
# for num in (lst_1 + lst_2):
#     if num not in new:
#         new.append(num)
# print(sorted(new))
#
# # 方法二：
# new = sorted(list(set(lst_1+lst_2)))
# print(new)
#
# # 方法三：
# new = sorted(list({}.fromkeys(lst_1+lst_2).keys()))
# print(new)

# 6.大脚超市赊账人员名单如下：
# 	['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
# 	大脚想移除掉里面的姓氏重复的人（不考虑复姓），但是对于每种姓氏大脚想保留最后出现的那个人。希望你来帮助她
# 	参考结果：['杨晓燕','刘大脑袋','谢飞机', '赵四','王大拿']

# names = ['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
# surnames = []  #姓氏列表
# result = []    #结果姓名列表
#
# for name in names[::-1]:
#     if name[0] not in surnames:
#         surnames.append(name[0])
#         result.append(name)
# result.reverse()
# print(result)


# 7.调用慧测会议管理接口，需要填写一个参数sign-数字签名
#   sign的算法如下：
#   	用户输入的参数中，去除username参数，将其余的参数按参数名的ASCII码降序排列，
#   	在得到的参数字符串之前拼接上user=username值
#   	组合成一个新的字符串,加密后作为sign
#   要求：用户入参如下：
#   		address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi
#   	    结果:user=tianlaoshititle=Huice_Test&time=2018-01-30&limit=200&address=beijing

# source = 'address=beijing&limit=200&title=Huice_Test&time=2018-01-30&username=tianlaoshi'
# paras = source.split('&')
# reserved = None
# for i, para in enumerate(paras):
#     if para.startswith('username='):
#         reserved = paras.pop(i)
# # print(reserved)
# # print(paras)
#
# resv_value = reserved.split('=')[-1]
# result = 'user=' + resv_value + '&'.join(sorted(paras, reverse=True))
# print(result)

# 8.编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
data = {
     'ZhaoLiYing': [60, 68, 45],
     'FengShaoFeng': [10, 28, 5],
     'TianLaoShi': [44, 86, 73],
     'TangYan': [99, 95, 95],
     'LuoJin': [98, 65, 100],
     'LiuLaoShi': [77, 97, 65]
    }
# 	a.找到平均分不足60分的人
# 	b.找出各科的最高分
# 	c.算出各科的平均分，再找出各科的学霸

# 方法一：
# # a.
# print('平均分不足60分的人有：')
# for name, scores in data.items():
#     avg = sum(scores) / len(scores)
#     if avg < 60:
#         print(name)
# # b.
# yuwen_scores = []
# shuxue_scores = []
# yingyu_scores = []
#
# for scores in data.values():
#     # print(scores[0])  # 语文成绩
#     # print(scores[1])  # 数学成绩
#     # print(scores[2])  # 英语成绩
#     yuwen_scores.append(scores[0])
#     shuxue_scores.append(scores[1])
#     yingyu_scores.append(scores[2])
#
# print('语文最高分是：', max(yuwen_scores))
# print('数学最高分是：', max(shuxue_scores))
# print('英语最高分是：', max(yingyu_scores))
#
# # c.
# print('语文平均分是%.1f' % (sum(yuwen_scores) / len(data)))
# print('数学平均分是%.1f' % (sum(shuxue_scores) / len(data)))
# print('英语平均分是%.1f' % (sum(yingyu_scores) / len(data)))
#
# for name, scores in data.items():
#     if scores[0] == max(yuwen_scores):
#         print('语文学霸是%s' % name)
#     if scores[1] == max(shuxue_scores):
#         print('数学学霸是%s' % name)
#     if scores[2] == max(yingyu_scores):
#         print('英语学霸是%s' % name)


# # 方法二，统一输出，并使用排序：
# # a, b, c：
# def avg(seq):
#     return sum(seq)/len(seq)
#
# # 各科分数分别存放到三个列表
# yuwen_scores = []
# shuxue_scores = []
# yingyu_scores = []
#
# # 平均分不及格的人存放到一个列表
# who_fail = []
#
# for name, scores in data.items():
#     yuwen_scores.append(scores[0])
#     shuxue_scores.append(scores[1])
#     yingyu_scores.append(scores[2])
#
#     if avg(scores) < 60:
#         who_fail.append(name)
#
# #输出结果
# print('平均分小于60分的人有：%s' % ' '.join(who_fail))
#
# #
# print('语文最高分是%d，数学最高分是%d，英语最高分是%d' %
#       (max(yuwen_scores), max(shuxue_scores), max(yingyu_scores)))
#
# print('语文平均分是%.1f, 数学平均分是%.1f, 英语平均分是%.1f' %
#       (avg(yuwen_scores), avg(shuxue_scores), avg(yingyu_scores)))
# #
# print('语文学霸是', sorted(data.items(), key=lambda x:x[-1][0])[-1][0])
# print('数学学霸是', sorted(data.items(), key=lambda x:x[-1][1])[-1][0])
# print('英语学霸是', sorted(data.items(), key=lambda x:x[-1][2])[-1][0])


# 9.编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
data = {
    '颖宝':{'语文':60, '数学':68, '英语':45},
    '冯威':{'语文':10, '数学':28, '英语':5},
    '糖糖':{'语文':44, '数学':86, '英语':73},
    '咕噜':{'语文':99, '数学':95, '英语':95},
    '田老师':{'语文':98, '数学':65, '英语':100},
    '刘老师':{'语文':77, '数学':97, '英语':65},
}
# 	a.找到平均分不足60分的人，
# 	b.找出各科的最高分,平均分
# 	c.找出各科的学霸

# 注：data.keys(),data.values(), data.items()不支持索引
# # 定义求平均值的函数
# def avg(seq):
#     return sum(seq) / len(seq)
#
# # 三门课的成绩，分别带着人名，存入三个字典
# yuwen_scores = {}  # 举例 {'颖宝'：60, '冯威'：10, ...}
# shuxue_scores = {}
# yingyu_scores = {}
#
# # 平均分不及格的人存放到一个列表
# who_fail = []
#
# for name, scores in data.items():
#     avg_score = avg(scores.values())
#     if avg_score < 60:
#         who_fail.append(name)
#
#     yuwen_scores[name] = scores['语文']
#     shuxue_scores[name] = scores['数学']
#     yingyu_scores[name] = scores['英语']
#
# # 输出结果
# print('平均分小于60分的人有：%s' % ' '.join(who_fail))
#
#
# print('语文最高分是%d，数学最高分是%d，英语最高分是%d' %
#       (max(yuwen_scores.values()), max(shuxue_scores.values()), max(yingyu_scores.values())))
#
# print('语文平均分是%.1f, 数学平均分是%.1f, 英语平均分是%.1f' %
#       (avg(yuwen_scores.values()), avg(shuxue_scores.values()), avg(yingyu_scores.values())))
#
# print('语文学霸是', sorted(yuwen_scores.keys(), key=lambda x: yuwen_scores.get(x))[-1])
# print('数学学霸是', sorted(shuxue_scores.keys(), key=lambda x: shuxue_scores.get(x))[-1])
# print('英语学霸是', sorted(yingyu_scores.keys(), key=lambda x: yingyu_scores.get(x))[-1])


# 10.统计一篇英文文章每个单词的出现频率，并返回出现频率最高的前5个单词及其出现次数(字典形式)
# A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian
text = 'A small sample of texts from Project Gutenberg' \
       ' appears in the NLTK corpus collection. However,' \
       ' you may be interested in analyzing other texts' \
       ' from Project Gutenberg. You can browse the catalog' \
       ' of 25,000 free online books at http://www.gutenberg.org/catalog/,' \
       ' and obtain a URL to an ASCII text file. Although 90%' \
       ' of the texts in Project Gutenberg are in English,' \
       ' it includes material in over 50 other languages,' \
       ' including Catalan, Chinese, Dutch, Finnish, French, German, Italian'

# words = text.split(' ')
# print(words)
# for i, word in enumerate(words):
#     if word.endswith(',') or word.endswith('.'):
#         words[i] = word[:-1]
# print(words)
#
# for i, word in enumerate(words):
#     if word.lower() in words:
#         words[i] = word.lower()
# print(words)
#
# for i, word in enumerate(words):
#     if not word.isalpha():
#         words.remove(word)
# print(words)
#
# result = {}
# for word in words:
#     result[word] = words.count(word)
#
# print(result)
# print(dict(sorted(result.items(), reverse=True, key=lambda x: x[-1])[:5]))


# 11.给定一个字符串，例如abcabcd，请你求得该字符串中所有的长度大于等于2的子串，
# 并统计每个字串出现的次数
# s = 'abcabcd'
# sub_strings = []
# for i in range(1, len(s)):
#     for j in range(1, len(s) - i + 1):
#         sub_strings.append(s[j - 1:j + i])
#
# print(sub_strings)
#
# result = {}
# for sub_string in sub_strings:
#     result[sub_string] = sub_strings.count(sub_string)
# print(result)

# 12.输出100之内的素数总个数，所谓"素数"是指除了1和它本身以外，不能被任何整数整除的数，例如17
# 方法一：使用计数器变量
# counter = 0
#
# for i in range(2,101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end = ' ')
#         counter += 1
#
# print('\n100以内一共有%d个素数' % counter)

# 方法二：使用列表，求长度
# prime_numbers = []
# for i in range(2,101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime_numbers.append(i)
#
# print(prime_numbers)
# print('100以内一共有%d个素数' % len(prime_numbers))

# 13.一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数

# for i in range(1, 1001):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     if sum == i:
#         print(i)
