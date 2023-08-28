#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 10:59 AM
# @Author  : Yongchin

from mkTestCase import generator

if __name__ == '__main__':
    f = generator()

    case_group1 = ["系统管理-机构管理", ["Add", "Modify", "Delete", "Search", 'Pagination']]
    case_group2 = ["系统管理-角色管理", ["Add", "Modify", "Delete", "Search", 'Pagination']]
    case_group3 = ["系统管理-用户管理", ["Add", "Modify", "Delete", "Search", 'Pagination']]

    prompt = [case_group1, case_group2, case_group3]

    f.regist_yamlfile('mkTestCase/testcases/delete.yml')
    a = f.deconstruction(prompt)
    f.mk_testcase("/path/to/your/xxx.xlsx")
