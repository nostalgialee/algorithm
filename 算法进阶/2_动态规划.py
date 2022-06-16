# -*- coding:utf-8 -*-
# @Time    : 2022/6/13 22:59
# @File    : 2_动态规划.py
# Author: lee


"""
斐波那契数列：
    fn = fn-1 + fn-2
    使用递归与非递归来求解斐波那数列的第n项的值

"""
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    return fibnacci(n-1) + fibnacci(n-2)

# print(fibnacci(10))


# 动态规划
def fibnacci_no_recurision(n):
    # 非递归方法
    f = [1,1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)

        return f[-1]

# print(fibnacci_no_recurision(10))


"""
动态规划
    1.最优子结构 -- 递推式
    2.重复子问题

"""


"""
问题1：钢条切割问题：
    某公司出售钢条，出售价格与钢条之间的关系如下表：
    
长度  1   2   3   4   5   6   7   8   9   10
价格  1   5   8   9   10  17  17  20  24  30

现有一段长度为n的钢条和上面的价格表，求切割钢条的方案
使得总收益最大

首先要求出 --- 递推式
思考：
长度为n的钢条的不同切割方案有几种

2 ** (n-1)
why:
    因为 长度为n的钢条有n-1个可以切割的地方，
    每个地方又有两种可能行，选择 切或者不切
    所以 2 ** (n-1) --- 但是也有重复的情况，
    例如：长度为4的钢条，可以切割为 112和211、121的情况
    这三种情况其实是重复的
    上述列举的切割方法的时候，假如n的长度很大的时候不方便全部列举
    
    所以需要，得到递推式，进行计算

长度 i        1   2   3   4    5   6   7   8   9   10
最大获益 pi    1   5   8   10  13  17  18   22  25  30

所以递推式：
设长度为n的钢条切割之后最优收益值为 rn, 则递推式为：
    rn = max(pn, r1+rn-1, r2+rn-2, ...rn-1+r1)
    pn 表示不切割，
    其他 n-1个参数分别表示另外 n-1 种不同切割方案
    将钢条分别切割为 i 和 n-i 两段
    
    
    简化为：
    rn = max(pi+rn-i)  1<=i<=n
    
"""




p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 25, 30]
# 每个元素为 长度 为 i 的时候，利润（不切割）

# 自顶向下的实现 --- 递归实现

def _cut(p, n):
    # 递归版本
    # 第1种
    """
    :param n: 钢条长度
    :return:
    """

    if n == 0:
        return 0
    else:
        res = p[n] # 不切割的最大值
        for i in range(1, n):
            res = max(res, _cut(p, i) + _cut(p, n-i))
    return res

# print(_cut(p, 9))


def _cut1(p, n):
    # 递归版本
    # 第2种
    """
    :param n: 钢条长度
    :return:
    """
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + _cut1(p, n-i))
    return res
#
# print(_cut1(p, 9))



"""
钢条切割问题 --- 动态规划解法：
    递归算大由于重复求解相同子问题，效率极低
    动态规划的思想：
        每个子问题只求解一次，保存求解结果
        之后需要此问题时，只需查找保存的结果
    
"""


# 自底向上的实现 O(n^2)
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 25, 30]
# 每个元素为 长度 为 i 的时候，利润（不切割）
def _cut2(p, n):
    r = [0]
    for i in range(1, n+1): # 循环得到 n 的各种长度
        max_value = 0
        for j in range(1, i+1): # 切分 长度为 i 的钢条
            max_value = max(max_value, p[j] + r[i-j])
        r.append(max_value)
    return r

# print(_cut2(p, 9))
# 最大获益 pi    1   5   8   10  13  17  18   22  25  30




# 同时给出切割方案的
def _cut22(p, n):
    r_value = [0]
    r_length = [0]
    for i in range(1, n+1): # 循环得到 n 的各种长度
        max_value = 0  # 切割的价值最大值
        max_length = 0 # 价值最大的切割方法 左边不切割部分的长度
        for j in range(1, i+1): # 切分 长度为 i 的钢条
            if p[j] + r_value[i-j] > max_value:
                max_value =  p[j] + r_value[i-j]
                max_length = j
        r_length.append(max_length)
        r_value.append(max_value)

    return r_length, r_value


def get_cut_result(p, n):
    r_length, r_value = _cut22(p, n)
    ans = []
    while n > 0:
        ans.append(r_length[n])
        n -= r_length[n]
    return ans

print(get_cut_result(p, 9))



"""
最长公共子序列

一个序列的子序列是在该序列中删去若干元素后得到的序列
ex: 
    ABCD 和 BDF 都是 ABCDEFG 的子序列

最长公共子序列 LCS 问题：
    给定两个序列x和y，求x和y长度最大的公共子序列
    ex:
        x = ABBCBDE 
        y = DBBCDB 
        LCS(x, y ) = BBCD
        
    应用场景：字符串相似度比对
    
    公共序列有很多，题目要求最长的
   
   
   
   
   
 思路：
    关键点在于递推式：
    
    LCS 最优子结构：令
        x = (x1, x2, x3 ...xm)
        y = (y1, y2, y3 ...yn)
        z = (z1, z2, z3 ...zk) 为 x, y 的任意一个LCS
    
    1.xm == yn   则，zk = xm = yn,且zk-1是xm-1 yn-1的一个LCS
    2.xm != yn   则，zk != xm, 意味着 z 是xm-1 和 y 的一个LCS
    3.xm != yn   则，zk != yn, 意味着 z 是x 和 yn-1 的一个LCS
    
   ex: 
        1. abcd 与 abd 的LCS 是 abd， 所以 ab 也是 abc 与 ab 的LCS (结论1)
        2. abc 与 ab 的LCS 是 ab，所以 ab 是 ab 和 ab 的 LCS (结论2)
 
   


    递推式：
    
    c[i,j]  = 0                              i==0 or j == 0
            = c[i-1,j-1] + 1                 i,j > 0 and i == j
            = max(c[i,j-1], c[i-1,j])        i,j > 0 and i == j
    
    c[i,j] 表示最长公共子序列的长度            


"""

def lcs_length(str1, str2):
    res = []
    path = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    trace = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                path[i][j] = path[i-1][j-1] + 1
                trace[i][j] = 1 # 表示来自左对角线
            else:
                if path[i-1][j] > path[i][j-1]:
                    path[i][j] = path[i-1][j]
                    trace[i][j] = 2 # 来自上面
                else:
                    path[i][j] = path[i][j-1]
                    trace[i][j] = 3 # 来自左边

    return path[len(str1)][len(str2)], trace


def trace(str1, str2):
    # 回溯
    _len, trace = lcs_length(str1, str2)
    i = len(str1)
    j = len(str2)
    res = []
    while i > 0 and j > 0:
        if trace[i][j] == 1: # 来自左上方
            res.append(str1[i-1]) # 上面就是 str1[i-1] == str2[j-1]
            i -= 1
            j -= 1
        elif trace[i][j] == 2:  # 来自上方
            i -= 1
        else: # 左边
            j -= 1
    return ''.join(reversed(res))

print(trace('abcbdab', 'bdcaba'))


# [
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 1, 1],
# [0, 1, 1, 1, 1, 2, 2],
# [0, 1, 1, 2, 2, 2, 2],
# [0, 1, 1, 2, 2, 3, 3],
# [0, 1, 2, 2, 2, 3, 3],
# [0, 1, 2, 2, 3, 3, 4],
# [0, 1, 2, 2, 3, 4, 4]
# ]
