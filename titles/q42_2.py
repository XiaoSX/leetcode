# #  -*-  coding: utf-8  -*-
# class Solution:
#     def trap(self, height) -> int:
#         # find left bound
#         n = len(height)
#         if n <= 1:
#             return 0
#
#         left_bound = [height[0] for _ in range(n)]
#         right_bound = [height[n - 1] for _ in range(n)]
#
#         for i in range(1, n):
#             if height[i] > left_bound[i - 1]:
#                 left_bound[i] = height[i]
#             else:
#                 left_bound[i] = left_bound[i - 1]
#         # find right bound index
#         for i in range(n - 2, -1, -1):
#             if height[i] > right_bound[i + 1]:
#                 right_bound[i] = height[i]
#             else:
#                 right_bound[i] = right_bound[i + 1]
#
#         ans = 0
#         for i in range(n):
#             ans += min(right_bound[i], left_bound[i]) - height[i]
#
#         return ans

class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n <= 1:
            return 0

        left_i = 0
        right_i = n - 1
        left_v = height[left_i]
        right_v = height[right_i]
        ans = 0
        while left_i <= right_i:
            if left_v <= right_v:
                ans += max(0, left_v - height[left_i])
                if height[left_i] > left_v:
                    left_v = height[left_i]
                left_i += 1
            else:
                ans += max(0, right_v - height[right_i])
                if height[right_i] > right_v:
                    right_v = height[right_i]
                right_i -=1
        return ans