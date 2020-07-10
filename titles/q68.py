#  -*-  coding: utf-8  -*-
class Solution:
    def fullJustify(self, words, maxWidth: int):
        ans = []
        n = len(words)

        i = 0
        while i < n:
            word_rb = []
            space_num = []
            left = 0
            while i < n:
                wn = len(words[i])
                if left + wn <= maxWidth:
                    word_rb.append(words[i])
                    space_num.append(1)
                    left += wn + 1
                    i += 1
                else:
                    left -= 1
                    space_num.pop(-1)
                    delta_space = maxWidth - left
                    space_num = [x + delta_space // len(space_num) for x in space_num]
                    space_num = [space_num[r] + 1 if r < delta_space % len(space_num) else space_num[r] for r in range(len(space_num)) ]
                    total = ''
                    for r in range(len(space_num)):
                        total += word_rb[r]
                        total += space_num[r] * ' '
                    total += word_rb[-1]
                    if len(total) != maxWidth:
                        total += (maxWidth - len(total)) * ' '
                    ans.append(total)
                    break

        total = ''
        cnt = 0
        for r in range(len(word_rb) - 1):
            total += word_rb[r]
            total += ' '
            cnt += len(word_rb[r]) + 1
        total += word_rb[-1]
        total += (maxWidth - cnt - len(word_rb[-1])) * ' '
        ans.append(total)
        return ans
