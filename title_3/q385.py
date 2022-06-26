#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/15
'''

class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       # :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def __init__(self):
        self.index = 0

    def deserialize(self, s: str):

        if s[0] != '[':
            # return NestedInteger(int(s))
            return int(s)



        num = ''
        # ans = NestedInteger()
        ans = []
        self.index += 1
        while self.index < len(s):
            t = s[self.index]
            if t == ',':
                # ans.add(NestedInteger(int(num)))
                if num != '':
                    ans.append(int(num))
                num = ''
            elif t == '[':
                # ans.add(self.deserialize(s))
                ans.append(self.deserialize(s))
            elif t == ']':
                if num != '':
                    # ans.add(NestedInteger(int(num)))
                    ans.append(int(num))
                self.index += 1
                return ans
            else:
                num += t

            self.index += 1


if __name__ == '__main__':
    s = Solution()
    t = "[123,456,[788,799,833],[[]],10,[]]"
    print(s.deserialize(t))