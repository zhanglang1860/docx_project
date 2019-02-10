import os
from generate_images import generate_images
from docxtpl import DocxTemplate, InlineImage
from foundation_args_chapter8 import foundation_args_chapter8
from connect_sql import connect_sql_chapter5, connect_sql_chapter8

path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
args_chapter8 = {'foundation_type': '扩展基础', 'maxload': 110000}
print(type(args_chapter8))
tur_np, power_np, efficiency_np = connect_sql_chapter5(*turbine_list)
sql_foundation, key_vaule = foundation_args_chapter8(foundation_type='扩展基础', baseboard_r=11)
# sql_foundation, key_vaule = foundation_args_chapter8(args_chapter8)
foundation_np = connect_sql_chapter8(sql_foundation, *key_vaule)
generate_images(path_images, power_np, efficiency_np)

#
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\CR_chapter5_template.docx')
context = {}
for i in range(0, 16):
    if i < 13:
        key = 'tbl_contents' + str(i)
        value = tur_np[:, i + 1]
        context[key] = value
    else:
        key = 'tbl_contents' + str(i)
        value = tur_np[:, i + 4]
        context[key] = value

png_box = ('powers', 'efficiency')
for i in range(0, 2):
    key = 'myimage' + str(i)
    value = InlineImage(tpl, os.path.join(path_images, '%s.png') % png_box[i])
    context[key] = value
tpl.render(context)
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\result_chapter5.docx')
print(foundation_np)
