#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 10:59 AM
# @Author  : Yongchin

from mkTestCase import Factory

if __name__ == '__main__':
    f = Factory()

    webdata = [["设备管理", "设备保养", "保养工单", ["Add", "Modify", "Delete", "Search", 'Pagination']],
               ["设备管理", "设备保养", "设备单位", ["Add", "Modify", "Delete", "Search", 'Pagination']],
               ["质量管理", "监督资料", ["Add", "Modify", "Delete"]]]

    a = f.deconstruction(webdata)
    f.mk_testcase("/Users/yangqing/Workspace/DEV/study/大屏3.0升级自动化输入表新.xlsx")
