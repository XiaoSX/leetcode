#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/7
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/7
'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        tmp = sorted([(a, 'a'), (b, 'b'), (c, 'c')], key=lambda x: x[0], reverse=True)
        a, b, c = [x[0] for x in tmp]
        ans_map = {'a': tmp[0][1], 'b': tmp[1][1], 'c': tmp[2][1]}
        ans = ''
        if a == 0:
            return ans

        while b > 0 or c > 0 or a > 0:
            if b + c > a:
                ans += 'a'
                a -= 1
                if b >= 2:
                    ans += 'bb'
                    b -= 2
                elif c >= 2:
                    ans += 'cc'
                    c -= 2
                else:
                    ans += 'bc'
                    b -= 1
                    c -= 1
            elif b + c < a:
                if a >= 2:
                    ans += 'aa'
                    a -= 2
                else:
                    ans += 'a'
                    a -= 1
                if b == 0 and c == 0:
                    break
                if b > 0:
                    ans += 'b'
                    b -= 1
                elif c > 0:
                    ans += 'c'
                    c -= 1
            else:
                ans += 'a'
                a -= 1
                if b > 0:
                    ans += 'b'
                    b -= 1
                elif c > 0:
                    ans += 'c'
                    c -= 1



        return ''.join([ans_map[i] for i in ans])