#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/17
'''

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        low = 0
        high = len(arr)

        # 标记未位0是否复制
        flag = False
        while low < high:
            if arr[low] != 0:
                low += 1
            # 遇0则有效位减1
            elif arr[low] == 0 and high > low + 1:
                high -= 1
                low += 1
            else:
                low += 1
                flag = True

        # 尾部元素不复制
        low = low - 1  # 有效值
        high = len(arr)
        while low < high - 1:
            arr[high - 1] = arr[low]
            high -= 1
            if arr[low] == 0:
                if not flag:
                    arr[high - 1] = 0
                    high -= 1
                flag = False
            low -= 1


if __name__ == '__main__':
    s = Solution()
    arr = []
    s.duplicateZeros(arr)
    assert arr == []

    arr = [1, 2]
    s.duplicateZeros(arr)
    assert arr == [1, 2]

    arr = [1]
    s.duplicateZeros(arr)
    assert arr == [1]

    arr = [0]
    s.duplicateZeros(arr)
    assert arr == [0]

    arr = [0, 0]
    s.duplicateZeros(arr)
    assert arr == [0, 0]

    arr = [0, 0, 1, 0, 3, 4]
    s.duplicateZeros(arr)
    assert arr == [0, 0, 0, 0, 1, 0]

    arr = [0, 1, 0, 1, 1]
    s.duplicateZeros(arr)
    assert arr == [0, 0, 1, 0, 0]