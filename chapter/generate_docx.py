import os
from generate_images import generate_images
from docxtpl import DocxTemplate, InlineImage
from foundation_args_chapter8 import foundation_args_chapter8
from connect_sql import connect_sql_chapter5, connect_sql_chapter8

path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']

args_chapter8 = {'foundation_type': '扩展基础', 'max_load': 110000}
print(type(args_chapter8))

args_chapter8 = {'foundation_type': '扩展基础', 'maxload': 110000}

tur_np, power_np, efficiency_np = connect_sql_chapter5(*turbine_list)
# sql_foundation, key_vaule = foundation_args_chapter8(foundation_type='扩展基础', baseboard_r=11)
sql_foundation, key_vaule = foundation_args_chapter8(**args_chapter8)
foundation_np = connect_sql_chapter8(sql_foundation, *key_vaule)
generate_images(path_images, power_np, efficiency_np)


# chapter 5
# tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\CR_chapter5_template.docx')
# context = {}
# for i in range(0, 16):
#     if i < 13:
#         key = 'tbl_contents' + str(i)
#         value = tur_np[:, i + 1]
#         context[key] = value
#     else:
#         key = 'tbl_contents' + str(i)
#         value = tur_np[:, i + 4]
#         context[key] = value
# print(context)
#
# png_box = ('powers', 'efficiency')
# for i in range(0, 2):
#     key = 'myimage' + str(i)
#     value = InlineImage(tpl, os.path.join(path_images, '%s.png') % png_box[i])
#     context[key] = value
# tpl.render(context)
# tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\result_chapter5.docx')
# print(foundation_np)

# # chapter 8

def Dict_chapter_8(foundation_np):
    import numpy as np
    np.set_printoptions(precision=2)
    Dict_8 = {}
    keys = ['ID', '基础型式', '极限荷载', '设防烈度', '承载力', '土方比', '底板半径R', '棱台顶面半径R1', '台柱半径R2',
            '底板外缘高度H1', '底板棱台高度H2', '台柱高度H3', '桩直径', '根数', '长度', '总桩长', '面积m2', '体积m3',
            '垫层', '土方开挖', '石方开挖', '土石方回填', '复合地基换填', '复合地基桩']
    for i in range(0, len(keys)):
        key = keys[i]
        value = foundation_np[:, i][0]

        Dict_8[key] = value
    return Dict_8


Dict_8 = Dict_chapter_8(foundation_np)
print(Dict_8)

keys = ['土方开挖', '石方开挖', '土石方回填', '体积m3', '垫层', '钢筋', '基础防水', '沉降观测']


def Write_Dict_chapter_8(Dict_8, *args):
    context = {}
    for i in args:
        key = i
        value = Dict_8.get(i, None)
        context[key] = value
    context['钢筋'] = round(Dict_8['体积m3'] / 10,2)
    context['基础防水'] = 1
    context['沉降观测'] = 4
    return context


context = Write_Dict_chapter_8(Dict_8, *keys)
print(context)

tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\CR_chapter8_template.docx')
tpl.render(context)
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\result_chapter8.docx')
