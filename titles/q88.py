# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午5:13
# @Author  : RenMeng
# @File    : q88.py

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = m - 1
        k = n - 1
        while k >= 0:
            if j >= 0 and nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            i -= 1
