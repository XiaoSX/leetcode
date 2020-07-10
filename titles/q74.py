#  -*-  coding: utf-8  -*-

def bi_search(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        if target < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return False

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        ith = m


        for i in range(m):
            if target == matrix[i][0]:
                return True
            elif target < matrix[i][0]:
                ith = i
                break
            else:
                pass

        ith -= 1
        if ith == -1:
            return False

        if target == matrix[ith][n - 1]:
            return True
        if target > matrix[ith][n - 1]:
            return False
        return bi_search(matrix[ith], target)