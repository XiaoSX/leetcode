#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/26
'''

from typing import List
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        j = len(self.blacklist) - 1
        self.end = n - 1
        self.cand = {}

        while self.end in self.blacklist:
            self.end -= 1
        self.cand[self.blacklist[j]] = self.end
        self.end -= 1
        j -= 1


        for num in range(n):
            if num not in self.blacklist:
                self.cand.append(num)
        self.cur = 0
        self.leng = len(self.cand)

    def pick(self) -> int:
        ans = self.cand[self.cur]
        self.cur += 1
        self.cur %= self.leng
        return ans

if __name__ == '__main__':
    s = Solution(7, [2, 3, 5])
    print(s.pick())
    print(s.pick())
    print(s.pick())
    print(s.pick())
    print(s.pick())
    print(s.pick())
    print(s.pick())



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()