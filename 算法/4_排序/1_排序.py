# -*- coding:utf-8 -*-
# @Time    : 2022/6/2 13:15
# @File    : 1_排序.py
# Author: lee

"""
排序：将一组无序的记录序列调整为有序的记录序列
升序与降序

内置排序函数 sort()
# sorted(iterable, key= lambda)
"""


# 低级排序
from .low_level_sort import bubble_sort
# 冒泡排序

from .low_level_sort import select_sort
# 选择排序

from .low_level_sort import insert_sort
# 插入排序



# 高级排序
from .high_level_sort import fast_sort
# 快速排序

from .high_level_sort import heap_sort
# 堆排序

from .high_level_sort import *
# 归并排序


# 其他排序
from .other_sort import *
from .other_sort import *
from .other_sort import *


