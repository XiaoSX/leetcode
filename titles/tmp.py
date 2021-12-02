# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午4:01
# @Author  : RenMeng
# @File    : tmp.py


if __name__ == '__main__':
    nodes = [1, 7, 3, 4, 5, 2, 3, 4, 5, 1]
    x = None
    y = None
    pre = nodes[0]
    # 扫面遍历的结果，找出可能存在错误交换的节点x和y
    for i in range(1,len(nodes)):
        if pre >nodes[i]:
            y=nodes[i]
            if not x:
                x = pre
        pre = nodes[i]
    # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树
    print(x, y)
    print(nodes)