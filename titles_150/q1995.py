# 重复元素
class Solution:
    # arr中n个数和为target的组合个数
    def countNumSum(self, arr, n, target):
        if len(arr) == 0:
            return 0

        if n == 0:
            return 0

        if n == 1:
            return len([x for x in arr if x == target])

        arr = [x for x in arr if x < target]
        cnt = 0
        for cur in list(arr):
            if len(arr) < n:
                break
            arr.remove(cur)
            pri_m = self.countNumSum(arr, n - 1, target - cur)
            cnt += pri_m
        return cnt

    def countQuadruplets(self, nums) -> int:
        cnt = 0
        for i in range(3, len(nums)):
            cnt += self.countNumSum(nums[:i], 3, nums[i])
        return cnt