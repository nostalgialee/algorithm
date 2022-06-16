# -*- coding:utf-8 -*-
# @Time    : 2022/6/10 14:15
# @File    : 2_二叉树.py
# Author: lee


# 二叉树
"""
二叉树的链式存储：将二叉树的节点定义为一个对象，节点之间通过
类似于链表的连接方式来连接

"""

# 节点定义
class BiTreeNode:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


E = BiTreeNode("E")
A = BiTreeNode("A")
G = BiTreeNode("G")
C = BiTreeNode("C")
F = BiTreeNode("F")
B = BiTreeNode("B")
D = BiTreeNode("D")

E.lchild = A
E.rchild = G
A.rchild = C
G.rchild = F
C.lchild = B
C.rchild = D


# 二、二叉树的遍历
"""
                 E
                / \
               /   \
              A     G
               \     \
                \     \
                 C     F
                / \
               /   \
              B     D


    # 前中后 表示的是 root 的相对位置
    遍历方式：
        前序遍历
        先root,然后左孩子(左孩子的左孩子右孩子)、右孩子
            E A C B D G F 
                
        中序遍历
        先左孩子 再root 右孩子
            A B C D E G F 

        
        后序遍历
            B D C A F G E 
        
        层次遍历(一眼看出)
            E A G C F B D
            

"""

# 非递归的方式还没有学


# 前序遍历
def preread(root):
    "递归法"
    if root:
        print(root.data, end=' ')
        preread(root.lchild)
        preread(root.rchild)
# preread(E)





# 中序遍历
def midread(root):
    "递归法"
    if root:
        midread(root.lchild)
        print(root.data, end=' ')
        midread(root.rchild)
# midread(E)




# 后序遍历
def lastread(root):
    "递归法"
    if root:
        lastread(root.lchild)
        lastread(root.rchild)
        print(root.data, end=' ')

# lastread(E)




# 层次遍历
# 使用队列 bfs

from collections import deque

def levelread(root):
    q = deque()
    q.append(root)
    res = []
    while q:
        node = q.popleft()
        res.append(node.data)
        try:
            lchild = node.lchild
            rchild = node.rchild
        except:
            raise TypeError('有点问题')
        if lchild:
            q.append(lchild)
        if rchild:
            q.append(rchild)

    print(res)
    return res

levelread(E)
# E    A   G   C   F   B   D
# ['E', 'A', 'G', 'C', 'F', 'B', 'D']




