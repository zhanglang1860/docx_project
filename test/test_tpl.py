
from docxtpl import *


def read_docx(path):
    tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\untitled\files\escape_tpl.docx')

    context = {'myvar': R('"less than" must be escaped : <, this can be done with RichText() or R()'),
               'myescvar': 'It can be escaped with a "|e" jinja filter in the template too : < ',
               'nlnp': Listing('Here is a multiple\nlines\nstring\aand some\aother\aparagraphs\aNOTE: the current character styling is removed'),
               'mylisting': Listing('the listing\nwith\nsome\nlines\nand special chars : <>&\f ... and a page break'),
               'page_break': R('\f'),
               }

    tpl.render(context)
    tpl.save(r'C:\Users\Administrator\PycharmProjects\untitled\files\escape.docx')

if __name__ == "__main__":
    read_docx(r'C:\Users\Administrator\PycharmProjects\untitled\files\testA_01.docx')