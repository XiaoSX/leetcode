#  -*-  coding: utf-8  -*-
def search(arr, visit, depth, ans, k, final_ans):
    if depth == 0:
        k -= 1
        if k == 0:
            final_ans.append([str(i) for i in ans])
        return k

    n = len(arr)
    for i in range(n):
        if visit[i] != 1:
            ans.append(arr[i])
            visit[i] = 1
            k = search(arr, visit, depth - 1, ans, k, final_ans)
            if k == 0:
                break
            visit[i] = 0
            ans.pop(-1)

    return k



class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        base = 1
        for i in range(1, n):
            base *= i

        ith = 1
        while k - base > 0:
            k -= base
            ith += 1

        final_ans = []
        arr = [i for i in range(1, n+1)]
        ans = [arr[ith - 1]]
        visit = [0 if i != ith - 1 else 1 for i in range(n) ]
        depth = n
        search(arr, visit, depth - 1, ans,  k, final_ans)
        return ''.join(final_ans[0])
