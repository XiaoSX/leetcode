#  -*-  coding: utf-8  -*-
import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.split('/', path)
        cur = []
        for p in path:
            if p == '.' or p == '':
                continue
            elif p == '..':
                cur = cur[:-1]
            else:
                cur.append(p)
        return '/' + '/'.join(cur)