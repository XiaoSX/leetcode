class Solution:
    # 将问题转化为q84, 利用单调栈求max_area
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

    def maximalRectangle(self, matrix) -> int:
        acc_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                r = i
                while r >= 0 and matrix[r][j] == '1':
                    acc_matrix[i][j] += int(matrix[r][j])
                    r -= 1

        max_area = 0
        for i in range(len(matrix)):
            max_area = max(max_area, self.largestRectangleArea(acc_matrix[i]))
        return max_area
