#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/14
'''

from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        # m组数据
        flags = [[i, 0] for i in range(m)]
        not_work_cnt = 0
        ans = []

        while k > 0:
            min_v = float('inf')
            min_x = -1
            min_y = -1

            candidate = []
            for fj in flags:
                # 无效组
                if fj[1] >= n:
                    continue
                # 后面的组不可能比当前小
                if len(candidate) > 0 and candidate[-1][1] == 0:
                    break
                # 当前组没有上一组小
                if len(candidate) > 0 and fj[1] == candidate[-1][1]:
                    continue
                candidate.append(fj)
                x, y = fj
                cur_num = nums1[x] + nums2[y]
                if cur_num < min_v:
                    min_v = cur_num
                    min_x = x
                    min_y = y

            flags[min_x][1] += 1
            ans.append([nums1[min_x], nums2[min_y]])
            if flags[min_x][1] >= n:
                not_work_cnt += 1

            if not_work_cnt == m:
                break
            k -= 1
        return ans

