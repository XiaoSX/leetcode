#  -*-  coding: utf-8  -*-
from collections import defaultdict
def check(window, t_info):
    for k in t_info:
        if k not in window or window[k] < t_info[k]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_info = {}
        for ct in t:
            if ct not in t_info:
                t_info[ct] = 1
            else:
                t_info[ct] += 1

        window = defaultdict(lambda : 0)
        left = right = 0
        ml = left
        mr = right
        mix_dis = len(s) + 1

        while left < len(s):
            if right < len(s) and not check(window, t_info):
                window[s[right]] += 1
                right += 1
            elif not check(window, t_info):
                break
            else:
                if right - left < mix_dis:
                    mix_dis = right - left
                    ml = left
                    mr = right
                window[s[left]] -= 1
                left += 1
        return s[ml:mr]
