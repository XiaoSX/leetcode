#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-02
'''

from collections import defaultdict
# 广搜不需要visit数组
def min_dis(vs, ve, edges, word_dic):
    n = len(word_dic)
    dis = [float('inf')] * n
    queues = [vs]
    dis[vs] = 0
    while len(queues) > 0:
        cur_node = queues.pop(0)
        if cur_node == ve:
            return dis[cur_node]

        for i in edges[cur_node]:
            if dis[i] == float('inf'):
                dis[i] = dis[cur_node] + 1
                queues.append(i)
    # 不可达
    return dis[ve]


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        n = len(wordList)
        word_len = len(beginWord)
        word_dic = {}
        edges = defaultdict(list)
        wi = 0
        for word in wordList:
            word_dic[word] = wi
            wi += 1
            for i in range(word_len):
                new_word = list(word)
                new_word[i] = '*'
                new_word = ''.join(new_word)
                if new_word not in word_dic:
                    word_dic[new_word] = wi
                    wi += 1
                edges[word_dic[word]].append(word_dic[new_word])
                edges[word_dic[new_word]].append(word_dic[word])

        if endWord not in word_dic:
            return 0
        if beginWord not in word_dic:
            word_dic[beginWord] = wi
            wi += 1
            for i in range(word_len):
                new_word = list(beginWord)
                new_word[i] = '*'
                new_word = ''.join(new_word)
                if new_word not in word_dic:
                    word_dic[new_word] = wi
                    wi += 1
                edges[word_dic[beginWord]].append(word_dic[new_word])
                edges[word_dic[new_word]].append(word_dic[beginWord])

        start = word_dic[beginWord]
        end = word_dic[endWord]
        min_v = min_dis(start, end, edges, word_dic)

        if min_v == float('inf'):
            return 0
        else:
            return min_v // 2 + 1