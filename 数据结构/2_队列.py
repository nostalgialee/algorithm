# -*- coding:utf-8 -*-
# @Time    : 2022/6/7 11:16
# @File    : 2_队列.py
# Author: lee

"""
队列：是一个数据集合，仅允许在列表的一端进行插入
    另一端删除

    进行插入的一端是队尾，插入动作成为入队

    进行删除的一端是队头，删除动作成为出队

    队伍的性质：先进先出

"""

# 队列能否用队列简单实现：
    # 时间复杂度太高了


# 队列的实现：环形队列

"""
环形队列：当对尾指针 near == maxsize-1 时，再进一位到0

    1.队首指针前进1：front = (front+1) % maxsize
    2.对尾指针前进1：near = (near+1) % maxsize
    3.队空条件：near == front
    4.队满条件：(near+1) % maxsize == front

解释：
    维护 front 与 near 字段为了压入和弹出元素而已
    队满为了区分与队空，所以front 与 near 不重合
    只需要 (near + 1) % max_size == front 即可
    
    弹出元素仅需要 return queue[front],而不需要代码实现中
    删除此位置的数据，是需要当压入元素的时候用新元素在此位置上
    做替代 queue[near] = new_item 即可
    

"""



class Queue:

    def __init__(self,size=100):
        """
        :param size: 列表长度
        """
        self.queue = [0 for i in range(size)]
        self.max_size = 100

        self.front = 0 # 队收
        self.near = 0 # 队尾


    def push(self, item):
        if not self.is_full():
            self.near = (self.near+1) % self.max_size
            self.queue[self.near] = item
        else:
            raise IndexError('Queue is fulled.')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front+1) % self.max_size
            return self.queue[self.front]
        raise IndexError('Queue is empty.')
        # return None

    def is_empty(self):
        return self.near == self.front

    def is_full(self):
        # 牺牲一节空间，区分队空
        return (self.near+1) % self.max_size == self.front



class Queue1:

    def __init__(self, size=100):
        self.queue = [0 for i in range(self.size)]
        self.size = size
        self.front = 0
        self.rear = 0

    def push(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
        else:
            raise IndexError('queue is fulled.')

    def pop(self):
        if not self.is_empty():
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return item

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front















"""
双向队列
    两端都支持进队和出队的操作
        队首进队
        队首出队
        队尾进队
        队尾出队

"""


# 内置模块
from collections import deque
# 双向队列

q = deque()
q.append(1) # 队尾进队
q.popleft() # 队首出队

q.appendleft(1) # 队首进队
q.pop() # 队尾出队


# 实例 查看文件后几行
# 原因：
    # deque 第二个参数设置队列长度，若超出长度，队首出队

"""
1qwqw
2qwqw
3qwqwq
4qwqwer
5qwqw
6qwewtr
7rtryry
8qwqw

当队列长度为5的时候，假如在压入一个元素，那么
1qwqw
2qwqw
3qwqwq
4qwqwer
5qwqw

变成

2qwqw
3qwqwq
4qwqwer
5qwqw
6qwewtr

"""


def tail(n):
    with open('t.txt, r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='\n')

















