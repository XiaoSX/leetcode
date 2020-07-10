#  -*-  coding: utf-8  -*-
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return 0

        next = [0 for _ in range(n + 1)]
        next[0] = -1
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                if needle[:j] == needle[i - j:i]:
                    next[i] = j
                    break

        indexs = []
        si = 0
        pi = 0
        sn = len(haystack)
        while si < sn:
            # pi == n 不能在下一次收集，漏掉si=sn情况
            # if pi >= n:
            #     indexs.append(si - n)
            #     pi = next[n]

            if haystack[si] == needle[pi]:
                si += 1
                pi += 1
            elif next[pi] == -1:
                si += 1
            else:
                pi = next[pi]

            if pi >= n:
                indexs.append(si - n)
                pi = next[n]

        if len(indexs) > 0:
            return indexs[0]
        else:
            return -1