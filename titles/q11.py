#  -*-  coding: utf-8  -*-
class Solution:
    def maxArea(self, height) -> int:
        left_i = 0
        left_v = -1

        n = len(height)
        max_area = 0

        while left_i < n:
            if height[left_i] <= left_v:
                left_i += 1
                continue
            left_v = height[left_i]
            # find the max right bound
            right_i = n - 1
            right_v = -1
            while right_i >= 0:
                if height[right_i] <= right_v:
                    right_i -= 1
                    continue
                area = min(height[right_i], left_v) * (right_i - left_i)
                max_area = max(area, max_area)
                if height[right_i] >= left_v:
                    break

                right_v = height[right_i]
                right_i -= 1
            left_i += 1

        return max_area
