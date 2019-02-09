
from docxtpl import *
import xlrd
import numpy as np

name_of_tower=[]

def read_parameters(path_excel):
    workbook = xlrd.open_workbook(path_excel)
    sheet1 = workbook.sheet_by_name('风电场概况')
    sheet2 = workbook.sheet_by_name('2.2长期气象资料')
    sheet3 = workbook.sheet_by_name('2.3.1测风数据检验及处理')
    sheet4 = workbook.sheet_by_name('2.3.2测风数据整理')
    sheet5 = workbook.sheet_by_name('2.4测风数据代表年订正')
    sheet6 = workbook.sheet_by_name('2.5代表年风资源分析')
    sheet7 = workbook.sheet_by_name('2.6预装机轮毂高度处相关参数')
    sheet8 = workbook.sheet_by_name('风机布置&坐标')
    sheet9 = workbook.sheet_by_name('折减表')
    sheet10 = workbook.sheet_by_name('比选表格')

    # t=np.dtype([('name',str,20)])
    number_of_tower = int(sheet1.cell(14, 2).value)
    print(number_of_tower)
    name_of_tower=np.empty(number_of_tower).astype("str")
    for name_i in range(number_of_tower):
        if name_i==0:
            name_of_tower[name_i] = str(sheet3.cell(1, 0).value)
        elif name_i==1:
            name_of_tower[name_i] = str(sheet3.cell(1, 3).value)
        elif name_i==2:
            name_of_tower[name_i] = str(sheet3.cell(1, 6).value)
        elif name_i == 3:
            name_of_tower[name_i] = str(sheet3.cell(1, 9).value)

    print(name_of_tower)


def read_docx(path_template):
    tpl = DocxTemplate(path_template)
    context = {'number_of_tower': read_parameters.number_of_tower,
               }

    tpl.render(context)
    tpl.save(r'C:\Users\Administrator\PycharmProjects\untitled\files\chapter5_test.docx')

if __name__ == "__main__":
    read_parameters(r'C:\Users\Administrator\PycharmProjects\untitled\files\风资源工作簿-zyc修改.xlsm')
    # read_docx(r'C:\Users\Administrator\PycharmProjects\untitled\files\testA_01.docx')