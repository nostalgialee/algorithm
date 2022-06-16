# -*- coding:utf-8 -*-
# @Time    : 2022/6/10 15:00
# @File    : 3_二叉搜索树.py
# Author: lee


# 二叉搜索树
"""
二叉搜索树是一颗二叉树，且满足性质：
    x 是树上的一个节点，
    若：
        y 是 x 左子树上的一个节点 y.key <= x.key
        y 是 x 左子树上的一个节点 y.key >= x.key

    其中序遍历为 有序的

"""


"""

                      17
                   /      \
                  /        \
                  5         35
                /  \       /  \
               /    \     /    \
              2      11  29    38
                    /                        
                   /
                  9
                 /
                /
               8

"""

# 二叉搜索树
class BiTreeNode:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class Bst:

    def __init__(self):
        self.root = None

    # 插入
    def insert(self, node, val):
        # 递归写法
        if not node:
            node = BiTreeNode(val)
        else:
            if val < node.data:
                node.lchild = self.insert(node.lchild, val)
                node.lchild.parent = node
            elif val > node.data:
                node.rchild = self.insert(node.rchild, val)
                node.rchild.parent = node
            else:
                pass
                # 一般要求key 不重复
        return node


    def insert_no_rec(self, val):
            # 非递归写法
            p = self.root
            if not p:  # 空树
                self.root = BiTreeNode(val)
                return self.root

            while True:
                if val < p.data:
                    if not p.lchild:  # 不存在 左子树
                        p.lchild = BiTreeNode(val)
                        p.lchild.parent = p
                        return
                    else:
                        p = p.lchild

                elif val > p.data:
                    if not p.rchild:
                        p.rchild = BiTreeNode(val)
                        p.rchild.parent = p
                        return
                    else:
                        p = p.rchild
                else:
                    # 一般要求key 不重复
                    return

    # 查找
    def find(self, node, val):
        # 递归版本
        if not node:
            return None
        if node.data < val:
            return self.find(node.rchild, val)
        elif node.data > val:
            return self.find(node.lchild, val)
        else:
            return node

    def find_no_rec(self, val):
        # 非递归版本
        p = self.root
        while p:
            if p.data > val:
                p = p.lchild
            elif p.data < val:
                p = p.rchild
            else:
                return p
        return None



    def __remove_node_1(self, node):
        # 1.叶子节点
        if not node.parent:
            # 没有父亲节点,即为 root 节点
            self.root = None
        if node == node.parent.lchild:
            # node 是左孩子
            node.parent.lchild = None
        else:
            node.parent.rchild = None


    def __remove_node_21(self, node):
        # node 只有一个左孩子
        if not node.parent:
            # 根节点
            # 左孩子做根节点
            self.root = node.lchild
            node.lchild.parent = None
        if node == node.parent.lchild:
            # node 是其父节点的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
            pass
        elif node == node.parent.rchild:
            # node 是其父节点的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # node 只有一个右节点
        if not node.parent:
            # 根节点
            self.root = node.rchild
            node.rchild.parent = None
        if node == node.parent.lchild:
            # node 是其父节点的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
            pass
        elif node == node.parent.rchild:
            # node 是其父节点的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent


    def delete(self, val):
        # 比较复杂
        if not self.root:
            return
        node = self.find_no_rec(val)
        if not node:
            return False

        # 1.叶子节点
        if not node.lchild and not node.rchild:
            self.__remove_node_1(node)


        # 删除比较复杂
        # 2.要删除的只有一个孩子节点：将此节点的父亲与孩子链接，然后删除此节点
        elif not node.rchild:
            # 只有一个左孩子 要是没有左孩子，会执行上面的条件
            self.__remove_node_21(node)
        elif not node.lchild:
            self.__remove_node_22(node)


        # 3.有两个孩子：将其右子树的最小节点删除，并替换此节点
        else:
            min_right_node = node.rchild
            while min_right_node.rchild:
                min_right_node = min_right_node.rchild

            # 这里也是比较复杂的。

            node.data = min_right_node.data # 数字更新，然后直接删除最小右节点
            # 删除 min_right_node 的时候有两种情况，叶子节点，还是有一个孩子节点
            if min_right_node.lchild:
                self.__remove_node_21(min_right_node)
            elif not min_right_node.lchild and not min_right_node.rchild:
                self.__remove_node_1(min_right_node)
