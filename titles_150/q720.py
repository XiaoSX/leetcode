#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/18
'''

from typing import List


class DictTreeNode:
    def __init__(self):
        self.isaword = False
        self.children = [None for _ in range(26)]

class Solution:
    def __init__(self):
        self.dict_tree = DictTreeNode()
        self.max_depth = 0
        self.ans = ''

    def createTree(self, words):
        for word in words:
            node = self.dict_tree
            for i in range(len(word)):
                if node.children[ord(word[i]) - ord('a')] is None:
                    new_node = DictTreeNode()
                    node.children[ord(word[i]) - ord('a')] = new_node
                node = node.children[ord(word[i]) - ord('a')]

            node.isaword = True


    def travelTree(self, node, connect, depth, paths):
        if connect and depth > self.max_depth:
            self.max_depth = depth
            self.ans = paths

        for i in range(26):
            ch = node.children[i]
            if ch is not None:
                self.travelTree(ch, connect & ch.isaword, depth + 1, paths + chr(ord('a') + i))



    def longestWord(self, words: List[str]) -> str:
        self.createTree(words)
        node = self.dict_tree
        self.travelTree(node, True, 0, '')
        return self.ans