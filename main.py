from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=0, h=12, txt='Hello World', align='L', ln=1)
pdf.line(x1=10, y1=18, x2=200, y2=18)



pdf.output("pdf_file.pdf")

