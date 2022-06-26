#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/10
'''

from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans