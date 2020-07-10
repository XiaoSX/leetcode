#  -*-  coding: utf-8  -*-


def find_left_ge(arr, q_index, high_v, mount_tmp):
    """

    :param arr:
    :param i:
    :param high_v:
    :return: return the mount of the rain
    """
    i = q_index - 1
    mount = 0
    step = 0
    while arr[i] < high_v and arr[i] < arr[q_index]:
        mount -= arr[i]
        step += 1
        i -= 1
        mount_tmp[i] = 0
    mount_tmp[i] = mount + step * min(arr[q_index], arr[i])

class Solution:
    def trap(self, height) -> int:
        # 找递增序列的最高点
        if len(height) <= 1:
            return 0
        i = 0
        cur = 0
        n = len(height)
        mount_tmp = [0 for _ in range(n)]
        while i < n and cur <= height[i]:
            cur = height[i]
            i += 1
        flag = pre = cur
        ans = 0
        step = 0
        tmp_ans = 0
        while i < n:
            cur = height[i]
            if cur > pre and cur >= flag:
                # 更新flag和step
                tmp_ans += step * min(cur, flag)
                ans = tmp_ans
                flag = cur
                step = 0
                mount_tmp = [0 for _ in range(n)]
            elif cur > pre:
                # 开始接雨水,计算临时接雨水量
                find_left_ge(height, i, flag, mount_tmp)
                tmp_ans -= cur
                step += 1
            else:
                tmp_ans -= cur
                step += 1
            pre = cur
            i += 1
        return ans + sum(mount_tmp)
