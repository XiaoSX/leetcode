# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午4:27
# @Author  : RenMeng
# @File    : q93.py

class Solution:
    def searchNext(self, s, ans, total_ans):
        if s == '' and len(ans) == 4:
            total_ans.append(list(ans))
            return

        if s == '' and len(ans) != 4:
            return

        if s[0] == '0':
            ans.append(s[0])
            self.searchNext(s[1:], ans, total_ans)
            ans.pop()
        else:
            for i in range(min(len(s), 3)):
                if int(s[:i + 1]) > 255:
                    continue
                ans.append(s[:i + 1])
                self.searchNext(s[i + 1:], ans, total_ans)
                ans.pop()



    def restoreIpAddresses(self, s: str):
        ans = []
        total_ans = []
        if len(s) > 12:
            return []
        self.searchNext(s, ans, total_ans)
        return ['.'.join(x) for x in total_ans]