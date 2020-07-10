#  -*-  coding: utf-8  -*-

def binary(num):
    if num == 2:
        return '10'

    if num == 1:
        return '1'

    if num == 0:
        return '0'

    return binary(num // 2) + str(num % 2)

def check_state(state):
    if len(state) >= 2 and state[:2] == '10':
        return True
    else:
        return False

class Solution:
    def validUtf8(self, data) -> bool:
        n_bytes = 0

        for num in data:
            bin_rep = format(num, '08b')

            if n_bytes == 0:
                for bit in bin_rep:
                    if bit == '0':
                        break
                    else:
                        n_bytes += 1
                if n_bytes == 0:
                    continue

                # 不合法的情况只有1个'1' 或者大于4个'1'
                if n_bytes > 4 or n_bytes == 1:
                    return False

            else:
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False
            n_bytes -= 1

        return n_bytes == 0

