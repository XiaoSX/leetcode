#  -*-  coding: utf-8  -*-

def bi_search(arr, num):
    low = 0
    high = len(arr)
    while low < high:
        mid_i = (low + high) // 2
        mid_v = arr[mid_i]
        if mid_v == num:
            return mid_i
        elif mid_v > num:
            high = mid_i
        else:
            low = mid_i + 1
    return low


class Solution:
    # 下标是默认元素值，下标和元素内容混淆
    # cur_value < pre_v 更新max_area, 忽略最后max_area的更新，即更新max_area，还有另外情况（数组便利结束）
    # 重置了area_size, 之后添加元素的时候，就不能用append了，要在area_size的地方重新赋值
    # 考虑性能，不是从[1, value]的值的cnt都需要维护
    # 利用排序数组，减少每次都要更新所有值操作，可以利用长度直接计算（不用每次更新），更新长度即可
    # 一个更巧妙的方法，用stack直接记录下标
    def largestRectangleArea(self, heights) -> int:
        heights = [0] + heights + [0]
        stacks = [0]  # 确保stack一定不会为空，代码中可以将“stack本来为空”的情况统一化处理
        max_area = 0
        for i in range(len(heights)):
            # 当出现逆序的时候，意味之前的元素（这里用while循环的原因）找到了上界，因为逆序中断了其往下拓展
            while heights[i] < heights[stacks[-1]]:
                # 出栈的同时，反向寻找其下界
                # 这个题巧妙就在其用stack记录了下标，出栈回退的时候，完全可以每次更新area
                j = stacks.pop()
                max_area = max(max_area, heights[j] * (i - stacks[-1] - 1))
            stacks.append(i)
        return max_area


