# -*- coding:utf-8 -*-
# @Time    : 2022/6/9 14:24
# @File    : 3_链表.py
# Author: lee


"""
链表：是由一系列节点组成的元素集合，每个节点包含两部分
数据域 item 和指向下一个节点和指针 next,
通过节点之间的相互连接，最终串成一个链表

"""

"""
head --> [value][next] --->  [value][next] --->  [value][next] 

"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None



a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

print(a.next.next.item)


# 二、创建链表

# 1.头插法 -- head 指针

"""
    head
    
    [2][next] --->  [1][next]

    [3][next] --->  [2][next] --->  [1][next]

    head 指向3 

"""




# 1.尾插法 head 和 tail 指针

"""
    head            tail

    [1][next] --->  [2][next]

    [1][next] --->  [2][next] --->  [1][next]

    tail 指向 3                      tail

"""



def create_linklist_tail(lis):
    head = lis[0]
    tail = head
    for item in lis[1:]:
        node = Node(item)
        tail.next = node
        tail = node
    return head


# def create_linklist_tail(li):
#     head = li[0] # 设置头节点
#     tail = head  # 此时尾节点与头节点为一个
#     for element in li[1:]:
#         # 开始
#         node = Node(element)
#         tail.next = node
#         tail = node
#     return head