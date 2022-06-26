#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/30
'''


def mapNum(num):
    ans = []
    while num:
        a = num % 26
        ans.append(a)
        if a == 0:
            num = (num - 1) // 26
        else:
            num = num // 26
    map_info = 'zabcdefghijklmnopqrstuvwxy'
    map_info.capitalize()
    map_info = {i: map_info[i] for i in range(26)}
    ans = ans[::-1]
    return ''.join([map_info[x] for x in ans])

def generateAns(n):
    ans = []
    map_info = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        ans.append(map_info[i])
        n -= 1
        if n == 0:
            break
    cur_pri = 'a'
    while n>0:
        for i in range(len(ans)-26, len(ans)):
            ans.append(cur_pri + map_info[i])
            n -= 1
            if n == 0:
                break
        if cur_pri == 'z':
            cur_pri = 'a'
        else:
            cur_pri = chr(ord(cur_pri) + 1)
    return ans



if __name__ == '__main__':
    ans = mapNum(1)
    assert ans == 'a'
    ans = mapNum(26)
    assert  ans == 'z'
    ans = mapNum(27)
    assert ans == 'aa'
    ans = mapNum(28)
    assert  ans == 'ab'
    ans = mapNum(52)
    assert ans == 'az'
    ans = mapNum(26* 26 + 26)
    assert ans == 'zz'
    n = 200
    ans = []
    for i in range(1, n + 1):
        ans.append(mapNum(i))
    true_ans = generateAns(n)
    for i in range(n):
        if true_ans[i] != ans[i]:
            print(i, true_ans[i], ans[i])
    # print(ans, true_ans)
    assert true_ans == ans