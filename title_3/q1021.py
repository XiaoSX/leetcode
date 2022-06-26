#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/28
'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        cnt = 0
        tmp = ''
        for t in s:
            if t == '(':
                cnt += 1
            else:
                cnt -= 1
            tmp += t
            if cnt == 0:
                ans += tmp[1:-1]
                tmp = ''
        return ans

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    ori = "(()())(())"
    t = "()()()"
    test.append(ori)
    ans.append(t)
    ori = "(()())(())(()(()))"
    t = "()()()()(())"
    test.append(ori)
    ans.append(t)
    ori = '()()'
    t = ''
    test.append(ori)
    ans.append(t)
    for i in range(len(test)):
        assert s.removeOuterParentheses(test[i]) == ans[i]