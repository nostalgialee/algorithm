# -*- coding:utf-8 -*-
# @Time    : 2022/6/2 13:21
# @File    : low_level_sort.py
# Author: lee


"""
需要练习冒泡

"""



"""
冒泡排序 O(n**2) 原地排序
列表中每两个相邻的数，前面的数字大于后面的，
交换这两个数字.

从第一个数字开始，
1.两个相邻的数，索引0数字大于索引1的数字，
交换彼此位置，否则不变。
然后从索引2的位置与其后索引3的数字进行上述规则比较，
重复上述操作
一趟流程下来， 队尾确定最大的数，建立有序区间
一共运行 n-1 趟

"""

def bubble_sort(lst):
    """
    代码思路

    建立一个指针，记录每次的有序区间的起始索引a
    当a == 1 的时候，完成所有拍序

    """

    count = len(lst)-1 # 次数 需要进行的趟数
    for i in range(count):
        change_flag = False
        for j in range(count-i): # 无序区的区间
            # 每一趟中，比较的流程
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j+1], lst[j]
                change_flag = True
        if not change_flag: # 没发生交换，说明已经排好顺序
            break





"""
选择排序：O(n**2)
每次遍历一遍，选择出一个最小数，最后将最小值与无序区第一个数字交换（此时整个列表均为无序区）
此时无序区变小，[有序区] + [无序区]
下一次在选择第二小的，最后将第二小的与无序区第一个数字交换


代码关键点：有序区、无序区、无序区最小数的位置
...

"""
def select_sort(lst):
    for i in range(len(lst)-1): # n-1 趟
        min_index = i
        for j in range(i+1, len(lst)): # 无序区的区间
        # for j in range(i, len(lst)): # 无序区的区间
        # 每次找到的最小的数字，与放到队前，形成有序区
            if lst[min_index] > lst[j]:
                min_index = j # 记录最小值的索引

        # 最后将最小值与无序区第一个数字交换
        lst[min_index], lst[i] = lst[i], lst[min_index]

#
# l = [2,5,1,5,6,8,2,7]
# print(l)
# select_sort(l)
# print(l)



# 要好好多练习几遍， 这个理解的不好
"""
插入排序 O(n**2)

类似于摸牌
初始室友只有一张牌，
每次从无序区摸出来一张牌，插入到有牌的正确位置

"""

def insert_sort(lst):

    for i in range(1, len(lst)): # 摸牌区间
        tmp = lst[i] # (摸到的牌) 保留值
        j = i-1      # 手里的牌
        while  j >= 0  and lst[j] >= tmp:
            # 手里的牌大于摸到的牌，需要调换顺序, 且手里有牌
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = tmp


l1 = [2,3,1,34,57,8,9,2]
print(l1)
insert_sort(l1)
print(l1)

