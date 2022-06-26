#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/13
'''

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        if m - n >= 2 or m - n <= -2:
            return False

        if m == n:
            cnt = 0
            for i in range(m):
                if first[i] != second[i]:
                    cnt += 1
            if cnt <= 1:
                return True
            return False

        while m > 0 and n > 0:
            if first[m - 1] != second[n - 1]:
                if m > n:
                    m -= 1
                elif m < n:
                    n -= 1
                else:
                    return False
            else:
                m -= 1
                n -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    first = "pale"
    second = "ple"
    test = []
    ans = []
    test.append([first, second])
    ans.append(True)

    first = "pale"
    second = "pple"
    test.append([first, second])
    ans.append(True)

    first = "ple"
    second = "pple"
    test.append([first, second])
    ans.append(True)

    first = "p"
    second = "pp"
    test.append([first, second])
    ans.append(True)

    first = ""
    second = ""
    test.append([first, second])
    ans.append(True)

    first = "teacher"
    second = "bleacher"
    test.append([first, second])
    ans.append(False)
    for i in range(len(test)):
        assert s.oneEditAway(*test[i]) == ans[i]