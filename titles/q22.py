#  -*-  coding: utf-8  -*-

def deep_search(l_depth, r_depth, ans, n, final_ans):
    if l_depth == n:
        final_ans.append(''.join(ans[:] + [')'] * (n - r_depth)))
        return

    for next_p in ['(', ')']:
        if l_depth == r_depth and next_p == ')':
            continue
        ans.append(next_p)
        if next_p == '(':
            deep_search(l_depth + 1, r_depth, ans, n, final_ans)
        else:
            deep_search(l_depth, r_depth + 1, ans, n, final_ans)
        ans.pop(-1)
    return

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        final_ans = []

        deep_search(0, 0, ans, n, final_ans)
        return final_ans
