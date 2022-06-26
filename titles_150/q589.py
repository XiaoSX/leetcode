#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/10
'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List
class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stack = []
        node = root
        while node is not None or len(stack) > 0:
            while node is not None:
                ans.append(node.val)
                if node.children is None or len(node.children) == 0:
                    node = None
                else:
                    cur = 1
                    stack.append([node, cur])  # 下次该访问的孩子节点
                    node = node.children[cur - 1]  # 当前节点

            if len(stack) > 0:
                node, child_id = stack[-1]
                if child_id >= len(node.children):
                    stack.pop(-1)
                    node = None
                else:
                    stack[-1][1] += 1
                    node = node.children[child_id]

        return ans