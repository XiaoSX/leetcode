#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-01
'''

class Solution:
    def hasCycle(self, head) -> bool:
        node = head
        first_p = node
        second_p = node
        while first_p and second_p and second_p.next:
            first_p = first_p.next
            second_p = second_p.next.next
            if first_p == second_p:
                return True
        return False
