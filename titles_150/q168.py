#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/31
'''
import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        map_info = list(string.ascii_uppercase)
        ans = []
        while columnNumber != 0:
            columnNumber -= 1
            ans.append(columnNumber % 26)
            columnNumber = columnNumber // 26
        ans = [map_info[i] for i in ans]
        ans = ans[::-1]
        return ''.join(ans)