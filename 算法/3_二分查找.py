# -*- coding:utf-8 -*-
# @Time    : 2022/6/2 12:30
# @File    : 3_二分查找.py
# Author: lee


# 内置列表查找函数 index() 使用的 顺序查找

"""
二分查找：O(logn)

使用二分查找有一个先决条件，队列必须是有序数列
思想：
1.寻找中间位置
2.与中间位置的值与目标值进行比较，
    决定剔除中间值左边部分，还是右边部分
3.在留存的队列中重复上述操作，
    最后直至最后队列为0(left与right重合或者 left>right)
"""



"""
代码步骤：
代码中可以使用 left、right、mid 作为指针进行移动
对比 left right mid 对应位置上的值
if lst[mid] > target:
    right = mid - 1
elif lst[mid] < target:
    left = mid + 1
else:
    找到目标值
    
最后 left>=right 仍没有找到对应值，即列表中不存在target
"""


def binary_search(lst, target):
    right = len(lst) -1
    left = 0
    print("compare with left and right:", left, right)
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > target:
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            return mid



l = [1,2,3,5,6,7]
print(binary_search(l, 7))


