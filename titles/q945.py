#  -*-  coding: utf-8  -*-


class Solution:
    def doQuickSort(self, A):
        if len(A) <= 1:
            return A

        A_len = len(A)
        flag = A[0]
        low_i = 1
        high_i = A_len - 1

        while low_i < A_len and high_i >= 1 and low_i <= high_i:
            while low_i < A_len and A[low_i] <= flag:
                low_i += 1
            while high_i >= 1 and A[high_i] >= flag:
                high_i -= 1

            if low_i < A_len and high_i >= 1 and low_i < high_i:
                tmp = A[low_i]
                A[low_i] = A[high_i]
                A[high_i] = tmp

        A[0] = A[high_i]
        A[high_i] = flag
        A[:high_i] = self.doQuickSort(A[:high_i])
        A[high_i + 1:] = self.doQuickSort(A[high_i+1:])
        return A[:high_i] + [A[high_i]] + A[high_i+1:]




    def minIncrementForUnique(self, A):
        # 快排
        self.doQuickSort(A)
        if len(A) <= 1:
            return 0

        # print(A)
        # 统计
        key = []
        counts = []

        A_len = len(A)
        low_i = 0
        high_i = low_i
        while high_i < A_len:
            high_i = low_i + 1
            cnt = 0
            while high_i < A_len and A[low_i] == A[high_i]:
                cnt += 1
                high_i += 1
            key.append(A[low_i])
            counts.append(cnt)
            low_i = high_i

        # print(key, counts)
        # 构建目标值
        target = [0 for _ in range(sum(counts))]
        total_count = 0
        t_i = 0
        for i in range(len(key)-1):
            total_count += counts[i]
            if total_count == 0:
                continue
            for j in range(key[i] + 1, key[i+1]):
                target[t_i] = j
                t_i += 1
                total_count -= 1
                if total_count == 0:
                    break
        last_num = key[-1]
        while t_i < len(target):
            target[t_i] = last_num + 1
            last_num = target[t_i]
            t_i += 1

        # print(target)

        # 还原待移动的值
        source = []
        for i in range(len(key)):
            for j in range(counts[i]):
                source.append(key[i])

        assert len(source) == len(target)

        # 求和
        ans = 0
        for i in range(len(source)):
            ans += target[i] - source[i]
        # print(ans)
        return ans


