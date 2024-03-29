#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-18
'''
from collections import defaultdict

# 双向广搜， 记录前驱
def findLadders(beginWord: str, endWord: str, wordList):
    if endWord not in wordList: return []
    # 定义了从头向后访问的集合，从尾向前访问的集合
    # 将wordlist转成了set，方便做减法运算。定义了默认首次访问方向为向后
    forward, backward, wordList, flag = {beginWord}, {endWord}, set(wordList), True
    # 所有字符，用于取代通配符，词长度， dic的key和value都是单词，value表示parent，或者说前置节点的意思。这里前置和后置的关系取决于距离beginword和endWord的距离
    # dic 或者说 指向的是离beginWord距离更近一层的节点。一种BFS的思想。
    letters, length, dic = 'abcdefghijklmnopqrstuvwxyz', len(beginWord), defaultdict(set)
    while forward:
        if len(forward) > len(backward):  # 当向后方向的长度大于向前方向长度时，反转以下三个值。 处理了困扰我n久的双向遍历时最大深度问题。。。
            forward, backward, flag = backward, forward, not flag

        wordList -= forward  # 从wordList移除将要遍历的forward ， 这样顺便将wordList当做了visited用，很棒的想法
        cur = set()
        for word in forward:
            # 这个循环我们将未插入dic的节点中，层数+1的节点全部插入dic。注意两个方向有区别。
            for i in range(length):
                left, right = word[:i], word[i + 1:]  # 老生常谈的通配符
                for l in letters:  # l类似我们之前用的通配符*
                    w = left + l + right  # 这个用letters处理，免去了构造一整个dict的过程，节约了很多代码和额外空间
                    if w in wordList:
                        cur.add(w)
                        if flag:
                            dic[w].add(word)  # 单词w可由word变化而来， 这里 w 比 word 离 beginWord远
                        else:
                            dic[word].add(w)  # 这个意思是逆序遍历时， 视为word可由w变化而来。这里 w 比word 离 endWord远，就是说离beginWord更近

        # 很酷炫的写法，利用了集合的交集 &计算出的是一个set。
        if cur & backward:  # 产生交集，最短路径找到
            # 用于生成全部路径，开始只放一个尾结点，通过dic不停找前置节点获取全路径
            # 这是一个二维数组， 第一维表示全部的路径，第二维表示该路径下的全部节点。
            res = [[endWord]]
            while res[0][0] != beginWord:  # 循环结束条件是刚添加进去的节点是beginWord
                # 这也是体现算法功底的代码。 遍历的是全部的路径， i代表的是其中一条路径，
                # i[0]代表的是每个路径的最前置节点，即第一个点。 注意我们每次都会清空之前的res，进行重新赋值。
                # 去除第一个点之后，通过dic[i[0]]获取前置节点x， 拼接路径：[x]+i
                # 这个代码干了这么多事，两层循环，但简洁优雅，又透露出算法功底，很佩服原作者！
                res = [[x] + i for i in res for x in dic[i[0]]]
            return res  # 产生交集就return,避免了我写的那个有5层又有6层的情况。很妙
        # 这个有一种指针向后移动的意味， 其实代表的是该层遍历结束，我们向后/向前移动一层。 类似常写的 cur = cur.next
        forward = cur
    return []