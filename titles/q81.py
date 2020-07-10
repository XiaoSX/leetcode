def bi_search(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1
    return False

class Solution:
    def search(self, nums, target: int) -> bool:
        # find the point
        if len(nums) == 0:
            return False

        low = 0
        high = len(nums) - 1
        rotate = len(nums)

        while low < high:
            if low + 1 == high:
                if nums[low] > nums[high]:
                    rotate = high
                low += 1
            else:
                mid = (low + high) // 2
                if nums[mid] > nums[low]:
                    low = mid
                elif nums[mid] == nums[low]:
                    low += 1
                elif nums[mid] < nums[high]:
                    high = mid
                else:
                    high -= 1

        if rotate == len(nums):
            return bi_search(nums, target)

        if target > nums[-1]:
            return bi_search(nums[:rotate], target)
        else:
            return bi_search(nums[rotate:], target)
