#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/3
'''

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def toInt(s):
            hour, min = s.split(':')
            hour = int(hour)
            min = int(min)
            return hour * 60 + min

        a = toInt(current)
        b = toInt(correct)
        c = b - a
        ans = c // 60
        c %= 60
        ans += c // 15
        c %= 15
        ans += c // 5
        c %= 5
        ans += c
        return ans


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    current = "02:30"
    correct = "04:35"
    test.append([current, correct])
    ans.append(3)
    for i in range(len(test)):
        assert s.convertTime(*test[i]) == ans[i]