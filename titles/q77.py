#  -*-  coding: utf-8  -*-

def _combine(start, n, k, ans, final):
    if k == 0:
        final.append(ans[:])
        return

    for i in range(start, n):
        ans.append(i + 1)
        _combine(i + 1, n, k - 1, ans, final)
        ans.pop(-1)




class Solution:
    def combine(self, n: int, k: int):
        ans = []
        final = []
        _combine(0, n, k, ans, final)
        return final