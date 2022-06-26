#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/12
'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List
class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        ans = []
        stack = []
        node = root
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append([node, 1])
                if node.children is not None and len(node.children) > 0:
                    node = node.children[0]
                else:
                    node = None
            node, child_num = stack[-1]
            if node.children is not None and len(node.children) > 0:
                if child_num >= len(node.children):
                    ans.append(node.val)
                    stack.pop(-1)
                    node = None
                else:
                    node = node.children[child_num]
                    stack[-1][1] += 1
            else:
                ans.append(node.val)
                stack.pop(-1)
                node = None

        return ans