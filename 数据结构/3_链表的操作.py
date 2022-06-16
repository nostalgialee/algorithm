# -*- coding:utf-8 -*-
# @Time    : 2022/6/9 16:32
# @File    : 3_链表的操作.py
# Author: lee

# 1.链表节点的插入
# 方法：
#
"""
    [1][next] --->  [2][next] --->  [3][next]
    [4][next]
    插入 4 到 1 后面

    curnode: [1][next]
    p: [4][next]


    step1:
        将 2 连接到 4 后面
        why: 不先连接 1 和 4? 链接完1和4后，找不到 2了
    step2:
        将 4 连接到 1 后面


    p.next = curnode.next
    curnode.next = p

"""



# 2.链表节点的删除

"""

    [1][next] --->  [2][next] --->  [3][next]

    curnode: [1][next]
    需要删除节点p：[2][next]

    p = curnode.next
    curnode.next = p.next
    del p
    



"""




# 3.双向链表
"""
双链表的每个节点存在两个指针，一个指向前面，一个指向后面

"""

class DoubleDirectNode:

    def __init__(self, item):
        self.item = item
        self.prior = None
        self.next = None



"""

双链表的节点插入

    [1][next] <--->  [2][next] <--->  [3][next]
    
    p = [4][next]
    curNode = [1][next]

    
    p.next = curNode.next
    curNode.next.prior = p
    curNode.next = p
    p.prior = curNode
    





双链表的节点删除
    [1][next] <--->  [2][next] <--->  [3][next]
    
    p = [2][next]
    curNode = [1][next]

    p = curNode.next
    curNode.next = p.next
    p.next.prior = curNode
    del p


"""




# 总结
"""
顺序表 与 链表

    1.按元素查找
    O(n) O(n) 
    
    2.按下标查找
    O(1) O(n) 

    3.在某元素后插入
    O(n) O(1)
   
    4.删除某元素
    O(n) O(1)


    1.插入删除操作明显快于顺序表
    2.链表的内存更加灵活的分配
        
    3.链表的链式存储对于树和图的结构有很大的启发性
    

"""
















