#  -*-  coding: utf-8  -*-
def search(nums, a):
    """
    二分查找
    :param nums: 有序数组
    :param a: query
    :return: query要插入的位置index
    """
    n = len(nums)
    if n == 0:
        return 0
    if a < nums[n//2]:
        return search(nums[:n//2], a)
    if a == nums[n//2]:
        return n//2
    return n//2 + 1 + search(nums[n//2 + 1:], a)

class Solution:
    def find_nth_num(self, nums1, nums2, nth):
        """
        找index为nth的数
        :param nums1:
        :param nums2:
        :param nth:
        :return:
        """
        n = len(nums1)
        m = len(nums2)
        if n == 0:
            return nums2[nth]
        if m == 0:
            return nums1[nth]

        if nth == 0:
            return nums1[0] if nums1[0] < nums2[0] else nums2[0]

        if nth == (n + m - 1):
            return nums1[-1] if nums1[-1] > nums2[-1] else nums2[-1]

        m_index = m // 2
        n_index = search(nums1, nums2[m_index])
        if m_index + n_index == 0:
            if nth == 0:
                return nums2[m_index]
            if nth == 1:
                return nums1[0]
            return self.find_nth_num(nums1[1:], nums2[:m_index], nth-2)

        former_n = n_index + m_index
        if former_n > nth:
            return self.find_nth_num(nums1[:n_index], nums2[:m_index], nth)
        return self.find_nth_num(nums1[n_index:], nums2[m_index:], nth-former_n)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        if (n + m) % 2 == 0:
            a = self.find_nth_num(nums1, nums2, (n + m)//2)
            b = self.find_nth_num(nums1, nums2, (n + m)//2 - 1)
            ans = (a + b) * 1.0 / 2
        else:
            ans = self.find_nth_num(nums1, nums2, (n+m)//2) * 1.0
        return ans
