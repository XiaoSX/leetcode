#  -*-  coding: utf-8  -*-
from collections import defaultdict
def sorf_alpha(s_arr):
    if len(s_arr) <= 1:
        return s_arr

    flag = s_arr[0]
    n = len(s_arr)
    low_i = 1
    high_i = n - 1
    while low_i <= high_i and low_i < n and high_i > 0:
        while low_i < n and s_arr[low_i] <= flag:
            low_i += 1

        while high_i > 0 and s_arr[high_i] >= flag:
            high_i -= 1

        if low_i < high_i:
            tmp = s_arr[low_i]
            s_arr[low_i] = s_arr[high_i]
            s_arr[high_i] = tmp

    s_arr[0] = s_arr[high_i]
    s_arr[high_i] = flag
    s_arr[:high_i] = sorf_alpha(s_arr[:high_i])
    s_arr[high_i + 1:] = sorf_alpha(s_arr[high_i + 1:])
    return s_arr



class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(lambda :[])
        for s in strs:
            ns = ''.join(sorf_alpha(list(s)))
            ans[ns].append(s)

        return list(ans.values())