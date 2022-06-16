# -*- coding:utf-8 -*-
# @Time    : 2022/6/1 23:15
# @File    : 2_递归.py
# Author: lee


# 递归
    # 自身调用
    # 有明确的结束条件

"""
大家都知道斐波那契数列，现在要求输入一个正整数 n ，
请你输出斐波那契数列的第 n 项。
斐波那契数列是一个满足
fib(x)  = 1                         x = 1,2
        = fib(x−1)+fib(x−2)         x >2
​
的数列
数据范围：1-40
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n) ，本题也有时间复杂度 O(logn)O(logn) 的解法

"""
# 递归做法
# 时间复杂度过高，导致通不过
def func(n):
    if n <= 2:
        return 1
    else:
        return func(n-1) + func(n-2)

print(func(6))

# 使用列表的做法
def Fibonacci(n):
    # write code here
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        f = [0, 1, 1]
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
        return f[-1]


"""
汉诺塔问题




"""