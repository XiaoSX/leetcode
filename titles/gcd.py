#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-03
'''


def gcd(a, b):
    """
    求a，b的最大公约数
    :param a:
    :param b:
    :return:
    """
    return a if b == 0 else gcd(b, a % b)