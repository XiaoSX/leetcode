#  -*-  coding: utf-8  -*-

def bi_search(arr, start_i, target):
    end_i = len(arr)

    while start_i < end_i:
        mid_i = (start_i + end_i) // 2
        if arr[mid_i] == target:
            return True
        elif arr[mid_i] > target:
            end_i = mid_i
        else:
            start_i = mid_i + 1
    return False


# 组合数去重，从当前下标往后搜索
def search(arr, visited, target, depth, start_i, ans, final_ans):
    if depth == 0:
        if target == 0:
            final_ans.append(ans[:])
        return

    used = []

    # 加快搜索
    if depth == 1:
        if bi_search(arr, start_i, target):
            ans.append(target)
            final_ans.append(ans[:])
            ans.pop(-1)
        return


    else:
        for i in range(start_i, len(arr)):
            if visited[i] == 1:
                continue

            if arr[i] in used:
                continue

            if arr[i] >= 0 and target - arr[i] < 0:
                break

            used.append(arr[i])
            visited[i] = 1
            ans.append(arr[i])
            search(arr, visited, target - arr[i], depth - 1, i + 1, ans, final_ans)
            ans.pop(-1)
            visited[i] = 0

    return


class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        if sum(nums[-4:]) < target:
            return []

        if sum(nums[:4]) > target:
            return []

        ans = []
        final_ans = []
        visited = [0 for _ in range(len(nums))]
        search(nums, visited, target, 4, 0, ans, final_ans)
        return final_ans
