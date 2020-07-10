#  -*-  coding: utf-8  -*-

# 区间一定是左<=右
# class Solution:
#     def merge(self, intervals):
#         if len(intervals) <= 1:
#             return intervals
#         intervals = sorted(intervals, key=lambda x:x[0])
#         n = len(intervals)
#         low = 0
#         most_left = intervals[low][0]
#         most_right = intervals[low][1]
#         low += 1
#         ans = []
#         while low < n:
#             # 合并
#             if most_right >= intervals[low][0]:
#                 # 最右更新
#                 most_right = max(most_right, intervals[low][1])
#                 low += 1
#             else:
#                 ans.append([most_left, most_right])
#                 most_left = intervals[low][0]
#                 most_right = intervals[low][1]
#         # 循环结束后别忘记更新
#         ans.append([most_left, most_right])
#         return ans
#


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged = []

        # 循环的时候，不停的比较和更新最后一个元素的最右值
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged