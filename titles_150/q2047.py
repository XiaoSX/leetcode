#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/27
'''

import re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = '((^|\s)([a-z]+(-[a-z]+)?([!,.])?|[!.,])(?=(\s|$)))'
        results = re.findall(pattern, sentence)
        return len(results)