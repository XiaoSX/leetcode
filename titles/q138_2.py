#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-03
'''

class Solution:
    # 注意next为空的情况时，避免出现next.next
    # 注意key为空的情况
    def copyRandomList(self, head):
        if head is None:
            return
        node = head
        node_dic = {}
        while node:
            node_dic[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            node_dic[node].next = node_dic[node.next] if node.next else None
            node_dic[node].random = node_dic[node.random] if node.random else None
            node = node.next
        node = head
        return node_dic[node]