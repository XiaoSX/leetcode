#  -*-  coding: utf-8  -*-

# search 函数的进入和退出, 进入访问，退出清零
# 在搜索的一条有效路径退出的时候，visit会全部清零
def search(point, direct, word, board, visit):
    if word == '':
        return True

    x, y = point
    visit[x][y] = 1
    for i in direct:
        new_x = x + i[0]
        new_y = y + i[1]
        if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]) and \
            visit[new_x][new_y] == 0 and word[0] == board[new_x][new_y] and search((new_x, new_y), direct, word[1:], board, visit):
            return True
    visit[x][y] = 0
    return False


class Solution:
    def exist(self, board, word: str) -> bool:
        paths = []
        start = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == start:
                    paths.append((i, j))

        direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visit = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for p in paths:
            if search(p, direct, word[1:], board, visit):
                return True
        return False