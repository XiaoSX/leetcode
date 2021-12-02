#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-28
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        tnode = root
        while tnode:
            dummy = Node()
            pre = dummy
            while tnode:
                if tnode.left:
                    pre.next = tnode.left
                    pre = pre.next
                if tnode.right:
                    pre.next = tnode.right
                    pre = pre.next
                tnode = tnode.next
            tnode = dummy.next

        return root