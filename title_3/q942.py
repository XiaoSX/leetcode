#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/9
'''

from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low = 0
        high = n
        ans = []
        for i in range(n):
            if s[i] == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append('I')
    for i in range(len(test)):
        print(s.diStringMatch(test[i]))