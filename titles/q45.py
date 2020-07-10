#  -*-  coding: utf-8  -*-

# 找每一层的最大值
# 贪心
def Dijkstar(nums):
    n = len(nums)
    if n == 1:
        return 0
    low_i = 0
    high_i = 0
    dist = 0
    while True:
        max_v = 0
        # max_v = index
        for p in range(low_i, high_i + 1):
            max_v = max(max_v, p + nums[p])
        dist += 1
        low_i = high_i + 1
        high_i = max_v
        if max_v >= n - 1:
            return dist



def Dijkstra_star(nums):
    n = len(nums)
    g = [0 for _ in range(n)]
    for i in range(nums[0]):
        if i + 1 < n:
            g[i+1] = 1

    for i in range(1, n):
        if g[i] == 1:
            continue

        min = 999999
        for j in range(1, i):
            if i - j > nums[j]:
                continue
            if g[j] + 1 < min:
                min = g[j] + 1
        g[i] = min
    return g[n-1]



class Solution:
    def jump(self, nums) -> int:
        return Dijkstar(nums)