#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/6
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        paths = path.split('/')
        new_paths = []
        for p in paths:
            if p in ['/', '.', '']:
                continue
            if p == '..':
                new_paths = new_paths[:-1]
                continue
            new_paths.append(p)
        return '/' + '/'.join(new_paths)