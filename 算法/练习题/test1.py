# -*- coding:utf-8 -*-
# @Time    : 2022/6/5 17:04
# @File    : test1.py
# Author: lee

"""
1. 给定两个字符串 s 和 t,
判断t是否为s的重新排列后组成的单词
s = 'anagtam', t = 'nagaram' return true
s = 'rat', t = 'car'. reutrn false

"""
def func(s, t):
    dict1 = {}
    dict2 = {}
    for i in s:
        dict1[i] = dict1.get(i, 0) + 1
    for i in t:
        dict2[i] = dict2.get(i, 0) + 1

    return dict1 == dict2

def func1(s, t):
    return sorted(s) == sorted(t)


# print(func1('anagram', 'nagaram'))

"""
2.给定一个 m*n的二维列表，查找一个数是否存在
列表有一下特性
每一行的列表从左到右已经排列好顺序
每一行第一个数比上一行的最后一个数大
"""

# 二分查找
def _binary_sort(lis, target):
    # 约束条件与边界条件
    m = len(lis)    # 行数
    if m == 0:
        return False
    n = len(lis[0]) # 列数
    if n == 0:
        return False
    left = 0
    right = (m*n) -1

    while left <= right:

        mid = (left + right) // 2 # 中间元素
        # 找到他的下标
        i = mid // n # 哪一行
        j = mid % n # 哪一列
        if lis[i][j] > target:
            right = mid - 1
        elif lis[i][j] < target:
            left = mid + 1
        else:
            return True
    return False

lis = [
    [1,2,3,4],
    [5,6,8,9],
    [11,14,56,89]
]

print(_binary_sort(lis, 14))


"""
3.给定一个列表和整数，设计算法找到两个数字的下标
使得两个数之间的和为给定的整数，
保证肯定仅有一个结果

例如：
[1,2,5,4] target = 3
1+2 = 3 结果就为 (0, 1)

"""



