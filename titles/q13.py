#  -*-  coding: utf-8  -*-
class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

        pre_v = 2000
        ans = 0
        for i in range(len(s)):
            if pre_v >= _map[s[i]]:
                ans += 0 if pre_v == 2000 else pre_v
            else:
                ans -= pre_v
            pre_v = _map[s[i]]

        if len(s) >= 1:
            ans += _map[s[-1]]
        return ans
