#  -*-  coding: utf-8  -*-

# from titles_150.q1380 import MinStack as Solution
# from titles_150.q432 import Solution
# from titles_150.q432 import Heap
from jianzhi.ms_test2 import rotateArray
from titles_150.q2013 import DetectSquares
from titles.listnode import create_listnode, print_listnode
# from titles_150.q2024 import Solution
# from titles.tree import TreeNode, createTrees, inorderTraversal
from time import  time
from titles.tree import inorderNonRecur, preorderNonRecur, lastorderNonRecur

if __name__ == '__main__':
    # s = Solution()
    # s = Heap()
    # s = StockPrice()
    start = time()
    t = "TFFT"
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    # print(s.maxConsecutiveAnswers(t, 1))
    print(rotateArray(nums))


    # s.insert('renmeng')
    # s.insert('eugene')
    # s.insert('taotao')
    # s.update(2, 1)
    # s.update(2, 1)
    # s.update(2, 1)
    # s.update(2, 1)
    # s.update(2, 1)
    # s.update(2, 1)
    # s.update(1, 1)
    # s.update(1, 1)
    # s.update(1, 1)
    # s.update(0, 1)
    # print(s.memory_min)
    # print(s.memory_max)

    # s.add([11, 2])
    # s.update(1, 10)
    # # s.update(2, 5)
    # print(s.current())
    # print(s.maximum())
    # s.update(1, 3)
    # print(s.maximum())
    # s.update(4, 2)
    # print(s.minimum())
    # print(s.totalMoney(1000))
    # print(s.kSmallestPairrs(nums1, nums2, k))
    # print(s.compareVersion(version1, version2))
    # print(s.isEscapePossible([[1, 0], [3, 0], [2, 1], [0, 3], [2, 3]], [0, 0], [3, 3]))
    # print(s.calculateMinimumHP(nums))
    # s.getMin()
    # s.push(2147483646)
    # s.push(2147483646)
    # s.push(2147483647)
    # print(s.top())
    # s.pop()
    # print(s.getMin())
    # s.pop()
    # print(s.getMin())
    # s.pop()
    # s.push(2147483647)
    # print(s.top())
    # print(s.getMin())
    # s.push(-2147483647)
    # print(s.top())
    # print(s.getMin())
    # s.pop()
    # print(s.getMin())

    print(time() - start)

