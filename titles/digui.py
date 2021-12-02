#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-03
'''

def digui(graph, start, end):
    """
    返回从起点到终点的所有paths
    给出graph(dic type)， 含义为可达尾节点的头节点list，如graph[2] = [5, 6], 5-->2, 6-->2 可达
    start: 起点
    end: 终点
    :return:
    """
    res = [[end]]
    while res[0][0] != start:
        res = [[x] + i for i in res for x in graph[i[0]]]
    return res

if __name__ == '__main__':
    graph = {}
    graph[1] = [3]
    graph[2] = [5, 6]
    graph[3] = [0]
    graph[5] = [0]
    graph[6] = [0]
    graph[8] = [1, 2]
    print(digui(graph, 0, 8))