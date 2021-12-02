#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-02
'''

a = [1,2,3]
def foo(b):
    print(b is a)
    b.append(4)
    print(b is a)
foo(a)    # 会打印出 True  True
print(a)  #  [1,2,3,4]

def bar(c):
    print(c is a)
    c = [0,0,0]
    print(c is a)
bar(a)    # 会打印出 True  False
print(a)  # [1,2,3,4]

    