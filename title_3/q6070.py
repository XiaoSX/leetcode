#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/17
'''


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            t = ''
            for i in range(0, len(s), k):
                ans = 0
                for j in s[i:i+k]:
                    ans += int(j)
                t += str(ans)
            s = t

        return s



if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    t = "11111222223"
    k = 3
    test.append([t, k])
    ans.append('135')

    t = "00000000"
    k = 3
    test.append([t, k])
    ans.append('000')
    for i in range(len(test)):
        assert s.digitSum(*test[i]) == ans[i]
