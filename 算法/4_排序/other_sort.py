# -*- coding:utf-8 -*-
# @Time    : 2022/6/2 13:21
# @File    : other_sort.py
# Author: lee

import random
lis = [i for i in range(15)]
random.shuffle(lis)
print(lis)


"""
希尔排序：一种分组插入的排序算法

时间复杂度与 gap 的选取有关


shell sort

    1.首先取一个整数 d1 = n/2, 将元素分为 d1个组，
    每组相邻量元素之间的距离为d1，在各组内进行插入排序


    2.取第二个整数d2 = d1/2, 重复上述分组排序过程，直到
    d1 = 1， 即所有元素在同一组内进行直接插入排序

    3.希尔排序每趟并不使某些元素有序，
    而是使整体数据越来越接近有序
    最后一趟排序使得所有数据有序


    ex:
        step1:
            5 7 4 6 3 1 2 9 8

            d1 = 9 // 2 = 4
            >> 分为 4 组

            5      3      8
             7      1
              4      2
               6      9
            进行插入排序
            3 1 2 6 5 7 4 9 8



        step2:
            d2 = d1 // 2
            >> 分为 2 组
            3 1 2 6 5 7 4 9 8

            3 2 5 4 8
             1 6 7 9

            进行插入排序得到：
            2 1 3 6 4 7 5 9 8

        step3:
            d3 = d2 // 2 = 1
            就是插入排序了


"""

# 插入排序 改编 --- 基于插入排序
def insert_sort_gap(lis, gap):

    for i in range(gap, len(lis)):
        j = i -gap
        tmp = lis[i]

        while j >= 0 and lis[j] > tmp:
            lis[j+gap] = lis[j]
            j = j - gap

        lis[j+gap] = tmp


# def shell_sort(lis):
#     d = len(lis) // 2
#     while d > 0:
#         insert_sort_gap(lis, d)
#         d = d // 2
#
#
# shell_sort(lis)
# print(lis)



"""
计数排序 O(n)

对列表进行排序，已知列表中的数的范围都在 0-100 之间，
设计时间复杂度为 O(n)的算法

结合索引相关去考虑
"""

def count_sort(li, max_count = 100):
    """
    前提：知道最大数字a
    且会消耗长度为最大数字a 的列表

    :param li:
    :param max_count:  最大的数字是多少
    :return:
    """
    count = [0 for i in range(max_count+1)]

    for i in li:
        count[i] += 1

    li.clear()

    for index, val in enumerate(count):
        for i in range(val):
            li.append(index)


# count_sort(lis, 14)
# print(lis)
#





"""
桶排序：由计数排序隐身而来的桶排序
        用的不多， 不是很重要

在计数排序中，如果元素范围过大，（ex: 1-1亿）

解决：桶排序
    首先将元素分在不同的桶中，再对每个桶中的元素进行排序
    
    关键：分桶（分组）
    
    
桶排序的效率
    取决于数据的分布，需要读不同的数据进行不同的分桶的策略
    平均时间复杂度：O(n+k)
    最坏时间复杂度 O(k*n**2)
    空间复杂度 O(nk)

"""
def bucket_sort(lis, n =100, max_num=10000):
    '''

    :param lis:
    :param n: 几个桶
    :param max_num: 最大的元素
    :return:
    '''
    bucket = [[] for _ in range(n)]
    for val in lis:
        # 表示应该放到桶的编号
        i = min(val // (max_num//n), n-1)
        bucket[i].append(val)

        for j in range(len(bucket[i])-1, 0, -1):
            if bucket[i][j] < bucket[i][j-1]:
                bucket[i][j], bucket[i][j - 1] = bucket[i][j-1], bucket[i][j]

            else:
                break
    sort_lis = []
    for buc in bucket:
        sort_lis.extend(buc)
    return sort_lis


# print(bucket_sort(lis, 3, 14))





"""
基数排序：比较快，但是有内存消耗
    时间复杂度 O(kn)
    空间复杂度 O(k+n)
    
    
    由 多关键字排序 -- 先按照年龄排序，再按照工资排序
    
    对于 32 13 94 52 17 54 93 是不是可以看做是多关键字排序
    
    方法：先比低位数，再比高位数
    
    
"""
# 这个记住！！！！！
def radix_sort(lis):
    max_num = max(lis)
    it = 0
    while 10**it <= max_num: # 现在是个位
        bucket = [[] for i in range(10)]
        for var in lis:
            digit =  (var//(10**it)) % 10 # 这里有点想不出来
            bucket[digit].append(var)

        lis.clear()

        for buc in bucket:
            lis.extend(buc)
        it += 1


radix_sort(lis)
print(lis)









