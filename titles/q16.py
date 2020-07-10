#  -*-  coding: utf-8  -*-

#  最接近的位置，start， start-1
def bi_search(arr, start_i, target):
    end_i = len(arr)

    while start_i < end_i:
        mid_i = (start_i + end_i) // 2
        if arr[mid_i] == target:
            return mid_i
        elif arr[mid_i] > target:
            end_i = mid_i
        else:
            start_i = mid_i + 1
    return start_i


class Solution:
    #  搜索边界，最接近不是min,min(abs())
    def threeSumClosest(self, nums, target):
        nums.sort()

        n = len(nums)
        ans = 9999999
        final = 0

        tmp = {}
        # 组合数去重
        for i in range(1, n - 1):

            if i >= 1 and nums[i - 1] == nums[i]:
                if nums[i - 1] not in tmp:
                    tmp[nums[i - 1]] = 1
                    cur_sum = 2 * nums[i]
                    closet_i = bi_search(nums, i + 1, target - cur_sum)
                    if closet_i == i + 1 and closet_i < n:
                        t = abs(cur_sum + nums[closet_i] - target)
                        if ans > t:
                            ans = t
                            final = cur_sum + nums[closet_i]
                    elif closet_i == n:
                        t = abs(cur_sum + nums[closet_i - 1] - target)
                        if ans > t:
                            ans = t
                            final = cur_sum + nums[closet_i - 1]
                    else:
                        t = abs(cur_sum + nums[closet_i] - target)
                        if ans > t:
                            ans = t
                            final = cur_sum + nums[closet_i]

                        t = abs(cur_sum + nums[closet_i - 1] - target)
                        if ans > t:
                            ans = t
                            final = cur_sum + nums[closet_i - 1]
                continue

            for j in range(0, i):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                cur_sum = nums[i] + nums[j]
                closet_i = bi_search(nums, i + 1, target - cur_sum)
                if closet_i == i + 1 and closet_i < n:
                    t = abs(cur_sum + nums[closet_i] - target)
                    if ans > t:
                        ans = t
                        final = cur_sum + nums[closet_i]
                elif closet_i == n:
                    t = abs(cur_sum + nums[closet_i - 1] - target)
                    if ans > t:
                        ans = t
                        final = cur_sum + nums[closet_i - 1]
                else:
                    t = abs(cur_sum + nums[closet_i] - target)
                    if ans > t:
                        ans = t
                        final = cur_sum + nums[closet_i]

                    t = abs(cur_sum + nums[closet_i - 1] - target)
                    if ans > t:
                        ans = t
                        final = cur_sum + nums[closet_i - 1]
        return final

