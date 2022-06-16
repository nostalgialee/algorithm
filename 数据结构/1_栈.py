# -*- coding:utf-8 -*-
# @Time    : 2022/6/6 22:36
# @File    : 1_栈.py
# Author: lee


"""
栈：数据集合，可以理解为只能在一端进行插入或者删除操作的列表

    系统堆栈其实就是栈

特点：
    先进后出

概念：
    栈顶、栈底

栈的基本操作：
    进栈

    出栈

    取栈顶

"""


class Stack:

    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()


    def get_top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        if self.stack:
            return False
        return True


"""
栈的应用举例 --- 括号匹配问题
括号匹配问题：给一个字符串，其中包含小括号，中括号，大括号。求该字符串
中的括号是否匹配

遇到左半边的进展，遇到右半边的，与栈顶比较，匹配就出栈，最后循环完成后
判断栈是不是为空

"""

def _match_str(s):

    stack = Stack()
    match = {
        '}':'{',
        ']':'[',
        ')':'(',
    }

    for i in s:
        if i in ('(','{','['):
            stack.push(i)
        else:

            top_item = stack.get_top()
            if not top_item:
                return False

            if match[i] == top_item:
                stack.pop()
            else:
                return False

    if stack.is_empty():
        return True
    return False


s = '({{{[()()]}}})'
print(_match_str(s))

# def match_str(s):
#     stack = Stack()
#     match = {
#         "}": "{",
#         "]": "[",
#         ")": "("
#     }
#
#     for i in s:
#         # print("每个元素", i)
#         if i in ['(', '[', '{']:
#             stack.push(i)
#         else:
#             top_item = stack.get_top()
#             if not top_item:
#                 # print(1)
#                 return False
#
#             if match[i] == top_item:
#                 stack.pop()
#             else:
#                 # print(2)
#                 return False
#
#     print(stack.stack)
#     if stack.is_empty():
#         # print(3)
#         return True
#
#     # print(4)
#     return False

s = "{{({[]})}}"
# print(match_str(s))



