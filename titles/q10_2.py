#  -*-  coding: utf-8  -*-
# 更好的抽象问题，找到问题的最优子结构

# class Solution(object):
#     def isMatch(self, s: str, p: str) -> bool:
#         # 模式串为空，主串为空，不一定是false
#         if p == '':
#             return not s
#
#         first_match = False
#
#         # 可以用"更短的字符串"匹配问题来表示原问题
#         if len(s) >= 1 and p[0] in [s[0], '.']:
#             first_match = True
#         # '*'出现，匹配零次，或多次
#         if len(p) >= 2 and p[1] == '*':
#             return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
#         # 直接匹配
#         else:
#             return first_match and self.isMatch(s[1:], p[1:])


class Solution(object):
    def __init__(self):
        self.dp = {}

    def isMatch(self, s: str, p: str) -> bool:
        # 模式串为空，主串为空，不一定是false
        if p == '':
            return not s

        if (s, p) in self.dp:
            return self.dp[(s, p)]

        first_match = False

        # 可以用"更短的字符串"匹配问题来表示原问题
        if len(s) >= 1 and p[0] in [s[0], '.']:
            first_match = True
        # '*'出现，匹配零次，或多次
        if len(p) >= 2 and p[1] == '*':
            self.dp[(s, p)] = self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        # 直接匹配
        else:
            self.dp[(s, p)] = first_match and self.isMatch(s[1:], p[1:])

        return self.dp[(s, p)]
