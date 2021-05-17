import re
import json
import PyPDF2
from processing_funcs import get_cnic_text, get_name_text, get_name_att


FILE_PATH = '/home/talhaabdulqayyum/Desktop/Extracted_pages/terrorist.pdf'
output_path = r'/home/talhaabdulqayyum/Desktop/Extracted Json/fia_t_list.json'
list_main = []

file = open(FILE_PATH, mode='rb')
reader = PyPDF2.PdfFileReader(file)

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
        name_ = get_name_att(name)
        dict_items = ['name', 'fatherName']
        dictionary = dict(zip(dict_items, name_))
        dictionary['cnic'] = cnic_
        list_main.append(dictionary)


with open(output_path, "w") as outfile:
    json.dump(list_main, outfile)
outfile.close()
