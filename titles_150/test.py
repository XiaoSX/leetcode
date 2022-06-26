#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/5
'''

from titles_150.q1576 import Solution
from time import time

if __name__ == '__main__':
    s = Solution()
    t = ["a?a?a?a?a?a?a?a?", '????????', 'a??b', '?ab????ab']
    for sub_t in t:
        print('ori: {}, replace: {}'.format(sub_t, s.modifyString(sub_t)))
    # print(s.modifyString(t))
