# -*- coding:utf-8 -*-
# @Time    : 2022/6/9 17:05
# @File    : 4_哈希表.py
# Author: lee

# 重点看看

# 哈希表（散列表）：python 中的实例：字典与集合 由 哈希表实现

"""
哈希表：
    是一个通过哈希函数来计算数据存储位置的数据结构
    通常支持一下操作
        insert(key, value)
        get(key)
        delete(key)

"""



# 一、直接寻址表：就是将 数字a 放到索引为 a 的位置上去

#       当关键字的全域U比较小的时候，直接寻址法是一种简单而有效的方法

    # 缺点：
        # 1. 当 U 很大的时候，需要消耗内存，很不实际
        # 2. 如果 U 很大，而实际 Key 很少的时候，会造成浪费
        # 3. 无法处理关键字不是数字的情况





# 二、哈希函数
# 哈希表 = 直接寻址表 + 哈希函数

"""
    哈希表 Hash Table, 散列表，是一种线性表的存储结构，
    # 哈希表 = 直接寻址表 + 哈希函数
    哈希函数h(k) 将关键字k作为自变量，返回元素的存储下标
        可以将U中很大的数, 转换为较小的下标，然后存储



    直接寻指表：key 为 k 的元素放在 k 位置上
    改进直接寻址表：
        1.构建大小为m的寻址表T
        2.key 为 k 的元素放在h(k)位置上
        3.h(k)是一个函数，其将域U映射到表 T[0,1,2..m]



           域                h(k) 哈希          寻址表T
    [-------------]                             {
    [             ]                             
    [      14     ]                             0:14
    [      22     ]          h(k) = k%7         1:22
    [      3      ]                             2:
    [      5      ]                             3:3
    [             ]                             ...
    [-------------]                                 }




    --------------------------------------------------
        
    # 哈希冲突：由于哈希表的大小是有限的，但是存储的值是无线的，
    当两个全域中的不同元素映射到寻址表中的同一位置的时候 --- 哈希冲突
        
    h(7) = h(14)
    
    
    解决方法：
        1.开放寻址法: 哈希函数返回的位置已经有值，则可以向后探查新的位置来存储
            线性探查
                如果 i 位置被占用，那么使用 i+1, i+2...
                    
            二次探查        
                如果 i 位置被占用，那么使用 i**2+1, i**2+2..
            
            二度哈希
                有n个哈希函数，h1发生冲突之后，使用h2, h3

        2.拉链法
            哈希表的每一个位置上维护一个链表，发生哈希冲突之后，冲突的元素
            被加到该位置链表的最后
            
            [0] ---> [] ---> [] ---> 
            [1] ---> [] ---> [] ...
            [2] ---> [] ---> [] ..
            [3] ---> [] ---> [] .
            [4] ---> [] ---> [] .
            [5] ---> [] ---> [] .
            [6] ---> [] ---> [] .
        



    哈希函数
        除法哈希
            h(k) = k % m

        乘法哈希
            h(k) = floor(m(A*key)%1)

        全域哈希:
            ...
            



"""



# 哈希表的实现 --- 拉链法

# 链表 --- 自己想不出来，借鉴一下
class LinkList:
    # 链表
    # 删除功能没做

    class Node:
        # 节点
        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator:
        # 迭代器类
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
            # 返回迭代器对象自己
            return self

    def __init__(self, iterable=None):
        """
        :param iterable: 列表类的可迭代对象
        """
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        # s = LinkList.Node(obj)
        s = self.Node(obj)
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
            # self 是类本身，因为已经是可以迭代了，所以可以使用 for 循环
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


# l = LinkList([1, 2, 3, 4])
# print(l) # <<1, 2, 3, 4>>



class Hashtable:

    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]
        # 使用拉链法，所以初始时，每个位置是一个空列表

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            # 重复插入
            print("Duplicated insert")
        else:
            # 这里的 append 方法是 链表方法
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        # 这里的 find 方法是 链表方法
        return self.T[i].find(k)


ht = Hashtable()

ht.insert(0)
ht.insert(1)
ht.insert(2)
ht.insert(102)


"""
链表的形式实现

<<0>>,<<1, 102>>,<<2>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,
<<>>,<<>>,<<>>,<<>>,<<>>,<<>>,<<>>


"""


print(",".join(map(str,ht.T)))



"""
哈希表的应用：

    1. 字典与集合都是通过哈希表来实现的
    2. 是用哈希表存储字典，通过哈希函数将字典的键映射为下标，
    3.如果发生哈希冲突，则通过拉链法或者开放寻址法解决



哈希表的应用 --- md5算法
    可以把任意数据映射为128位的哈希值
    
    检验文件一致性
    秒传
    
"""