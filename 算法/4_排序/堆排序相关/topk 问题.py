# -*- coding:utf-8 -*-
# @Time    : 2022/6/4 15:46
# @File    : topk 问题.py
# Author: lee

"""
堆排序：
现有n个数，设计算法得到前k大的数 k<n
ex:榜单


解决思路
    1、排序后切片 O(nlogn)
    2、lowb 三人组 冒泡排序 O(kn)
    3、堆排序
        前 k 个数字建立小根堆，然后将剩余的列表中
        所有元素依次与堆顶元素进行比较，大于堆顶元素
        就取代原来对顶元素，然后进行向下调整
"""


# 代码实现

def sift(li, low, high):
    # 向下调整
    i = low
    node = 2 * i + 1
    tmp = li[i]
    while node <= high:
        if node+1 <= high and li[node+1] < li[node]:
            node = node + 1
        if li[node] < tmp: # 孩子比父亲小，孩子取代父亲
            li[i] = li[node]
            i = node
            node = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp




def topk_sort(li, k):
    # 建立小根堆
    target = li[:k] # 排序区间
    # 建堆
    # 从最后一个根节点开始
    for i in range((k-2)//2, -1, -1):
        sift(target, i, k-1)

    # 遍历列表中剩余的所有元素
    for i in range(k, len(li)-1):
        if li[i] > target[0]:
            target[0] = li[i]
            sift(target, 0, k-1)

    # 排序 --- 挨个出数
    for i in range(k-1, -1, -1):
        target[0], target[i] = target[i], target[0]
        sift(target, 0, i-1)

    print(target)

    return target


import random
# li = [i for i in range(16)]
li = [11,23,45,5,3,4,23,423,6,657,6]
random.shuffle(li)
print(li)
topk_sort(li, 7)

