#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/1
'''

from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        area = sum(matchsticks)
        matchsticks = sorted(matchsticks)
        width = area // 4
        if area % 4 != 0:
            return False

        visit = [0 for _ in range(len(matchsticks))]
        n = len(matchsticks)
        final_ans = []


        def search(val, cnt, path):
            if cnt == 4:
                return True


            if val > width:
                return False

            for i in range(n):
                if visit[i] == 0:
                    if val + matchsticks[i] > width:
                        return False

                    visit[i] = 1
                    path.append(matchsticks[i])
                    if val + matchsticks[i] == width:
                        final_ans.append(list(path))
                        if search(0, cnt + 1, []):
                            return True
                        final_ans.pop()
                    else:
                        if search(val + matchsticks[i], cnt, path):
                            return True
                    path.pop()
                    visit[i] = 0
            return False

        ans = search(0, 0, [])
        return ans

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    matchsticks = [1,2,3,4,5,6,7,8,9,10,5,4,3,2,1]
    test.append(matchsticks)
    ans.append(False)

    matchsticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    test.append(matchsticks)
    ans.append(True)

    matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
    test.append(matchsticks)
    ans.append(True)

    matchsticks = [3, 3, 3, 3, 4]
    test.append(matchsticks)
    ans.append(False)

    for i in range(len(test)):
        assert s.makesquare(test[i]) == ans[i]
