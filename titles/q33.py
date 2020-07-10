#  -*-  coding: utf-8  -*-
def bi_search(nums, target):
    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    low_i = 0
    high_i = len(nums) - 1

    while low_i < high_i:
        if nums[low_i] == target:
            return low_i
        if nums[high_i] == target:
            return high_i

        move_i = (low_i +high_i) // 2
        if nums[move_i] == target:
            return move_i
        if nums[move_i] > target:
            high_i = move_i
        else:
            if low_i == move_i:
                return -1
            low_i = move_i



class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1

        low_i = 0
        high_i = len(nums) - 1
        while low_i < high_i:
            if target > nums[high_i] and target < nums[low_i]:
                return -1

            if target == nums[low_i]:
                return low_i
            if target == nums[high_i]:
                return high_i

            if target < nums[high_i]:
                move_i = (low_i + high_i) // 2
                if move_i == low_i:
                    return -1
                if nums[move_i] == target:
                    return move_i
                elif nums[move_i] < target:
                    b_ans = bi_search(nums[move_i:high_i], target)
                    if b_ans == -1:
                        return b_ans
                    else:
                        return b_ans + move_i
                elif nums[move_i] < nums[high_i]:
                    high_i = move_i
                    continue
                else:
                    low_i = move_i
                    continue
            elif target > nums[high_i]:
                move_i = (low_i + high_i) // 2
                if move_i == low_i:
                    return -1
                if nums[move_i] == target:
                    return move_i
                elif nums[move_i] > target:
                    ans = bi_search(nums[low_i:move_i], target)
                    if ans == -1:
                        return ans
                    else:
                        return ans + low_i
                elif nums[move_i] > nums[low_i]:
                    low_i = move_i
                    continue
                else:
                    high_i = move_i
                    continue
