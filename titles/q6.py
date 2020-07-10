#  -*-  coding: utf-8  -*-
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        n = len(s)
        for i in range(n):
            group = numRows * 2 - 2
            row_i = i % group
            order = row_i // numRows
            if order == 0:
                rows[row_i % numRows].append(s[i])
            else:
                rows[numRows - 2 - row_i % numRows].append(s[i])
        ans = ''.join(''.join(row) for row in rows)
        return ans