#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/18
'''

from typing import List
# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         ans = [1]
#         cnt = n - 1
#         while cnt > 0:
#             c = ans[-1]
#             # 深搜
#             if c * 10 <= n:
#                 ans.append(c * 10)
#             else:
#                 # 末位数位已搜索完成
#                 while c + 1 > n or c % 10 == 9:
#                     c = c // 10
#
#                 c += 1
#                 ans.append(c)
#
#             cnt -= 1
#
#         return ans

from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(a, limit):
            if a > limit:
                return

            ans.append(a)
            for i in range(10):
                dfs(a * 10 + i, limit)


        for i in range(1, 10):
            dfs(i, n)

        return ans



if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append(2)
    ans.append([1, 2])

    test.append(10)
    ans.append([1, 10, 2, 3, 4, 5, 6, 7, 8, 9])

    test.append(9)
    ans.append([1, 2, 3, 4, 5, 6, 7, 8, 9])


    for i in range(len(test)):
        print(s.lexicalOrder(test[i]))
        assert s.lexicalOrder(test[i]) == ans[i]