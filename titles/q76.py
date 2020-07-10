#  -*-  coding: utf-8  -*-


# 只改变最小边界
def bi_search(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if target == arr[mid][1]:
            return mid + 1
        if target > arr[mid][1]:
            low = mid + 1
        else:
            high = mid

    return low

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == '' or t == '':
            return ''

        t_dic = {}
        for i in range(len(t)):
            if t[i] not in t_dic:
                t_dic[t[i]] = [1, []]
            else:
                t_dic[t[i]][0] += 1

        for i in range(len(s)):
            if s[i] in t_dic:
                t_dic[s[i]][1].append(i)

        if len(t_dic) == 1:
            for k in t_dic:
                if len(t_dic[k][1]) < t_dic[k][0]:
                    return ''
                elif t_dic[k][0] == 1:
                    return k
                else:
                    l = 0
                    h = 0
                    min_dic = len(s) + 1
                    for i in range(len(t_dic[k][1]) - t_dic[k][0] + 1):
                        low = t_dic[k][1][i]
                        high = t_dic[k][1][i + t_dic[k][0] - 1]
                        if (high - low) < min_dic:
                            min_dic = high - low
                            l = low
                            h = high
                    return s[l:h+1]


        candidates = []
        for k in t_dic:
            if len(t_dic[k][1]) < t_dic[k][0]:
                return ''
            for _ in range(t_dic[k][0]):
                candidates.append((k, t_dic[k][1][0]))
                t_dic[k][1].pop(0)

        candidates.sort(key=lambda x: x[1])
        low_k, low = candidates[0]
        high_k, high = candidates[-1]
        max_dis = high - low
        candidates.pop(0)

        while t_dic[low_k][1] != []:
            if t_dic[low_k][1][0] < candidates[0][1]:
                candidates.insert(0, (low_k, t_dic[low_k][1][0]))
            elif t_dic[low_k][1][0] > candidates[-1][1]:
                candidates.append((low_k, t_dic[low_k][1][0]))
            else:
                find_i = bi_search(candidates, t_dic[low_k][1][0])
                candidates.insert(find_i, (low_k, t_dic[low_k][1][0]))
            t_dic[low_k][1].pop(0)
            low_k, l = candidates[0]
            high_k, h = candidates[-1]
            if max_dis > (h - l):
                max_dis = h - l
                low = l
                high = h
            candidates.pop(0)

        return s[low:high+1]
