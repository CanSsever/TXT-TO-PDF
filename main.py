from fpdf import FPDF
from pathlib import Path
import glob


filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation='p', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()

    filename = Path(filepath).stem
    animal_name = filename.split('.')[0]

    name = animal_name.capitalize()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.set_font(family="Times", size=16)
    pdf.multi_cell(w=0, h=6, txt=content)



pdf.output("output.pdf")