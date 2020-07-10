#  -*-  coding: utf-8  -*-

def s2k(t):
    if t.isspace():
        return 'space'
    if t in set(list('0123456789')):
        return 'digit'
    if t in ['+', '-']:
        return 'sign'
    if t == '.' or t == 'e':
        return t
    return 'alpha'

class Solution:
    def isNumber(self, s: str) -> bool:
        s += ' '
        states = 10
        sybom = {'space': 0,
                 '.': 1,
                 'digit': 2,
                 'e': 3,
                 'sign': 4}

        graph = [[-1 for _ in range(len(sybom))] for _ in range(states)]
        graph[0] = [0, 1, 7, -1, 8]
        graph[1] = [-1, -1, 2, -1, -1]
        graph[2] = [6, -1, 2, 3, -1]
        graph[3] = [-1, -1, 4, -1, 5]
        graph[4] = [6, -1, 4, -1, -1]
        graph[5] = [-1, -1, 4, -1, -1]
        graph[6] = [6, -1, -1, -1, -1]
        graph[7] = [6, 9, 7, 3, -1]
        graph[8] = [-1, 1, 7, -1, -1]
        graph[9] = [6, -1, 2, 3, -1]
        start_s = 0

        for t in s:
            if s2k(t) == 'alpha':
                return False

            start_s = graph[start_s][sybom[s2k(t)]]
            if start_s == -1:
                return False

        if start_s == 0:
            return False
        return True
