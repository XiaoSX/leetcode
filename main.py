#  -*-  coding: utf-8  -*-

from titles.q144 import Solution
from titles.listnode import create_listnode, print_listnode
from titles.tree import TreeNode, createTrees, inorderTraversal
from time import  time
from titles.tree import inorderNonRecur, preorderNonRecur, lastorderNonRecur

if __name__ == '__main__':
    s = Solution()
    start = time()
    root = createTrees([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(s.preorderTraversal(root))
    print(time() - start)

