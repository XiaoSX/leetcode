#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/5
'''
from typing import List
import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.radius = radius

    def randPoint(self) -> List[float]:
        r = random.random() * self.radius
        theta = random.random() * 2 * math.pi
        x = self.x + r * math.cos(theta)
        y = self.y + r * math.sin(theta)
        return [x, y]