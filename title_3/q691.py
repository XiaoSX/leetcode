#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/14
'''

from typing import List
from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cnt = 0
        target_dict = Counter(target)

        while target != '':
            max_v = 0
            map_s = {}
            for word in stickers:
                v = 0
                d = {}
                w_dic = Counter(word)
                for t in target_dict:
                    if t in w_dic:
                        v += min(w_dic[t], target_dict[t])
                        d[t] = min(w_dic[t], target_dict[t])
                if v > max_v:
                    max_v = v
                    map_s = d

            if max_v == 0:
                return -1

            target = ''
            for t in target_dict:
                if t in map_s:
                    target_dict[t] -= map_s[t]
                if target_dict[t] > 0:
                    target += t

            cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    stickers = ["with", "example", "science"]
    target = "thehat"
    test.append([stickers, target])
    ans.append(3)

    stickers = ["notice", "possible"]
    target = "basicbasic"
    test.append([stickers, target])
    ans.append(-1)

    stickers = ["these", "guess", "about", "garden", "him"]
    target = "atomher"
    test.append([stickers, target])
    ans.append(3)
    for i in range(len(test)):
        assert s.minStickers(*test[i]) == ans[i]