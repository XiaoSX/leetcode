#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/30
'''

from titles.tree import TreeNode, createTrees
class Solution:
    def sumRootToLeaf(self, root) -> int:
        ans = 0

        def travel(node, path):
            nonlocal ans
            if node is None:
                return

            path.append(node.val)
            if node.left is None and node.right is None:
                num = 0
                for cur in path:
                    num *= 2
                    num += cur
                ans += num
                path.pop()
                return

            travel(node.left, path)
            travel(node.right, path)
            path.pop()

        travel(root, [])
        return ans

if __name__ == '__main__':
    s = Solution()
    node = createTrees([1, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1])
    s.sumRootToLeaf(node)