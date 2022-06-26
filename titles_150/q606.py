#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/19
'''


class Solution:


    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ''
        if root is None:
            return ans

        stack = []
        node = root
        visit = []
        while node is not None or len(stack) > 0:
            while node is not None:
                ans += '(' + str(node.val)
                stack.append(node)
                visit.append(0)
                node = node.left
            node = stack[-1]
            flag = visit[-1]
            if flag == 1:
                ans += ')'
                stack.pop(-1)
                visit.pop(-1)
                node = None
            else:
                if node.left is None and node.right is not None:
                    ans += '()'
                node = node.right
                visit[-1] += 1

        return ans[1:-1]

    # def tree2str(self, root: Optional[TreeNode]) -> str:
    #     ans = ''
    #     if root is None:
    #         return ans
    #
    #     stack = [')', root, '(']
    #
    #     while len(stack) > 0:
    #         node = stack.pop(-1)
    #         if node in ['(', ')']:
    #             ans += node
    #             continue
    #         ans += str(node.val)
    #         if node.left is None and node.right is not None:
    #             ans += '()'
    #             stack.extend([")", node.right ,'('])
    #         else:
    #             if node.right is not None:
    #                 stack.extend([")", node.right , '('])
    #
    #             if node.left is not None:
    #                 stack.extend([")" , node.left, '('])
    #
    #     return ans[1:-1]

    # def tree2str(self, root: Optional[TreeNode]) -> str:
    #     ans = ''
    #     if root is None:
    #         return ans
    #
    #     ans += str(root.val)
    #
    #     # 左子树为空, 只有在右子树不是空时才遍历
    #     if root.left is None and root.right is not None:
    #         ans += '()(' + self.tree2str(root.right) + ')'
    #
    #     # 其他情况, 为空不需要遍历
    #     else:
    #         if root.left is not None:
    #             ans += '(' + self.tree2str(root.left) + ')'
    #
    #         if root.right is not None:
    #             ans += '(' + self.tree2str(root.right) + ')'
    #
    #     return ans

