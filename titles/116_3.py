#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-09
'''

from titles.node import Node

class Solution:
    def subTreeConnect(self, root):
        if root is None:
            return

        leftmost = root

        # 逐层遍历非叶节点
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next

            leftmost = leftmost.left
        return root

"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 从根节点开始
        leftmost = root
        
        while leftmost.left:
            
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # 指针向后移动
                head = head.next
            
            # 去下一层的最左的节点
            leftmost = leftmost.left
        
        return root


"""
