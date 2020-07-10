#  -*-  coding: utf-8  -*-

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        n = len(s)
        if n == 0:
            return True

        for i in range(n):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop(-1)
                if top == '(' and s[i] == ')':
                    continue
                if top == '{' and s[i] == '}':
                    continue
                if top == '[' and s[i] == ']':
                    continue

                return False
        if len(stack) == 0:
            return True
        else:
            return False
