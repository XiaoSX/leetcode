#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/10
'''

class Solution:
    def largestInteger(self, num: int) -> int:
        arr = str(num)
        n = len(arr)
        odd = []
        even = []
        for i in range(n):
            if int(arr[i]) % 2 == 0:
                even.append(int(arr[i]))
            else:
                odd.append(int(arr[i]))
        odd = sorted(odd, reverse=True)
        even = sorted(even, reverse=True)
        oi = 0
        ei = 0
        ans = 0
        for i in range(len(arr)):
            if int(arr[i]) % 2 == 0:
                ans = ans * 10 + even[ei]
                ei += 1
            else:
                ans = ans * 10 + odd[oi]
                oi += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    num = 65875
    ans = s.largestInteger(num)
    print(ans)