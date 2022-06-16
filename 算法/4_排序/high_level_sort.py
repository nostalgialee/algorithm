# -*- coding:utf-8 -*-
# @Time    : 2022/6/2 13:21
# @File    : high_level_sort.py
# Author: lee

"""
快速排序：
快速排序思路：

1.取一个元素p(默认第一个元素),使p归位
2.列表被分为两部分，左边的都比p小，右边的都比p大
3.递归完成排序


快速排序的问题
最坏情况：倒序变正序
解决方案，将第一个数与随机与列表中的数字交换
递归

"""


def partition(data, left, right):
    """
    左右指针准备，将队首第一个储存（a），
    从后找比 a 小的数，放到 a 的位置上
    此时 从右看有一个空位，再从左边找比 a 大的数，放到空位上


    :param data:
    :param left:
    :param right:
    :return:
    """
    # mid = (left + right) // 2
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            # 右边的数字大的，右指针向左移
            right -= 1
        data[left] = data[right]  # 此时右边存在一个空位

        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]

    # 碰上了
    data[left] = tmp # tmp 归位
    return left


def fast_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        """
        为啥 下面的不包含 mid
        因为 经过 partition 函数后，data[mid] 已经是中间值了
        """
        fast_sort(data, left, mid-1)
        fast_sort(data, mid+1, right)


l = [1,2,4,1,7,3,1,7,23,5,7435,]
fast_sort(l, 0, len(l)-1)
# print(l)






"""
堆排序 O(nlogn)
"""
def sift(li, low, high):
    """
    向下调整函数，前提条件子树已经是大根堆了
    :param li:
    :param low: 最后一个元素的下标
    :param high: 堆顶元素的下标
    :return:
    """
    root = low        # 根节点
    left_child= 2 * root + 1 # 左孩子
    tmp = li[low]
    while left_child <= high:
        if left_child + 1 <= high and li[left_child+1] > li[left_child]: # 右孩子比左孩子大
            left_child = left_child + 1       # 换分支了
        if li[left_child] > tmp: # 孩子比父亲大
            li[root] = li[left_child] # 孩子上去
            root = left_child
            left_child = 2 * root + 1
        else: # 父亲大于孩子
            li[root] = tmp
            break
    else:
        li[root] = tmp


def heap_sort(li):
    """
    堆排序，
    1.建立堆
    2.挨个出数了就是，然后每出一个数字。都要想要向下调整 sift

    孩子找父亲 (i - 1) // 2

    :param li:
    :return:
    """
    # 建堆: 农村包围城市
    n = len(li)
    last_node = n - 1
    root_node = (n-2) // 2

    for node in range(root_node, -1, -1):
        # node 代表的 需要调整的所有根节点的下标
        sift(li, node, last_node) # high 就是起到了边界的作用

    # 挨个出数
    for node in range(last_node, -1, -1):
        li[0], li[node] = li[node], li[0]
        sift(li,0,  node-1) # node-1是新的边界了


import random
# li = [i for i in range(15)]
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)







# 归并排序
"""
归并 O(nlogn) 空间复杂度O(n)
假设两段有序列表，怎么变成一段有序列表呢
i j 两个指针分别指向两个列表元素，从序号0开始分别比较



归并排序
    分解：将列表越分越小，直至分成一个元素
    终止条件：一个元素是有序的
        
    合并：将两个有序的列表归并，列表越来越大

"""

def merge(li, low, mid, high):
    i = low
    j = mid+1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i+=1
        else:
            ltmp.append(li[j])
            j+=1
    # 这里为什么不用
    # if i <= mid:
    #     ltmp.extend(li[i:])
    # 因为 li[i:] 元素增多了，其实并没有这么多
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def merge_sort(li, low, high):
    if low < high:
    # if len(li) < 1:
        mid = (low+high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)



li = [2,4,5,7,1,3,6,8]
merge_sort(li, 0, 7)
print(li)

# 内置方法sorted 基于 归并排序



"""
总结：

1. 时间复杂度都是 O(nlogn)
2.一般情况下（运行时间）：
    快速排序<归并排序<堆排序
    
    
3.三种排序算法的缺点：
    快速排序：极端情况下效率最低
    归并排序：需要额外的空间开销
    堆排序：在快的排序方法中相对较慢
    


"""

