#  -*-  coding: utf-8  -*-

class Solution(object):
    # cur_r, cur_i 以最远边界为更新依据
    def longestPalindrome(self, s):
        text = '#' + '#'.join(s) + '#'
        text_len = len(text)
        if text_len <= 1:
            return text
        cur_i = 0
        p = [0 for _ in range(text_len)]
        p[cur_i] = 1
        cur_r = p[cur_i]
        id_maxp = cur_i
        i = cur_i + 1
        while i < text_len:
            if cur_r == 1:
                d = 1
                low_i = i - d
                high_i = i + d
                while (low_i >= 0 and high_i < text_len and text[low_i] == text[high_i]):
                    d += 1
                    low_i -= 1
                    high_i += 1
                p[i] = d
                cur_i = i
                cur_r = p[cur_i]
            else:
                for step in range(1, cur_r):
                    j = cur_i + step
                    d = p[cur_i - step]
                    if (d + step < cur_r):
                        p[j] = d
                        continue
                    d = min(d, cur_r - step)
                    low_i = j - d
                    high_i = j + d
                    while (low_i >= 0 and high_i < text_len and text[low_i] == text[high_i]):
                        d += 1
                        low_i -= 1
                        high_i += 1
                    p[j] = d
                    # rightest bound
                    if j + d > cur_i + cur_r:
                        cur_r = d
                        cur_i = j
                        break
                else:
                    cur_i = cur_i + cur_r - 1
                    cur_r = p[cur_i]

            if cur_r > p[id_maxp]:
                id_maxp = cur_i
            i = cur_i + 1

        low_i = max(0, id_maxp - p[id_maxp] + 1)
        high_i = min(id_maxp + p[id_maxp], text_len)
        ans = ''.join([ele for ele in text[low_i:high_i] if ele != '#'])
        return ans


