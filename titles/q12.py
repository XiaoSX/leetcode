#  -*-  coding: utf-8  -*-
class Solution:
    def intToRoman(self, num: int) -> str:
        i2r = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        roman = ['M', 'CM',  'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',  'V',  'IV', 'I']
        obj_i = [1000, 900, 500, 400, 100, 90, 50, 40,  10,  9, 5, 4, 1]
        ans = [0 for _ in range(len(roman))]

        i = 0
        while num > 0:
            t = num // obj_i[i]
            ans[i] = t
            num = num % obj_i[i]
            i += 1
        final_ans = ''
        for i in range(len(ans)):
            final_ans += ans[i] * roman[i]
        return final_ans

