#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/1
'''

class Solution:
    def majorityElement(self, nums) -> int:
        cnt = 0
        canditate = None
        for cur in nums:
            if cnt == 0:
                canditate = cur

            cnt += (1 if cur == canditate else -1)
        return canditate