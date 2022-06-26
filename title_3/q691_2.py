#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/14
'''

from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        @cache
        def dp(mask: int) -> int:
            if mask == 0:
                return 0
            res = m + 1
            for sticker in stickers:
                left = mask
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    if mask >> i & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dp(left) + 1)
            return res
        res = dp((1 << m) - 1)
        return res if res <= m else -1
