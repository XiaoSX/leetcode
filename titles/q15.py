
class Solution:
    def threeSum(self, nums):
        target = 0
        nums.sort()

        n = len(nums)
        ans = {}
        final_ans = []

        for i in range(1, n):
            if nums[i] not in ans:
                ans[nums[i]] = 1
            else:
                ans[nums[i]] += 1

        tmp = {}
        # 组合数去重
        for i in range(1, n):
            ans[nums[i]] -= 1
            if ans[nums[i]] == 0:
                ans.pop(nums[i])

            if i >= 1 and nums[i - 1] == nums[i]:
                if nums[i - 1] not in tmp:
                    tmp[nums[i - 1]] = 1
                    cur_sum = 2 * nums[i]
                    if -cur_sum in ans:
                        final_ans.append([nums[i], nums[i], -cur_sum])
                continue

            for j in range(0, i):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                cur_sum = nums[i] + nums[j]
                if -cur_sum in ans:
                    final_ans.append([nums[i], nums[j], -cur_sum])
        return final_ans

