#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/12
'''

from typing import List

# 维护序列最后一个元素，和当前最小
# 当前最小成立，则其余比当前小大的数，更成立
# 序列最后一个元素，一定是遇到的（大于当前小）的最小元素；如果比当前小 还小，则更新当前小；如果不是第二小，函数返回，存在答案
# 维护两套，因为 10, 12, 5, 13 这种case， 此时当前小不能更新
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return False

        cnt = 1
        meet_min = nums[0]
        last_num = meet_min
        next_meet_min = None

        for i in range(1, n):
            if nums[i] > last_num:
                last_num = nums[i]
                cnt += 1
                if cnt >= 3:
                    return True
            # 更新序列最后元素，对两段序列都有效，因为最后元素不变, 但是第一个元素变了，会影响后续序列的最后一个元素1, 5, 0, 4
            elif nums[i] <= last_num and nums[i] >= meet_min:
                if nums[i] > meet_min:
                    last_num = nums[i]
                    cnt = 2
                if next_meet_min is not None:
                    meet_min = next_meet_min
                    if nums[i] > meet_min:
                        last_num = nums[i]
                    next_meet_min = None
                    cnt = 2
            # 遇到最小
            elif nums[i] < meet_min:
                # 更新
                if next_meet_min is not None and nums[i] > next_meet_min:
                    meet_min = next_meet_min
                    last_num = nums[i]
                    cnt = 2
                    next_meet_min = None
                # 暂时更新
                elif next_meet_min is None or nums[i] < next_meet_min:
                    next_meet_min = nums[i]
                else:
                    pass
        return False