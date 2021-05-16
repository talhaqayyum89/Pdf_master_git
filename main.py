import re
import json
import PyPDF2
from processing_funcs import get_cnic_text, get_name_text

FILE_PATH = '/home/talhaabdulqayyum/Desktop/Extracted_pages/terrorist.pdf'
output_path = r'/home/talhaabdulqayyum/Desktop/Extracted Json/test.json'
list_main = []

f = open(FILE_PATH, mode='rb')
reader = PyPDF2.PdfFileReader(f)

for i in range(500):
    page = reader.getPage(i)
    txt = page.extractText()
    txt = txt.replace('\n', '')
    txt = txt.lower()

    # searching keywords in extracted text from pdf
    word_lookup = ['name', 'cnic']
    search_text = [w for w in word_lookup if re.search(r'\b{}\b'.format(re.escape(w)), txt)]

    if search_text != word_lookup:
        pass

    else:
        cnic = get_cnic_text(txt).replace("\n", "").strip()
        cnic_ = re.sub(r'-', '', cnic)

        name = get_name_text(txt).replace("\n", "").strip()

        if name.find('s/o') != -1:
            name_ = re.split('s/o', name)
        else:
            name_ = re.split('f/name:', name)

        dict_items = ['name', 'fatherName']
        dictionery = dict(zip(dict_items, name_))
        dictionery['cnic'] = cnic_

        list_main.append(dictionery)

with open(output_path, "w") as outfile:
    json.dump(list_main, outfile)
outfile.close()
