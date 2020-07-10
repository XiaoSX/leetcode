#  -*-  coding: utf-8  -*-
class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        counts = 1 << n
        # 0 padding, 8 long
        _format = '0' + str(n) + 'b'
        for i in range(counts):
            _index = format(i, _format)
            ans.append([nums[subi] for subi in range(n) if _index[subi] == '1'])
        return ans