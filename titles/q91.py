# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 上午9:40
# @Author  : RenMeng
# @File    : q91.py

class Solution:
    # 搜索空间和结束条件
    def search(self, s, ans):
        if s == '' and len(ans) != 0:
            self.cnt += 1
            return
        if s == '' and len(ans) == 0:
            return

        for i in range(min(2, len(s))):
            if int(s[:i + 1]) == 0:
                return
            if int(s[:i + 1]) < 27:
                ans.append(s[:i + 1])
                self.search(s[i + 1:], ans)
                ans.pop()

    # f[i] = f[i - 1] + f[i - 2] (if s[i-2:i] is possible)
    def numDecodings_0(self, s: str) -> int:
        if s == '':
            return 0
        # remove 0
        for i in range(len(s)):
            if s[i] == '0' and (i == 0 or int(s[i - 1]) == 0 or int(s[i - 1]) >= 3):
                return 0
        t = ''

        # 向前试探一个
        for i in range(1, len(s)):
            if s[i - 1] != '0' and s[i] == '0':
                t += 'A'
            elif s[i - 1] != '0' and s[i] != '0':
                t += s[i - 1]
            elif s[i - 1] == '0':
                continue
        if s[-1] != '0':
            t += s[-1]

        length = len(t)
        f = [0 for _ in range(length)]
        f.insert(0, 1)
        f[1] = 1

        for i in range(2, length + 1):
            f[i] = f[i - 1]
            try:
                cond = int(t[i-2:i])
                if cond < 27:
                    f[i] += f[i - 2]
            except:
                pass
        return f[length]

    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):  # 开头有 ‘0’ 直接返回
            return 0

        n = len(s)
        dp = [1] * (n + 1)  # 重点是 dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            if s[i - 1] == '0' and s[i - 2] not in '12':  # 出现前导 ‘0’ 的情况，不能解码，直接返回
                return 0
            if s[i - 2:i] in ['10', '20']:  # 只有组合在一起才能解码
                dp[i] = dp[i - 2]
            elif '10' < s[i - 2:i] <= '26':  # 两种解码方式
                dp[i] = dp[i - 1] + dp[i - 2]
            else:  # '01'到 ‘09’ 或 > '26'，只有单独才能解码
                dp[i] = dp[i - 1]
        return dp[n]