#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/21
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.split('.')
        return '[.]'.join(address)


if __name__ == '__main__':
    s = Solution()
    address = "1.1.1.1"
    ans = s.defangIPaddr(address)
    print(ans)