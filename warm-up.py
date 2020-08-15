#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11/011 10:17
# @Author  : strawleave

# # 1.type判断数据类型
# print(type('陆舟'))
# print(type('8.8'))
# print(type(8.8))
# print(type(True))
# print(str(8))
# print(bool(0))
# print(bool(123))


# # 2. 计算网络带宽
# # 计算带宽的单位是bit,而计算机存储的单位是byte,它们之间是1比8的关系
# print(100/8)  # 百兆带宽每秒可以下载多少兆的文件
# # 以上程序很有局限性，我们需要引入有意义的名称——变量。
# bandwidth = 100
# ratio = 8
# print(bandwidth/ratio)
# # 可以看到第二个程序更有可读性。


# # 3. 记录12生肖，根据年份判断生肖
# chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# # 例如年份2016刚好可以被12整除，而这一年的生肖是猴，所以把猴放在了字符串的第一位
# # print(chinese_zodiac[0])
# # print(chinese_zodiac[0:4])
# # print(chinese_zodiac[-1])  # 最后一个值：猪
# year = 2020
# print(year % 12)
# print(chinese_zodiac[year % 12])
#
#
# # 3.1 序列(字符串，列表，元组)的操作
# # 字符串的切片、成员关系、连接、重复
# print('鼠' in chinese_zodiac)
# print(chinese_zodiac + '12星座')
# print(chinese_zodiac * 3)


# # 3.2 元组的实例
# # 生肖是一个字，星座是三个字，所以星座用元组比较方便
# # 不可变类型用元组，需要变化比如切片等操作，可以用列表。
# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# (month, day) = (2, 15)
#
# zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
# print(zodiac_day)
# print(type(zodiac_day))
# # print(list(zodiac_day))
# # Fix Me: 这行不注释，为什么结果就是摩羯座？
# # 答上：使用type()查看一下zodiac_day会发现它的类型是一个迭代类型，当你去取迭代类型的数据时，相当于把里面的内容拿走了，它存储的内容为空，自然统计长度变成第一个，即你看到结果。
# # 注意一下zodiac_day的类型，它的返回值是“生成器类型”，它的特点是逐个取出，取出之后里面的内容就是“空的”了。
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])
# print(zodiac_day)
# print(list(zodiac_day))  #list取走zodiac_day的数据后，再次打印发现结果为空了。


# # 3.3 列表小例
a_list = ['xyz', 123]
a_list.append('qianli')
print(a_list)
a_list.remove('xyz')
print(a_list)
