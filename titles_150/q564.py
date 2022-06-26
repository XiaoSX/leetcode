#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/2
'''


def cal(num, a=1, dir=1):
    ans = list(num)
    n = len(ans)
    move = 0
    a *= dir
    for i in range(n-1, -1, -1):
        cur = move + int(num[i]) + a
        a = 0
        move = 0
        if cur < 0:
            cur += 10
            move -= 1
        elif cur > 9:
            cur -= 10
            move += 1
        ans[i] = str(cur)
    if move > 0:
        ans = [str(move)] + ans
    i = 0
    while i < n:
        if ans[i] == '0':
            i += 1
        else:
            break

    ans = ans[i:]
    if len(ans) == 0:
        ans = ['0']
    return ''.join(ans)


def find(num, dir) -> (str, int):
    nlen = len(num)
    i, j = 0, 0
    if nlen % 2 == 1:
        i, j = nlen // 2, nlen // 2
    else:
        i = (nlen - 1) // 2
        j = i + 1

    pre_half = int(num[:i + 1][::-1])
    last_half = int(num[j:])
    if (dir > 0 and pre_half > last_half) or (dir < 0 and pre_half < last_half):
        if nlen % 2 == 1:
            ans = list(num[:i]) + list(num[:i + 1][::-1])
        else:
            ans = list(num[:i + 1]) + list(num[:i + 1][::-1])
        return ans, abs(pre_half - last_half)
    elif dir < 0:
        pre_half_str = cal(num[:i+1], 1, -1)
        num = pre_half_str + num[i+1:]

        nlen = len(num)
        i, j = 0, 0
        if nlen % 2 == 1:
            i, j = nlen // 2, nlen // 2
        else:
            i = (nlen - 1) // 2
            j = i + 1

        pre_half = int(num[:i + 1][::-1])
        last_half = int(num[j:])

        if nlen % 2 == 1:
            ans = list(num[:i]) + list(num[:i + 1][::-1])
        else:
            ans = list(num[:i + 1]) + list(num[:i + 1][::-1])
        return ans, abs(pre_half - last_half)

    else:
        pre_half_str = cal(num[:i + 1], 1, 1)
        num = pre_half_str + num[i + 1:]

        nlen = len(num)
        i, j = 0, 0
        if nlen % 2 == 1:
            i, j = nlen // 2, nlen // 2
        else:
            i = (nlen - 1) // 2
            j = i + 1

        pre_half = int(num[:i + 1][::-1])
        last_half = int(num[j:])

        if nlen % 2 == 1:
            ans = list(num[:i]) + list(num[:i + 1][::-1])
        else:
            ans = list(num[:i + 1]) + list(num[:i + 1][::-1])
        return ans, abs(pre_half - last_half)





class Solution:
    def nearestPalindromic(self, n: str) -> str:
        nlen = len(n)
        if nlen == 1:
            return str(int(n) - 1)

        if all([x == '0' for x in n[1:-1]]) and n[-1] in ['1', '0']:
            return '9' * (nlen - 1)

        if all([x == '9' for x in n]):
            return '1' + '0' * (nlen - 1) + '1'


        if nlen % 2 == 1:
            i, j = nlen // 2, nlen // 2
        else:
            i = (nlen - 1) // 2
            j = i + 1

        pre_half = n[:i+1][::-1]
        last_half = n[j:]
        if pre_half == last_half:
            num = cal(n, 1, 1)
            up_num, up_diff = find(num, 1)
            num = cal(n, 1, -1)
            down_num, down_diff = find(num, -1)
        else:
            up_num, up_diff = find(n, 1)
            down_num, down_diff = find(n, -1)

        if up_diff < down_diff:
            return ''.join(up_num)
        else:
            return ''.join(down_num)