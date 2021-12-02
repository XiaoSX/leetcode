#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-18
'''
from collections import defaultdict

def findPath(vs, ve, word_dic, edges):
    n = len(word_dic)
    queue = [vs]
    dis = [float('inf')] * n
    dis[vs] = 0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node == ve:
            return dis[cur_node]
        for i in edges[cur_node]:
            if dis[i] == float('inf'):
                queue.append(i)
                dis[i] = dis[cur_node] + 1

    return dis[ve]

# 单向dfs超时
# 双向dfs， visit数组问题（因为遍历的结束条件是vs=ve， 两次visit同一个节点）， 答案组装的时候step=2的细节问题
def genPath(vs, ve, edges, depth, total_paths, front_path, back_path, dic_word,
            front_visit, back_visit):
    if vs == ve:
        _path = []
        new_path = front_path + [back_path[p] for p in range(len(back_path) - 1, -1, -1)][1:]
        for i in range(0, len(new_path), 2):
            _path.append(dic_word[new_path[i]])
        total_paths.append(_path)
        return

    if depth == 0:
        return

    for i in edges[vs]:
        if front_visit[i] == 0:
            front_path.append(i)
            front_visit[i] = 1
            for j in edges[ve]:
                if back_visit[j] == 0:
                    back_path.append(j)
                    back_visit[j] = 1
                    genPath(i, j, edges, depth - 2 , total_paths, front_path, back_path, dic_word, front_visit,
                            back_visit)
                    back_visit[j] = 0
                    back_path.pop(-1)
            front_path.pop(-1)
            front_visit[i] = 0
    return



class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        word_dic = {}
        word_len = len(beginWord)
        wi = 0
        edges = defaultdict(list)
        for word in wordList:
            if word not in word_dic:
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
            return []
        if beginWord not in word_dic:
            word = beginWord
            if word not in word_dic:
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

        depth = findPath(word_dic[beginWord], word_dic[endWord], word_dic, edges)
        if depth == float('inf'):
            return []
        else:
            total_path = []
            dic_word = {v:k for k, v in word_dic.items()}
            front_path = [word_dic[beginWord]]
            back_path = [word_dic[endWord]]
            front_visit = [0 for _ in range(len(word_dic))]
            back_visit = [0 for _ in range(len(word_dic))]
            front_visit[word_dic[beginWord]] = 1
            back_visit[word_dic[endWord]] = 1

            genPath(word_dic[beginWord], word_dic[endWord], edges, depth, total_path, front_path, back_path,
                    dic_word, front_visit, back_visit)
            return total_path