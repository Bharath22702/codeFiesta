import PyPDF2

a = PyPDF2.PdfFileReader('Sample.pdf')
str = ""
for i in range(a.getNumPages()):
    str += a.getPage(i).extract_text()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(str)

f.close()
