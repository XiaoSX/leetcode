# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 下午3:07
# @Author  : RenMeng
# @File    : tree.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTrees(pri_order, mid_order):
    if len(pri_order) == 0 and len(mid_order) == 0:
        return None
    root = TreeNode()
    root.val = pri_order[0]
    flag = -1
    for i in range(len(mid_order)):
        if mid_order[i] == root.val:
            flag = i
            break
    root.left = createTrees(pri_order[1:flag+1], mid_order[:flag])
    root.right = createTrees(pri_order[1+flag:], mid_order[1+flag:])
    return root

def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def inorderNonRecur(root):
    stacks = []
    node = root
    ans = []
    while node or len(stacks) > 0:
        while node:
            stacks.append(node)
            node = node.left
        node = stacks.pop(-1)
        ans.append(node.val)
        node = node.right
    return ans

def preorderNonRecur(root):
    stacks = []
    node = root
    ans = []
    while node or len(stacks) > 0:
        while node:
            stacks.append(node)
            ans.append(node.val)
            node = node.left
        node = stacks.pop(-1)
        node = node.right
    return ans

def lastorderNonRecur(root):
    if root is None:
        return []

    stacks = [root]
    node = root.left
    ans = []

    flag = 0
    while len(stacks) > 0:
        while node:
            stacks.append(node)
            node = node.left

        while node is None or flag == 1:
            if len(stacks) == 0:
                break

            if len(stacks) > 0 and stacks[-1].left == node:
                node = stacks[-1]
                node = node.right
                if node:
                    flag = 0
                    break
            if len(stacks) > 0 and stacks[-1].right == node:
                node = stacks.pop(-1)
                ans.append(node.val)
                flag = 1

    return ans


