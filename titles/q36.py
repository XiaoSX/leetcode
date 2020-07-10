#  -*-  coding: utf-8  -*-

class Solution:
    def isValidSudoku(self, board) -> bool:
        n = len(board)

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        blocks = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False

                if board[i][j] not in cols[j]:
                    cols[j].add(board[i][j])
                else:
                    return False

                if board[i][j] not in blocks[3 * (i // 3) + (j // 3)]:
                    blocks[3 * (i // 3) + (j // 3)].add(board[i][j])
                else:
                    return False
        return True