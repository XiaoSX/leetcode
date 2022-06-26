#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/31
'''

import numpy as np
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        ans = 1
        for cur in range(int(np.sqrt(num)), 1, -1):
            if num % cur == 0:
                ans += cur
                ans += num // cur
        return ans == num