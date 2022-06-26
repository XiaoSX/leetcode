#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/30
'''

class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        n = len(hand)
        if n == 0:
            return False
        if groupSize == 1:
            return True

        hand = sorted(hand)
        groups_cnt = []
        low = 0
        while low < n:
            # 重复的numbers
            high = low
            while high < n and hand[high] == hand[low]:
                high += 1
            high -= 1
            cnt = high - low + 1
            pre_v = hand[low]
            low += cnt

            # 计数统计
            j = -1
            for i in range(len(groups_cnt)):
                nth, g_cnt = groups_cnt[i]
                nth += 1
                groups_cnt[i][0] = nth
                if nth == groupSize:
                    j = i
                cnt -= g_cnt
                if cnt < 0:
                    return False
            if cnt > 0:
                groups_cnt.append([1, cnt])
            groups_cnt = groups_cnt[j+1:]

            if low < n and hand[low] != pre_v + 1 and len(groups_cnt) > 0:
                return False

        if len(groups_cnt) > 0:
            return False
        return True