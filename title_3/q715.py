#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/20
'''

# list 插入和删除不友好, 可以维护数据有序
# 堆, 插入删除log(n), 排序nlog(n), 堆不维护数据有序
# hash, 插入, 删除十分友好, 维护有序比较难?
# 有序, 支持动态插入, 删除
# 线段树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.flag = 0
        self.left = left
        self.right = right


class RangeModule:

    def __init__(self):
        self.root = TreeNode(val=0)
        self.start = 1
        self.end = 1000000000


    def _pushDown(self, node, left_sum, right_sum):
        if node.flag == 0:
            return

        node.flag = 0
        if node.left is None:
            node.left = TreeNode()
        if node.right is None:
            node.right = TreeNode()

        if node.val == 0:
            node.left.val = 0
            node.right.val = 0
        else:
            node.left.val = left_sum
            node.right.val = right_sum

        node.left.flag = 1
        node.right.flag = 1


    # 树没建的时候, 防止空节点, 新建的节点一定要挂到当前树上
    # 树的value = left.value + right.value, 每次value都要重新赋0
    # 查询点的更新 min(), max()
    def update(self, node, start, end, left, right, val):
        if left <= start and end <= right:
            node.val = val * (end - start + 1)
            node.flag = 1
            node.left = None
            node.right = None
            return

        mid = (start + end) // 2
        # 来自上次的记录更新
        self._pushDown(node, mid - start + 1, end - mid)

        # 当前更新
        if left <= mid:
            if node.left is None:
                node.left = TreeNode(val=0)

            self.update(node.left, start, mid, left, min(mid, right), val)

        if right > mid:
            if node.right is None:
                node.right = TreeNode(val=0)

            self.update(node.right, mid + 1, end, max(mid + 1, left), right, val)

        node.val = 0
        if node.left is not None:
            node.val += node.left.val

        if node.right is not None:
            node.val += node.right.val
        return

    def query(self, node, start, end, left, right):
        # 查询不存在的区间
        if node is None:
            return 0

        if left <= start and end <= right:
            return node.val

        ans = 0
        mid = (start + end) // 2
        # 来自上次的记录更新
        self._pushDown(node, mid - start + 1, end - mid)

        if left <= mid:
            ans += self.query(node.left, start, mid, left, right)
        if right > mid:
            ans += self.query(node.right, mid + 1, end, left, right)
        return ans

    def addRange(self, left: int, right: int) -> None:
        self.update(self.root, self.start, self.end, left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        ans = self.query(self.root, self.start, self.end, left, right - 1)
        if ans == right - left:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        self.update(self.root, self.start, self.end, left, right - 1, 0)


if __name__ == '__main__':
    s = RangeModule()
    s.addRange(10, 20)
    s.removeRange(14, 16)

    ans = s.queryRange(10, 14)
    assert ans == True

    ans = s.queryRange(13, 15)
    assert ans == False

    ans = s.queryRange(16, 17)
    assert ans == True

