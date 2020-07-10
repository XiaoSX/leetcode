#  -*-  coding: utf-8  -*-
def combine(dig, alp_maps):
    n = len(dig)

    if n == 0:
        return []

    if n == 1:
        return list(alp_maps[dig])

    ans = []
    alphas = alp_maps[dig[0]]
    for s in alphas:
        for p in combine(dig[1:], alp_maps):
            ans.append(s+p)
    return ans


class Solution:
    def letterCombinations(self, digits: str):
        alp_maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        return combine(digits, alp_maps)