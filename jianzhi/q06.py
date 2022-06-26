#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/8
'''

from typing import List
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        return self.reversePrint(head.next) + [head.val]
