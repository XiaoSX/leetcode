#  -*-  coding: utf-8  -*-
class ListNode:
    def __init__(self, num):
        self.data = num
        self.next = None

def add_listnode(node1, node2):
    head = ListNode(-1)
    pre = head

    cum = 0
    node1 = node1.next
    node2 = node2.next

    while node1 and node2:
        sum = node1.data + node2.data + cum
        cum = sum // 10
        pre.next = ListNode(sum % 10)
        pre = pre.next
        node1 = node1.next
        node2 = node2.next

    while node1:
        sum = node1.data + cum
        cum = sum // 10
        pre.next = ListNode(sum % 10)
        pre = pre.next
        node1 = node1.next

    while node2:
        sum = node2.data + cum
        cum = sum // 10
        pre.next = ListNode(sum % 10)
        pre = pre.next
        node2 = node2.next

    if cum != 0:
        pre.next = ListNode(cum)
    return head

def print_node(node):
    if node is None:
        return ''

    s = print_node(node.next)
    s += str(node.data)
    return s


class Solution:
    # 位数之间先相加，有进位的问题，可以最后考虑位数之间的进位
    # 倒序生成，可以不考虑进位累加问题
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)

        ans = [0 for _ in range(m + n)]

        for i in range(m-1, -1, -1):
            a = int(num1[i])
            for j in range(n-1, -1, -1):
                b = int(num2[j])
                # 位数间的相加进位
                sum = ans[i + j + 1] + a * b
                ans[i + j + 1] = sum % 10
                ans[i + j] += sum // 10

        i = 0
        while i < m + n and ans[i] == 0:
            i += 1
        s = ''
        if i == m + n:
            return '0'
        else:
            while i < m + n:
                s += str(ans[i])
                i += 1
        return s



