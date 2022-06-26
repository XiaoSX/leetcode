#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/12
'''

def Add(a, b):
    n = len(a)
    m = len(b)
    cnt = 0

    i = n - 1
    j = m - 1
    ans = []
    cnt = 0
    while i >= 0 or j >= 0:
        if i >= 0 and j >= 0:
            s = int(a[i]) + int(b[j]) + cnt
            i -= 1
            j -= 1
        elif i >= 0:
            s = int(a[i]) + cnt
            i -= 1
        else:
            s = int(b[j]) + cnt
            j -= 1
        ans.append(str(s % 10))
        cnt = s // 10
    if cnt != 0:
        ans.append(str(cnt))

    ans = ans[::-1]
    return ''.join(ans)


if __name__ == '__main__':
    a = '1'
    b = '99'
    ans = Add(a, b)
    assert ans == '100'

