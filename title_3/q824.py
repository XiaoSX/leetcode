#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/21
'''


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        ans = ''
        for i in range(len(words)):
            suffix = 'a' * (i + 1)
            word = words[i]
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                ans += word + 'ma' + suffix
            else:
                ans += word[1:] + word[0] + 'ma' + suffix
            ans += ' '

        return ans[:-1]