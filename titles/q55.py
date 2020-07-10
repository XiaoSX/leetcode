#  -*-  coding: utf-8  -*-
class Solution:
    def canJump(self, nums) -> bool:
        jump = 0
        n = len(nums)

        while jump < n:
            bound_jump = nums[jump] + jump
            if bound_jump >= n - 1:
                return True

            next_jump = jump
            max_jump = bound_jump
            while bound_jump > jump:
                if nums[bound_jump] + bound_jump > max_jump:
                    max_jump = nums[bound_jump] + bound_jump
                    next_jump = bound_jump
                bound_jump -= 1

            if next_jump != jump:
                jump = next_jump
            else:
                return False
