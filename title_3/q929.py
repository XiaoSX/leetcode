#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/4
'''

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        address = set()
        for add in emails:
            local_name, domain_name = add.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            address.add(local_name + '@' + domain_name)
        return len(address)


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    test.append(emails)
    ans.append(2)

    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    test.append(emails)
    ans.append(3)

    for i in range(len(test)):
        assert s.numUniqueEmails(test[i]) == ans[i]