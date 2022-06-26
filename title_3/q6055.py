#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/3
'''

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_hour, cur_min = [int(x) for x in current.split(':')]
        cor_hour, cor_min = [int(x) for x in correct.split(':')]
        if cur_hour == cor_hour and cur_min == cor_min:
            return 0

        ans = 0
        bases = [60, 15, 5, 1]
        i = 0
        while 1:
            nx_min = (cur_min + bases[i]) % 60
            nx_hour = (cur_min + bases[i]) // 60 + cur_hour
            if nx_hour < cor_hour or (nx_hour == cor_hour and nx_min < cor_min):
                ans += 1
                cur_hour, cur_min = nx_hour, nx_min
            elif nx_hour == cor_hour and nx_min == cor_min:
                return ans + 1
            else:
                i += 1


if __name__ == '__main__':
    s = Solution()
    test = [
            ["02:30", "02:59"], ["11:00","11:00"]]
    ans = [7, 0]
    for i in range(len(test)):
        assert s.convertTime(*test[i]) == ans[i]