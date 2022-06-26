#!/usr/bin/pythoan
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/1
'''


# 负数
# 整除和除法
# 正负数交替

from typing import List
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        even = []
        odd = []
        n = len(arr)
        if n == 0:
            return False

        even = []
        j = 0
        i = -1
        is_nagetive = False
        for cur in range(len(arr)):
            if arr[cur] >= 0:
                if is_nagetive:
                    is_nagetive = False
                    if len(odd) != len(even):
                        return False

                if j >= len(even) or arr[cur] < 2 * even[j]:
                    even.append(arr[cur])
                    if len(even) > len(arr) / 2:
                        return False

                elif arr[cur] == 2 * even[j]:
                    odd.append(arr[cur])
                    j += 1
                else:
                    return False
            else:
                if not is_nagetive:
                    is_nagetive = True

                if j >= len(odd) or arr[cur] < odd[j] / 2:
                    odd.append(arr[cur])
                    if len(odd) > len(arr) / 2:
                        return False

                elif arr[cur] > odd[j] / 2:
                    return False
                else:
                    even.append(arr[cur])
                    j += 1

        return True


if __name__ == '__main__':
    s = Solution()
    case = [[0, 0, 0, 0],
            [0, 1, 0, 1],
            [1, 1, 2, 2],
            [1, 2, 3, 4],
            [1, 2],
            [1, 1],
            [4, -2, 2, -4],
            [4, -2, 0, 0, 2, -4],
            [-4, -2, -2, -1],
            [-5, -3],
            [-1, 2]
            ]
    ans = [True, False, True, False, True,
           False, True, True, True, False,
           False]
    for i in range(len(case)):
        assert s.canReorderDoubled(case[i]) == ans[i]