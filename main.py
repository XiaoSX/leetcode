#  -*-  coding: utf-8  -*-

from titles.q84 import Solution
from time import  time

if __name__ == '__main__':
    s = Solution()
    start = time()
    arr = [2,1,5,6,2,3]
    print(s.largestRectangleArea(arr))
    print(time() - start)