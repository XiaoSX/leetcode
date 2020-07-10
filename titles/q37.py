#  -*-  coding: utf-8  -*-

class Solution:

    def deep_search(self, arr, board):
        if len(arr) == 0:
            return True

        t_i, t_j = arr[0]
        total = self.rows[t_i].union(self.cols[t_j]).union(self.blocks[3 * (t_i // 3) + t_j // 3])
        canditates = [str(x) for x in range(1, 10) if str(x) not in total]
        if len(canditates) == 0:
            return False

        for i in canditates:
            board[t_i][t_j] = i
            self.rows[t_i].add(i)
            self.cols[t_j].add(i)
            self.blocks[3 * (t_i // 3) + t_j // 3].add(i)
            if self.deep_search(arr[1:], board):
                return True
            board[t_i][t_j] = '.'
            self.rows[t_i].remove(i)
            self.cols[t_j].remove(i)
            self.blocks[3 * (t_i // 3) + t_j // 3].remove(i)




    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.n = len(board)
        self.rows = [set() for _ in range(self.n)]
        self.cols = [set() for _ in range(self.n)]
        self.blocks = [set() for _ in range(self.n)]

        self.emptys = []
        # init
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == '.':
                    self.emptys.append((i, j))
                else:
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    self.blocks[3 * (i // 3) + j // 3].add(board[i][j])

        self.deep_search(self.emptys, board)
