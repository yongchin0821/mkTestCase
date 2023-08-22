#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/6 10:55 AM
# @Author  : Yongchin

import copy
import os
import string

import yaml
from openpyxl import Workbook

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Factory:
    def __init__(self):
        self.m_count = 0
        self.model_index = []
        self.rows = []
        self.yaml_map = []

        self.init_yamlfiles()

    def init_yamlfiles(self):
        """初始化自带yml文件的信息"""
        script_path = os.path.split(__file__)[0]
        for root, _, files in os.walk(script_path):
            for file in files:
                if '.yml' in file:
                    # 获取文件的完整路径
                    file_path = os.path.join(root, file)
                    # 输出文件路径
                    with open(file_path) as f:
                        ya = yaml.safe_load(f)
                        data = {
                            "name": file,
                            "module": ya.keys(),
                            "path": file_path
                        }
                        self.yaml_map.append(data)

    def regist_yamlfile(self, file_path: str):
        """注册yml文件的信息"""
        filename = os.path.split(file_path)[1]
        # 输出文件路径
        with open(file_path) as f:
            ya = yaml.safe_load(f)
            data = {
                "name": filename,
                "module": ya.keys(),
                "path": file_path
            }
            self.yaml_map.append(data)

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

        for module in datas:
            for yml_info in self.yaml_map:
                if module in yml_info["module"]:
                    with open(yml_info["path"]) as f:
                        ya = yaml.safe_load(f)
                        f.close()
                        break
            if not ya:
                raise IOError("模块在列表中不存在")

            result = ya[module]
            for j in result:
                head = copy.deepcopy(self.model_index)
                head.append(j["identifies"])
                head.append(j["name"])
                head.append(j["step"])
                head.append(j["expect"])
                treeData.append(head)

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

        result = copy.deepcopy(self.rows)

        return result

    def mk_testcase(self, output_path):
        wb = Workbook()
        ws = wb.active
        lowercase = string.ascii_lowercase
        title_prefix = []
        for i in range(self.m_count):
            module_name = "模块" + lowercase[i]
            title_prefix.append(module_name)
        ws.append(title_prefix + ["用例标识", "用例名称", "测试步骤", "期望结果"])
        for row in self.rows:
            ws.append(row)

        wb.save(output_path)


if __name__ == '__main__':
    f = Factory()
    f.regist_yamlfile('/demo/login.yml')
    case_group1 = ["设备管理", "设备保养", "保养工单", ["Add", "Modify", "Delete", "Search"]]
    case_group2 = ["质量管理", "监督资料", ["Add", "Code"]]
    webdata = [case_group1, case_group2]

    a = f.deconstruction(webdata)
