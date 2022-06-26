#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/29
'''

import re

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4_set = queryIP.split('.')
        ipv6_set = queryIP.split(':')
        ipv4 = False
        ipv6 = False
        if len(ipv4_set) == 4:
            for num in ipv4_set:
                if len(num) == 0:
                    break

                if num[0] == '0' and len(num) != 1:
                    break

                try:
                    num = int(num)
                except:
                    break

                if num < 0 or num > 255:
                    break
            else:
                ipv4 = True

        if len(ipv6_set) == 8:
            for num in ipv6_set:
                if re.search('^[0-9a-fA-F]{1,4}$', num) is None:
                    break
            else:
                ipv6 = True

        if ipv4:
            return "IPv4"

        if ipv6:
            return "IPv6"

        return "Neither"


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    queryIP = "172.16.254.1"
    test.append(queryIP)
    ans.append('IPv4')

    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    test.append(queryIP)
    ans.append('IPv6')

    queryIP = "256.256.256.256"
    test.append(queryIP)
    ans.append('Neither')

    queryIP = "192.168.1.1"
    test.append(queryIP)
    ans.append('IPv4')

    queryIP = "192.168.1.0"
    test.append(queryIP)
    ans.append('IPv4')

    queryIP = "192.168.01.1"
    test.append(queryIP)
    ans.append('Neither')

    queryIP = "192.168.1.00"
    test.append(queryIP)
    ans.append('Neither')

    queryIP = "192.168@1.1"
    test.append(queryIP)
    ans.append('Neither')

    queryIP = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    test.append(queryIP)
    ans.append('IPv6')

    queryIP = "2001:db8:85a3:0:0:8A2E:0370:7334"
    test.append(queryIP)
    ans.append('IPv6')

    queryIP = "2001:0db8:85a3::8A2E:037j:7334"
    test.append(queryIP)
    ans.append('Neither')

    queryIP = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
    test.append(queryIP)
    ans.append('Neither')

    queryIP = "10.1.1."
    test.append(queryIP)
    ans.append('Neither')

    for i in range(len(test)):
        assert s.validIPAddress(test[i]) == ans[i]

