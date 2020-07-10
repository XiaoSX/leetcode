# #  -*-  coding: utf-8  -*-
#
#
# def kmp(s, p, wth, wans):
#     if len(p) == 0:
#         return
#
#     n = len(p)
#     next = [0 for _ in range(n+1)]
#     for i in range(n+1):
#         if i == 0 or i == 1:
#             continue
#
#         for j in range(1, i):
#             if p[:j] == p[i-j:i]:
#                 next[i] = j
#     s_i = 0
#     p_i = 0
#     while s_i < len(s):
#         if s[s_i] == p[p_i]:
#             s_i += 1
#             p_i += 1
#         elif p_i == 0:
#             s_i += 1
#         else:
#             p_i = next[p_i]
#
#         if p_i == n:
#             wans[s_i - n].append(wth)
#             p_i = next[p_i]
#     return
#
#
#
# class Solution:
#     # 没有考虑重复的单词
#     def findSubstring(self, s: str, words):
#         w_n = len(words)
#         if w_n == 0:
#             return []
#         if s == '':
#             return []
#
#         w_len = len(words[0])
#         s_n = len(s)
#         index_word = [[] for _ in range(s_n)]
#
#         ans = []
#         for w in words:
#             if w != words[0]:
#                 break
#         else:
#             kmp(s, words[0] * w_n, 0, index_word)
#             for i in range(s_n):
#                 if index_word[i] != []:
#                     ans.append(i)
#             return ans
#
#
#         for i in range(w_n):
#             kmp(s, words[i], i, index_word)
#
#         for i in range(s_n):
#             if index_word[i] == []:
#                 continue
#
#             cur_w = index_word[i][0]
#             cur_i = i
#             seen = set()
#             seen.add(cur_w)
#             for j in range(w_n - 1):
#                 next_i = cur_i + w_len
#                 if next_i >= s_n:
#                     break
#                 if index_word[next_i] == []:
#                     break
#                 for ele in index_word[next_i]:
#                     if ele not in seen:
#                         seen.add(ele)
#                         break
#                 else:
#                     break
#
#                 cur_i = next_i
#             else:
#                 ans.append(i)
#         return ans
#
#
#
#
#


class Solution:
    def findSubstring(self, s: str, words):
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num :
                    res.append(left)
        return res
