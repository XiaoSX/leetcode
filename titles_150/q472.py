#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-28
'''
class Solution:
    def __init__(self):
        self.word = set()
        self.connect = set()
        self.dis_connect = set()

    def check_connect(self, text):
        n = len(text)
        if n <= 1:
            return False

        if text in self.connect:
            return True

        for i in range(1, n + 1):
            if text[:i] in self.word:
                if text[i:] != '':
                    if text[i:] in self.connect or text[i:] in self.word:
                        self.connect.add(text)
                        return True
                    if text[i:] in self.dis_connect:
                        continue
                    if self.check_connect(text[i:]):
                        self.connect.add(text)
                        return True
        self.dis_connect.add(text)
        return False

    def findAllConcatenatedWordsInADict(self, words):
        words = sorted(list(words), key=len)
        for w in words:
            if w == '':
                continue
            self.word.add(w)

        for w in words:
            if w == '':
                continue
            self.check_connect(w)

        connects = []
        for w in self.connect:
            if w in self.word:
                connects.append(w)
        return connects



