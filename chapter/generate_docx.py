import os
from connect_sql import connect_sql
from generate_images import generate_images
from docxtpl import DocxTemplate, InlineImage

path_images = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"
turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']

tur_np, power_np, efficiency_np = connect_sql(*turbine_list)
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
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\result_t1.docx')
