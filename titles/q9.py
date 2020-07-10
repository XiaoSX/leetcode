#  -*-  coding: utf-8  -*-
# 只反转一半即可
# 考虑反转溢出问题
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = 0
        old_ans = x
        while x != 0:
            ans = ans * 10 + x % 10
            x = x // 10
        if ans == old_ans:
            return True
        else:
            return False