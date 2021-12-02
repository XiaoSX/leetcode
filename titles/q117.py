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

        if root.left is None and root.right is None:
            return root

        tnode = root
        while tnode:
            bnode = None
            bnode_next = None
            while tnode:
                if tnode.left is None and tnode.right is None:
                    tnode = tnode.next
                    continue

                if tnode.left:
                    if bnode is None:
                        bnode = tnode.left
                        bnode_next = bnode
                    else:
                        bnode.next = tnode.left
                        bnode = bnode.next
                if tnode.right:
                    if bnode is None:
                        bnode = tnode.right
                        bnode_next = bnode
                    else:
                        bnode.next = tnode.right
                        bnode = bnode.next

                tnode = tnode.next
            tnode = bnode_next

        return root