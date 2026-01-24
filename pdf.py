import fitz #pymupdf
import pandas as pd

pdf= fitz.open("Resume final.pdf")
text=""

for page in pdf:
    text+= page.get_text()

with open("resume_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Text successfully saved to resume_text.txt")



with open("resume_text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


txt = "".join(lines[::2])   


pdf = fitz.open()
page = pdf.new_page()
page.insert_text((50, 50), text, fontsize=16)


pdf.save("output.pdf")
pdf.close()

