#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-27
'''
class Solution:
    def numFriendRequests(self, ages) -> int:
        ages = sorted(ages, reverse=True)
        limits = []
        cnt = 0
        ans = 0
        peer = 0
        peer_cnt = 1
        for cur in ages:
            # 14岁及以下不产生消息
            if cur <= 14:
                break

            # 同龄人处理
            if cur == peer:
                peer_cnt += 1

            # 同龄人出口
            if cur != peer and peer_cnt > 1:
                ans += peer_cnt * (peer_cnt - 1) // 2
                peer_cnt = 1

            # 遍历当前cur，计算前cnt人中，将有i人不再往后继续发消息（失效）
            # limits 递减
            # limits 中>= cur的都失效
            i = 0
            for j in range(len(limits)):
                if limits[j] >= cur:
                    i += 1
                else:
                    break

            limits = limits[i:]
            cnt -= i

            # 前cnt个人发来消息
            ans += cnt

            cnt += 1
            low = cur * 0.5 + 7
            limits.append(low)
            peer = cur
        # 同龄人出口
        if peer_cnt > 1:
            ans += peer_cnt * (peer_cnt - 1) // 2
        return ans




