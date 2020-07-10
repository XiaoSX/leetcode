#  -*-  coding: utf-8  -*-

alpha_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e'])



def is_Zero(s):
    s = s.strip()
    point_cnt = 0
    t = ''

    for i in range(len(s)):
        if s[i].isspace():
            return False

        if s[i] not in alpha_set:
            return False
        if s[i] in ['+', '-'] and i != 0:
            return False

        if s[i] == 'e':
            return False

        if s[i] == '.':
            if point_cnt != 0:
                return False
            else:
                point_cnt += 1
        if s[i] not in ['+', '-', '0', '.']:
            return False
        t += s[i]

        return t != '+' and t != '-' and t != '' and t != '.'

# case1 嵌套
def is_Int(s):

    s = s.strip()
    t = ''
    point_cnt = 0
    flag = 0

    for i in range(len(s)):
        if s[i].isspace():
            return False

        if s[i] not in alpha_set:
            return False
        if s[i] in ['+', '-'] and i != 0:
            return False
        if i > 0 and s[i - 1] in ['+', '-'] and s[i] in ['.', 'e']:
            return False
        if s[i] == 'e' and (i == 0 or i == len(s) - 1):
            return False
        if flag == 1 and s[i] != '0':
            return False

        if s[i] == '.':
            if point_cnt != 0 or i == len(s) - 1:
                return False
            else:
                point_cnt += 1
                flag = 1


        if s[i] == 'e':
            return t != '+' and t != '-' and t != '.' and t != '' and is_Zero(s[i + 1:])
        t += s[i]
    return t != '+' and t != '-' and t != '.' and t != ''


class Solution:
    def isNumber(self, s: str) -> bool:
        if s == '':
            return False

        s = s.strip()
        t = ''
        _int = ''
        _float = ''
        point_cnt = 0
        flag = 0

        for i in range(len(s)):
            if s[i].isspace():
                return False

            if s[i] not in alpha_set:
                return False
            if s[i] in ['+', '-'] and i != 0:
                return False
            if s[i] == 'e' and (i == 0 or i == len(s) - 1):
                return False
            if s[i] == '.':
                if point_cnt != 0:
                    return False
                else:
                    point_cnt += 1

            if s[i] in '0123456789':
                if point_cnt == 1:
                    _float += s[i]
                else:
                    _int += s[i]

            if s[i] == 'e':
                return t != '+' and t != '-' and t != '.' and t != '' and (_int != '' or _float != '') and is_Int(s[i+1:])
            t += s[i]
        return t != '+' and t != '-' and t != '.' and t != '' and (_int != '' or _float != '')
