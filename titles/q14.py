#  -*-  coding: utf-8  -*-
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        if n == 0:
            return ''

        ans = list(strs[0])
        for text in strs[1:]:
            j = -1
            for i in range(min(len(text), len(ans))):
                if text[i] != ans[i]:
                    j = i
                    break
            if j == -1:
                ans = ans[:min(len(text), len(ans))]
            else:
                ans = ans[:j]


        return ''.join(ans)