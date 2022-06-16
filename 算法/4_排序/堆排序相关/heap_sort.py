# -*- coding:utf-8 -*-
# @Time    : 2022/6/4 15:39
# @File    : heap_sort.py
# Author: lee

"""
python 中的内置模块 --- heapq

常用函数
    heapify(x)
    heappush(heap, item)
    heappop(heap)

"""
import random
import heapq
li = [i for i in range(15)]
random.shuffle(li)

heapq.heapify(li) # 建堆
heapq.heappop(li) # 每次弹出一个最小值

