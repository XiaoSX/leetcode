#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/23
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        states = ['start', 'end', 'start_fiction', 'fiction_float_num',
                  'int-num', 'num', 'e/E', 'wrong', '+/-', '+/-int']
        sname2id = [0, 1, 2, 3,
                    4, 5, 6, 7, 8, 9]

        # [' ', '.', 'e/E', 'num', '+/-']
        map_state = {' ': 0, '.': 1, 'e': 2, 'E':2, '+': 4, '-': 4,
                     '0': 3, '1': 3,'2': 3,'3': 3,'4': 3,
                     '5': 3,'6': 3,'7': 3,'8': 3,'9': 3,}
        transfer = [
            [0, 2, 7, 5, 8],
            [1, 7, 7, 7, 7],
            [7, 7, 7, 3, 7],
            [1, 7, 6, 3, 7],  # 3
            [1, 7, 7, 4, 7],  # 4
            [1, 3, 6, 5, 7],  # 5
            [7, 7, 7, 4, 9],  # 6
            [7, 7, 7, 7, 7],
            [7, 2, 7, 5, 7],
            [7, 7, 7, 4, 7],
        ]
        ns = 0
        s += ' '
        for i in range(len(s)):
            if s[i] not in map_state:
                return False
            ns = transfer[ns][map_state[s[i]]]
            if ns == 7:
                return False

        if ns == 1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    t = "+2.e+3"
    assert s.isNumber(t) == True
    t = "12.e+3"
    assert s.isNumber(t) == True
    t = "-2.3"
    assert s.isNumber(t) == True
    t = "-1"
    assert s.isNumber(t) == True
    t = "-1.1."
    assert s.isNumber(t) == False
    t = "e3"
    assert s.isNumber(t) == False
    t = ".2"
    assert s.isNumber(t) == True
    t = ".2+1"
    assert s.isNumber(t) == False
    t = "+2.+3"
    assert s.isNumber(t) == False
    t = "..."
    assert s.isNumber(t) == False
    test = ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
    for t in test:
        assert s.isNumber(t) == True

    test = ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
    for t in test:
        assert s.isNumber(t) == False

    t = "s.e"
    assert s.isNumber(t) == False

    t = "4e+"
    assert s.isNumber(t) == False

    t = " -."
    assert s.isNumber(t) == False
