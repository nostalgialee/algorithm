# -*- coding:utf-8 -*-
# @Time    : 2022/6/7 17:31
# @File    : 2_队列与栈的应用.py
# Author: lee


"""
迷宫问题
给一个二维列表，表示迷宫 0表示通道，1表示围墙
给出算法，求一条走出迷宫的路径
"""

lis = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

# 6.9 复习一下


dirs = [

    lambda x,y: (x+1, y),
    lambda x,y: (x-1, y),
    lambda x,y: (x, y+1),
    lambda x,y: (x, y-1)

]





# 深度优先 --- 回溯法
"""
思路：从一个节点开始，任意找一个能走的点，当找不到
能走的点的时候，退回上一个点寻找是否有其他方向的点
使用栈存储当前路径

简单来说：
不走回头路，拔剑四顾心茫然
每走一个节点，按照四个方向一致的顺序，上下左右，选择能走的路
不能走就退回上一个节点，选择下一个方向

所以使用 栈 来实现存储当前的路径
先进后出

路径未必最短

"""



# dirs = [
#
#     lambda x,y:(x+1,y),
#     lambda x,y:(x-1,y),
#     lambda x,y:(x,y+1),
#     lambda x,y:(x,y-1),
#
# ]
#
# def dfs(x1,y1,x2,y2):
#     """
#     :param x1: 起点
#     :param y1:
#     :param x2: 终点
#     :param y2:
#     :return:
#     """
#     stack = []
#
#     # 方向设置
#
#     stack.append((x1,y1)) # 起点存好
#     while stack: # 栈空说明无通路
#         curNode = stack[-1] # 当前节点
#         # 开始分方向了
#         if curNode[0] == x2 and curNode[1] == y2:
#             # 走到终点了
#             print(stack)
#             return True
#
#         for dir in dirs:
#             nextNode = dir(curNode[0], curNode[1])
#             if lis[nextNode[0]][nextNode[1]] == 0:
#                 # 能走
#                 stack.append(nextNode) # 路径存入
#                 # 足迹加入栈中
#
#                 lis[nextNode[0]][nextNode[1]] = 2
#                 # 走过的路 不走回头路
#                 break
#         else: # 路走不通
#             # 当前节点 curNode 的四个方向都不通，所以标记为2
#             lis[curNode[0]][curNode[1]] = 2
#             stack.pop() # 将 curNode 删除
#
#     else:
#         print("no way")
#         return False





# dfs(1,1,8,8)

# [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (6, 3), (6, 4), (6, 5), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8)]



# def maze_dfs(x1, y1, x2, y2):
#     stack = []
#     stack.append((x1, y1))
#     while stack:
#         item = stack[-1] # 当前节点
#         if item[0] == x2 and item[1] == y2:
#             return True
#         for dir in dirs:
#             next_item = dir(item[0], item[1])
#             if lis[next_item[0]][next_item[1]] == 0:
#                 # 可行
#                 stack.append(next_item)
#                 lis[next_item[0]][next_item[1]] = 2
#                 break
#         else:
#             lis[item[0]][item[1]] = 2
#             stack.pop()
#     else:
#         return False
#
# print(maze_dfs(1,1,8,8))



# 广度优先 --- 可以找到最优解
"""
思路：从一个节点开始，寻找所有接下来能继续走的点，
继续不断寻找，直到找到出口

队列存储当前正在考虑的点

简单来说就是


队首出队

队尾增加可行的节点




"""

from collections import deque


# def print_real_path(path):
#     curNode = path[-1]
#     real_path = []
#     while curNode[2] != -1: # curNode 不是起点
#         real_path.append(curNode[:2])
#         curNode = path[curNode[2]]
#
#     real_path.append(curNode[:2])
#     for i in real_path:
#         print(i)
#     return real_path[::-1]
#
#
# def maze_bfs(x1, y1, x2, y2):
#     q = deque()
#     q.append((x1, y1, -1)) # 谁带领起点的数字索引页加入其中
#     path = []
#
#     while q:
#         curNode = q.popleft() # 出队
#         path.append(curNode)
#         if curNode[0] == x2 and curNode[1] == y2:
#             # 终点了
#             print_real_path(path)
#             return True
#
#         for dir in dirs:
#             nextNode = dir(curNode[0], curNode[1])
#             if lis[nextNode[0]][nextNode[1]] == 0:
#                 # 判断四个方向，有路的话
#                 q.append((nextNode[0], nextNode[1], len(path)-1))
#                 lis[nextNode[0]][nextNode[1]] = 2 # 走过的路不走了
#
#     else:
#         print("没有路线")
#         return False
#
#
#
# maze_bfs(1,1,8,8)
#






# 路径最短的方法 --- 广度优先

from collections import deque


def print_path(path):
    curNode = path[-1]
    real_path = []
    while curNode[2] != -1:
        real_path.append(curNode[:2])
        curNode = path[curNode[2]]

    real_path.append(curNode[:2]) # 起点
    for i in real_path:
        print(i)
    return real_path[::-1]


def bfs(x1,y1,x2,y2):
    q = deque()
    q.append((x1, y1, -1))
    # 表示的是 点的坐标，
    # 以及哪个数字让它进到队列来的
    path = [] # 记录所有节点的出队的顺序
    while q:
        # 队空说明没有一条路

        # 队首出队
        curNode = q.popleft()
        # 当有元素出队的时候，就应该记录下来
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 重点
            print_path(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if lis[nextNode[0]][nextNode[1]] == 0:
                # 可以走通, 假如队列
                # 最终记录的时候我们记录的是一个三维的数据
                # 最后一位记录的是 curMode 在 path 中的序号
                q.append((nextNode[0], nextNode[1], len(path)-1))
                lis[nextNode[0]][nextNode[1]] = 2 # 记录每个节点已经走过

    else:
        print("没有路")
        return False



#
# bfs(1,1,8,8)

"""
(8, 8)
(8, 7)
(8, 6)
(8, 5)
(7, 5)
(6, 5)
(6, 4)
(6, 3)
(5, 3)
(5, 2)
(5, 1)
(4, 1)
(3, 1)
(2, 1)
(1, 1)
"""

def maze_dfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = [] # 存储将当前节点带入的节点
    while queue:

        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 重点
            print_path(path)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if lis[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path)-1))
                lis[nextNode[0]][nextNode[1]] = 2 # 记录每个节点已经走过


    else:
        print("no way")
        return False


