#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-18
'''

from collections import defaultdict
def findLadders(self, beginWord: str, endWord: str, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return []

    dictory = defaultdict(list)
    L = len(beginWord)

    # 准备过程  将字典中其中一位用*代替，建立map
    for word in wordList:
        for i in range(L):
            dictory[word[:i] + '*' + word[i + 1:]].append(word)

    ans = []

    queue_begin = [(beginWord, 1, [[beginWord]])]
    visited_begin = {beginWord: [[beginWord]]}

    minLevel = len(wordList) + 1  # 最大长度为字典长度+1

    while queue_begin:
        current_word, level, paths = queue_begin.pop(0)

        if level > minLevel: continue

        for i in range(L):
            tmp = current_word[:i] + '*' + current_word[i + 1:]
            for word in dictory[tmp]:
                if word == endWord:
                    # 拼接路径
                    for p in paths:
                        minLevel = level
                        ans.append(p + [endWord])

                elif word not in visited_begin:
                    new_paths = [p + [word] for p in paths]
                    visited_begin[current_word] = new_paths
                    queue_begin.append((word, level + 1, new_paths))

    return ans