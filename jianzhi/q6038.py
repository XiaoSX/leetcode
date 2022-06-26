#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/10
'''


class Solution:
    def minimizeResult(self, expression: str) -> str:
        add_id = expression.index('+')
        n = len(expression)
        left_i = 0
        right_i = add_id + 1
        num3 = 1
        num4 = 1
        min_ans = float('inf')
        for i in range(add_id):
            if i > 0:
                num3 = int(expression[:i])
            else:
                num3 = 1
            num1 = int(expression[i:add_id])
            for j in range(add_id + 1, n):
                if j < n - 1:
                    num4 = int(expression[j+1:])
                else:
                    num4 = 1
                num2 = int(expression[add_id + 1: j+1])
                ans = num3 * (num1 + num2) * num4
                if min_ans > ans:
                    min_ans = ans
                    left_i = i
                    right_i = j

        result = ''
        for i in range(n):
            if i == left_i:
                result += '('
            result += expression[i]
            if i == right_i:
                result += ')'

        return result


if __name__ == '__main__':
    s = Solution()
    exp = "999+999"
    ans = s.minimizeResult(exp)
    print(ans)

