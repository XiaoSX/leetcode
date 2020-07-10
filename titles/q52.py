#  -*-  coding: utf-8  -*-

#  -*-  coding: utf-8  -*-

class Solution:

    def is_ok(self, i, j):
        if j not in self.col_set and (i + j) not in self.limit_1 and (i - j) not in self.limit_2:
            return True
        else:
            return False

    def search(self, depth, ans):
        if depth == 0:
            ans.append([''.join(ele) for ele in self.space])
            return

        for i in range(self.n):
            if self.is_ok(self.n - depth, i):
                self.space[self.n - depth][i] = 'Q'
                self.col_set.add(i)  # col
                self.limit_1.add(self.n - depth + i)  # row+col 对角线
                self.limit_2.add(self.n - depth - i)  # row-col 反对角线
                self.search(depth - 1, ans)
                self.col_set.discard(i)  # col
                self.limit_1.discard(self.n - depth + i)  # row+col 对角线
                self.limit_2.discard(self.n - depth - i)  # row-col 反对角线
                self.space[self.n - depth][i] = '.'




    def totalNQueens(self, n: int):
        self.space = [['.' for _ in range(n)] for _ in range(n)]
        self.queens = ['Q' for _ in range(n)]
        self.n = n
        self.col_set = set()
        self.limit_1 = set()
        self.limit_2 = set()

        ans = []
        self.search(self.n, ans)
        return len(ans)