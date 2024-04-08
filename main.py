from fpdf import FPDF
import pandas as pd


df = pd.read_csv("data/topics.csv")
# print (df)
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)




for index, row in df.iterrows():


    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(x1=10, y1=18, x2=200, y2=18)
    y=28
    while y < 297:
        pdf.line(x1=10, y1=y, x2=200, y2=y)
        y = y + 10
    pdf.ln(265)
    pdf.set_text_color(180, 180, 180)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align='R', ln=1)
    for i in range(1,row["Pages"]):
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=12)
        pdf.line(x1=10, y1=18, x2=200, y2=18)
        y=28
        while y < 297:
            pdf.line(x1=10, y1=y, x2=200, y2=y)
            y = y + 10
        pdf.ln(275)
        pdf.set_text_color(180, 180, 180)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R', ln=1)





pdf.output("pdf_file.pdf")

