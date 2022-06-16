# -*- coding:utf-8 -*-
# @Time    : 2022/6/13 22:51
# @File    : 1_贪心算法.py
# Author: lee


"""
贪心算法：
    对问题求解的时候，总是做出在当前看来是最好的选择
    换句话说，不从整体的最优上加以考虑，他所做出的是在
    某种意义上的局部最优解


    贪心算法不能保证得到最优解，但是在某些问题上，贪心算法的解就是
    最优解，要学会判断一个问题是否能使用贪心算法


"""


"""
找零问题：
老板要找零n元钱，钱币的面额有 100，50，20，5，1
如何值得找零是的所需钱币的数量最少

思路：就是面值越大，一定是数量越少

"""

def change_money(money):
    """
    :param money: 需要找的钱
    :return:
    """
    cash = [100, 50, 20, 5, 1]
    res = []

    for i in cash:
        if money == 0:
            return res
        if i > money:
            continue
        count = money // i
        money = money % i
        res.extend([i] * count)
    return res

# print(change_money(376))








"""
背包问题：
一个小偷在某个商店发现了有n个商品，第i个商品价值vi元，
重wi千克，他希望拿走的价值尽量高，但是背包中只能容纳w千克的东西
他应该拿走哪些商品？

    0-1背包：
        对于一个商品，小偷要么全部拿走，要么留下，不能只拿走一部分
        贪心算法 不能 在这个问题在中得到最优解
        需要使用动态规划解决得到最优解
        
    分数背包：
        对于一个商品，小偷可以拿走其中的一部分
        贪心算法 能 在这个问题在中得到最优解
        
        
"""

# 分数背包 --- 金砂
stuff = [(60, 10), (100, 20), (120, 30)]
# (价值, 重量(有多少))


def fractional_backpack(stuff, total_weight):
    """
    :param stuff:  商品
    :param weight: 规定总重量
    :return:
    """
    # 商品的单价排序
    stuff.sort(key=lambda x:x[0]/x[1], reverse=True)
    print(stuff)
    m = [[value, 0] for value, sand_weight in stuff] # 拿走的东西
    total_value = 0

    for ind, (value, weight) in enumerate(stuff):

        if total_weight >= weight:
            # 此时包的容量 大于 当前商品存在的重量
            m[ind][1] = 1 * weight
            total_value += value
            total_weight -= weight
        else:
            # 此时包不够装下 这件商品的所有了
            m[ind][1] = total_weight
            total_value += value * (total_weight/weight)
            total_weight = 0
            break

    return m, total_value


# print(fractional_backpack(stuff, 50))




"""
拼接最大数字的问题
有 n 个非负整数，将其按照字符串拼接的方式拼接位一个整数，如何拼接可以
使的得到的整数最大

ex:
 32 94 128 1286 6 71
 
 ===> 94716321286128


所有的数字，从最高位置开始比，


"""

li = [32, 94, 128, 1286, 6, 71]

def number_join(li):
    # 冒泡排序也是可以的
    # 前后两个元素比较， x+y y+x 拼成的大小

    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if int(str(li[j]) + str(li[j+1])) < int(str(li[j+1]) + str(li[j])):
                li[j], li[j+1] = li[j+1], li[j]

    # print(''.join(li))
    print(''.join(map(str,li)))
    return li


# print(number_join(li))




"""
活动选择问题：

假设有 n 个活动，这些活动要占用同一片场地，而场地在某时刻只能供一个活动使用
每个活动都有一个开始时间 si 和 结束时间 fi, 题目中以整数表示
表示活动在 [si, fi)区间占用场地


问：安排那些活动能够是该改场地举办的活动个数最多？

i   1   2   3   4   5   6   7   8   9   10  11
si  1   3   0   5   3   5   6   8   8   2   12
fi  4   5   6   7   9   9   10  11  12  14  16




思路：
    最先结束的活动一定是最优解
    why:
        证明：假设a是所有活动中最先结束的活动
        b是所有最优解中最先活动的活动
        
        证明 a==b
        
    证：
        if a == b, 结论成立
        if a != b, b的结束时间一定是晚于a的，此时用a替换
        b，a依旧不与最优解中的其他的活动时间重叠，
        所以a也是最优解中最先结束的货送

"""


li = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
      (5, 9), (6, 10), (8, 11), (8, 12), (2, 14),
      (12, 16)]
# 保证活动已经是按照结束时间排序完毕了
# 保证了最先结束的活动一定是最优解中的活动
def activity_selection(li):
    res = [li[0]]
    for i in range(1, len(li)):
        if li[i][0] >= res[-1][1]:
            # 当前进行判断的活动的开始时间
            # 大于等于等于res中最后一个活动的结束时间
            res.append(li[i])
    return res

print(activity_selection(li))



"""
总结贪心算法
    一般是最优解问题，
    但是不是所有的最优解问题都可以是用贪心算法
    遇到上述问题，可以考虑能否使用贪心算法


"""