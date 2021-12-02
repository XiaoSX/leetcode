# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 下午5:41
# @Author  : RenMeng
# @File    : q95.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from titles.tree import TreeNode

class Solution:
    # 递归结束条件
    def createTrees(self, pri_order, mid_order):
        if len(pri_order) == 0 and len(mid_order) == 0:
            return None
        root = TreeNode()
        root.val = pri_order[0]
        flag = -1
        for i in range(len(mid_order)):
            if mid_order[i] == root.val:
                flag = i
                break
        root.left = self.createTrees(pri_order[1:flag+1], mid_order[:flag])
        root.right = self.createTrees(pri_order[1+flag:], mid_order[1+flag:])
        return root

    # 层次遍历补None
    def levelTravel(self, root):
        if root is None:
            return []
        ans = [root.val]
        ans_node = [root]
        travel = root
        stack = [travel]
        while len(stack) > 0:
            travel = stack.pop(0)
            if travel.left is None and travel.right is None:
                continue

            if travel.left is not None:
                ans.append(travel.left.val)
                ans_node.append(travel.left)
                stack.append(travel.left)
            else:
                ans_node.append(None)
                ans.append(None)

            if travel.right is not None:
                ans.append(travel.right.val)
                ans_node.append(travel.right)
                stack.append(travel.right)
            else:
                ans_node.append(None)
                ans.append(None)

        n = len(ans) - 1
        while n >= 0:
            if ans[n] is not None:
                break
            ans.pop()
            ans_node.pop()
            n -= 1
        return ans_node

    # python list 引用和赋值的区别
    def generateTrees(self, n: int):
        f = [0 for _ in range(n + 1)]
        ans = [[] for _ in range(n + 1)]
        if n == 0:
            return []
        f[0] = 1
        ans[0] = [[]]
        for i in range(1, n + 1):
            # mid=[1, 2, ..., i]
            # f[i] += f[j - 1] * f[i - j]
            # j: 第i个节点在先序遍历中出现的次序
            pre_order_in_ans = []
            for j in range(1, n + 1):
                # 分别叠加左右节点的结果
                for l_node in ans[j - 1]:
                    pre = list(l_node) # 不动
                    pre += [i]
                    for r_node in ans[i - j]:
                        pre_right = [x + j - 1 for x in r_node] # 依次后延,前面已经遍历了j-1个元素
                        pre_order_in_ans.append(pre + pre_right)
                f[i] += f[j - 1] * f[i - j]
            ans[i] = list(pre_order_in_ans)

        result = []
        mid = [x for x in range(1, n + 1)]
        for pre in ans[n]:
            tree = self.createTrees(pre, mid)
            result.append(tree)
            # result.append(self.levelTravel(tree))
        return result