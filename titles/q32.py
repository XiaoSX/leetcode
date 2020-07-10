#  -*-  coding: utf-8  -*-

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        cnt = [0 for _ in range(n)]
        for i in range(n):
            if s[i] == ')' and i == 0:
                continue
            elif s[i] == ')':
                # 检查是否有匹配的左括号，有的话则累加"(()()())"
                if s[i - 1] == ')':
                    p = i - 1 - cnt[i - 1]
                    if p < 0 or s[p] == ')':
                        cnt[i] = 0
                    elif p == 0:
                        cnt[i] = cnt[i - 1] + 2
                    else:
                        cnt[i] = cnt[i - 1] + 2 + cnt[p - 1]
                # 有效累加"()()"
                else:
                    if i == 1:
                        cnt[i] = 2
                    else:
                        cnt[i] = cnt[i - 2] + 2
            else:
                pass
        return max(cnt)