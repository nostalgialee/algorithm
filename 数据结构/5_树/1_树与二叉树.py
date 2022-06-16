# -*- coding:utf-8 -*-
# @Time    : 2022/6/10 12:54
# @File    : 1_树与二叉树.py
# Author: lee


"""
1.树是一种数据结构
2.树是一种可以递归定义的数据结构

树是由n个节点组成的集合
    如果 n == 0, 空树
    n > 0, 那存在1个节点作为树的根节点，其他
    节点可以分为m个集合，每个集合本身又是一棵树


"""


# 文件目录结构

class Node:

    def __init__(self, name, type):
        self.name = name
        self.type = type # dir or file
        self.parent = None
        self.children = []


class FileSystemTree:

    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name 以 / 结尾
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self,name):
        return self.now.children

    def cd(self, name):
        pass




