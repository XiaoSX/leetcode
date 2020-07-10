#  -*-  coding: utf-8  -*-
def get_next(text):
    ans = []
    pre_v = -1
    cnt = 0
    for i in range(len(text)):
        if i == 0:
            pre_v = text[i]
            cnt = 1
            continue

        if text[i] == pre_v:
            cnt += 1
        else:
            ans.append(str(cnt))
            ans.append(pre_v)
            pre_v = text[i]
            cnt = 1
    if pre_v != -1:
        ans.append(str(cnt))
        ans.append(pre_v)

    return ans


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        num = 1
        start = ['1']
        for i in range(2, n + 1):
            start = get_next(start)

        return ''.join(start)