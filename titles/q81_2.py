#  -*-  coding: utf-8  -*-
class Solution:
    def search(self, nums, target: int) -> bool:
        high = len(nums)
        low = 0
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True

            if nums[mid] == nums[low]:
                low += 1
                continue
            elif nums[mid] > nums[low]:
                if target == nums[low]:
                    return True
                if target > nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if target == nums[high - 1]:
                    return True
                if target > nums[mid] and target < nums[high - 1]:
                    low = mid + 1
                else:
                    high = mid
        return False
