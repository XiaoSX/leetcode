# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 下午5:36
# @Author  : RenMeng
# @File    : q84_2.py

class Solution:
    # find the most-left bounder through the stack
    # find the bounder through comparison, same ways for both left and right
    def largestRectangleArea(self, heights) -> int:
        heights = [0] + heights + [0]
        stacks = [0] # 栈顶是heights的添加值
        cur_area = 0
        for i in range(1, len(heights)):
            # 直到当前元素大于栈顶, 并入栈
            # 栈顶元素比 > 当前元素, 出栈并计算面积
            while heights[i] < heights[stacks[-1]]:
                # 确定当前元素右界是否确定
                # 当前元素的左界
                cur_x = heights[stacks.pop(-1)]
                cur_area = max(cur_area, cur_x * (i - stacks[-1] - 1))
            stacks.append(i)
        return cur_area