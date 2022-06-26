#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/20
'''


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        t = 0
        n = len(input)
        max_v = 0

        while t < n:
            cur = 0
            while t < n and input[t] == '\t':
                cur += 1
                t += 1

            tmp = ''
            is_file = False
            while t < n and input[t] != '\n':
                if input[t] == '.':
                    is_file = True
                tmp += input[t]
                t += 1

            t += 1
            length = len(tmp)
            while len(stack) > cur:
                stack.pop(-1)
            if len(stack) > 0:
                length += stack[-1] + 1
            if is_file:
                max_v = max(max_v, length)
            stack.append(length)


        return max_v



# class Solution:
#     def __init__(self):
#         self.i = 0
#         self.max_v = 0
#
#     def lengthLongestPath(self, input: str) -> int:
#         def dfs(level, target):
#             tmp = ''
#             while self.i < len(input) and input[self.i] != '\n':
#                 tmp += input[self.i]
#                 self.i += 1
#             self.i += 1
#
#             cur = 0
#             while self.i < len(input) and input[self.i] == '\t':
#                 self.i += 1
#                 cur += 1
#
#             l = len(tmp)
#
#             if cur > level:
#                 cur = dfs(cur, target + l + 1)
#             if cur == level:
#                 self.max_v = max(self.max_v, target + l + 1)
#                 cur = dfs(cur, target)
#             if cur < level:
#                 self.max_v = max(self.max_v, target + l + 1)
#                 return cur
#
#         dfs(0, -1)
#         return self.max_v


if __name__ == '__main__':
    s = Solution()
    t = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(s.lengthLongestPath(t))
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(s.lengthLongestPath(input))
    input = "a"
    print(s.lengthLongestPath(input))

