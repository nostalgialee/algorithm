# -*- coding:utf-8 -*-
# @Time    : 2022/6/3 16:39
# @File    : practice.py
# Author: lee





import random
lis = [i for i in range(15)]
random.shuffle(lis)
print(lis)


# 二分查找
def binary_search(lis, target):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] > target:
            right = mid - 1
        elif lis[mid] < target:
            left = mid + 1
        else:
            return mid

    print('meiyou')

# li = [i for i in range(15)]
# binary_search(li, 8)



# 冒泡排序
def bubble_sort(lis):

    for i in range(len(lis)-1):
        change_flag = False
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
                change_flag = True
        if not change_flag:
            return

# bubble_sort(lis)
# print(lis)


# 选择排序
def select_sort(lis):
    # 每次挑选一个最小的
    for i in range(len(lis)):
        min_index = i # 最小的下标
        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_index]:
                min_index = j
        lis[i], lis[min_index] = lis[min_index], lis[i]

# select_sort(lis)
# print("select_sort", lis)


# 插入排序
def insert_sort(lis):
    for i in range(1, len(lis)):
        j = i - 1
        tmp = lis[i]
        while j >= 0 and lis[j] > tmp:
            lis[j+1] = lis[j]
            j = j - 1

        lis[j+1] = tmp

# insert_sort(lis)
# print('insert_sort', lis)





# 快速排序, 还是有点问题的
def parention(lis, left, right):
    tmp = lis[left]
    while left < right:
        while left < right and lis[right] >= tmp:
            right -= 1
        lis[left] = lis[right]
        while left < right and lis[left] <= tmp:
            left += 1
        lis[right] = lis[left]
    # left == right
    lis[left] = tmp

    return left


def fast_sort(lis, left, right):
    if left < right:
        mid = parention(lis, left, right)
        fast_sort(lis, left, mid - 1)
        fast_sort(lis, mid + 1, right)

# fast_sort(lis, 0, 14)
# print(lis)




# 堆排序
def sift(lis, low, high):

    # 向下调整
    i = low
    j = 2 * i + 1 # 左节点
    tmp = lis[i]
    while j <= high:
        pass
        if j + 1 <= high and lis[j + 1] > lis[j]:
            j = j + 1 # 变为右节点
        if lis[j] > tmp:
            lis[i] = lis[j]
            i = j
            j = 2 * i + 1
        else:
            lis[i] = tmp
            break
    else:
        lis[i] = tmp


def heap_sort(lis, low, high):
    # 建堆
    n = len(lis)
    for i in range((n-2)//2, -1, -1):
        # i 是从后往前的 子树根节点 坐标
        sift(lis, i, n-1)
    # 挨个出数
    for i in range(n-1, -1, -1):
        lis[i], lis[0] = lis[0], lis[i]
        sift(lis, 0, i-1)

# heap_sort(lis, 0, 14)
# print(lis)



# 归并排序
def merge(lis, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if lis[i] > lis[j]:
            ltmp.append(lis[j])
            j = j + 1
        else:
            ltmp.append(lis[i])
            i = i + 1
    if i <= mid:
        ltmp.extend(lis[i:mid+1])
    if j <= high:
        ltmp.extend(lis[j:high+1])
    lis[low:high+1] = ltmp


def merge_sort(lis, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(lis, left, mid)
        merge_sort(lis, mid+1, right)

        merge(lis, left, mid, right)


# merge_sort(lis, 0, 14)
# print(lis)



# 挨个分解成单个元素比较大小，





# 希尔排序
# 基于 插入排序


def insert_sort_gap(lis, gap):
    for i in range(gap, len(lis)):
        j = i - gap
        tmp = lis[i]
        while j >= 0 and lis[j] > tmp:
            lis[j+gap] = lis[j]
            j = j - gap
        lis[j+gap] = tmp


def shell_sort(lis):
    d = (len(lis)) // 2
    while d > 0:
        insert_sort_gap(lis, d)
        d = d // 2


# shell_sort(lis)
# print(lis)


# 计数排序
def count_sort(lis, max_count=100):

    ltmp = [0 for i in range(max_count)]
    for item in lis:
        ltmp[item] += 1
    lis.clear()
    for ind, val in enumerate(ltmp):
        for i in range(val):
            lis.append(ind)

# count_sort(lis)
# print(lis)


# 桶排序


# 基数排序
def radix_sort(lis):
    max_num = max(lis)
    it = 0
    while 10 ** it <= max_num:
        bucket = [[] for i in range(10)]
        for val in lis:
            digit = (val//(10**it)) % 10
            bucket[digit].append(val)

        lis.clear()

        for buc in bucket:
            lis.extend(buc)
        it += 1


# radix_sort(lis)
# print(lis)



# 哈希表
    # 链表

class LinkList:

    class Node:

        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator:

        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                curnode = self.node
                self.node = curnode.next
                return curnode.item
            else:
                raise StopIteration

        def __iter__(self):
            return self


    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = self.node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        return False

    def __iter__(self):
        # 返回迭代器
        # 定义 __iter__ 方法需要在使用时创建迭代器才能使用 iter() 方法
        # 即 iter() 方法 需要调用类中的 __iter__ 魔术方法
        return self.LinkListIterator(self.head)

    def __repr__(self):
        # 打印显示迭代器
        return "<<" + ", ".join(map(str, self)) + ">>"
