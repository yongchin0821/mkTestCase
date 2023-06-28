#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 10:55 AM
# @Author  : Yongchin

import yaml
import copy
from openpyxl import Workbook
import string
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Factory:
    def __init__(self):
        self.m_count = 0
        self.model_index = []
        self.rows = []

    def load(self):
        with open(os.path.join(BASE_DIR, "testcases/form.yml")) as f:
            ya = yaml.safe_load(f)
        result = ya["Add"]
        f.close()

        return result

    def mk_model(self, name_list):
        lenth = len(name_list)
        for i in range(self.m_count - lenth):
            name_list.append("")
        self.model_index = name_list

    def mk_row(self, data):
        model = data[:-1]
        self.mk_model(model)
        case = data[-1]
        rows = self.contact(case)
        for i in rows:
            self.rows.append(i)

    def contact(self, datas):
        treeData = []

        for i in datas:
            if i in ["Add", "Modify", "Delete", "Search"]:
                with open(os.path.join(BASE_DIR, "testcases/form.yml")) as f:
                    ya = yaml.safe_load(f)

            elif i in ["Pagination"]:
                with open(os.path.join(BASE_DIR, "testcases/page.yml")) as f:
                    ya = yaml.safe_load(f)

            else:
                raise IOError("模块在列表中不存在")

            result = ya[i]
            for j in result:
                head = copy.deepcopy(self.model_index)
                head.append(j["name"])
                head.append(j["step"])
                head.append(j["expect"])
                treeData.append(head)

            f.close()

        return treeData

    def deconstruction(self, datas: list):
        # 解析数据

        # 得到模板最大数
        for data in datas:
            count = len(data) - 1
            if count > self.m_count:
                self.m_count = count

        # 拆解数据
        for data in datas:
            self.mk_row(data)

        return self.rows

    def mk_testcase(self, output_path):
        wb = Workbook()
        ws = wb.active
        lowercase = string.ascii_lowercase
        title_prefix = []
        for i in range(self.m_count):
            module_name = "模块" + lowercase[i]
            title_prefix.append(module_name)
        ws.append(title_prefix + ["用例名称", "测试步骤", "期望结果"])
        for row in self.rows:
            ws.append(row)

        wb.save(output_path)


if __name__ == '__main__':
    f = Factory()

    webdata = [["设备管理", "设备保养", "保养工单", ["Add", "Modify", "Delete", "Search", ""]],
               ["质量管理", "监督资料", ["Add", "Modify", "Delete"]]]

    a = f.deconstruction(webdata)
