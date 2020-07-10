#  -*-  coding: utf-8  -*-
import re

def subMatch(s, p):
    if s == '' and p == '':
        return True

    if s == '' and p == '.*':
        return True

    if s == '':
        return False

    if p == '':
        return False

    si = 0
    pi = 0
    sn = len(s)
    pn = len(p)

    while si < sn and pi < pn:
        if s[si] == p[pi]:
            si += 1
            pi += 1
        else:
            if p[pi] == '.':
                si += 1
                pi += 1
            elif p[pi] == '*':
                if pi == 0:
                    return False
                if p[pi - 1] == '.':
                    si -= 1
                    pi += 1
                    while si < sn and not subMatch(s[si:], p[pi:]):
                        si += 1
                    if si >= sn and pi != pn:
                        return False
                    else:
                        return True
                else:
                    si -= 1
                    pi += 1
                    pre_v = p[pi - 2]
                    tmp = 0
                    while si < sn and not subMatch(s[si:], p[pi:]):
                        if s[si] == pre_v:
                            si += 1
                        else:
                            tmp = 1
                            break

                    if tmp == 1 and si < sn and s[si] != pre_v:
                        return False
                    elif si >= sn and pi != pn:
                        return False
                    else:
                        return True
            else:
                if pi + 1 < pn and p[pi + 1] == '*':
                    pi += 1
                    si += 1
                else:
                    return False

    if si != sn or pi != pn:
        return False
    else:
        return True

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s += '$$$'
        p += '$$$'

        p = re.sub('(\*){1,}', '*', p)
        p = re.sub('(\.\*){1,}', '.*', p)

        return subMatch(s, p)


