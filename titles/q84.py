#  -*-  coding: utf-8  -*-
class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        area = 0
        for i in range(n):
            low = -1
            high = n
            for j in range(i, -1, -1):
                if heights[j] < heights[i]:
                    low = j
                    break
            for j in range(i, n, 1):
                if heights[j] < heights[i]:
                    high = j
                    break

            new_area = (high - low - 1) * heights[i]
            if new_area > area:
                area = new_area
        return area


