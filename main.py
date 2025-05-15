from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) # RGB, Grey
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Add the Lines
    for y in range(21, 290, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)  # break lines
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)  # RGB, Light Grey
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Add the Lines
        for y in range(11, 290, 10):
            pdf.line(10, y, 200, y)

        pdf.ln(277)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)  # RGB, Light Grey
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")



pdf.output("output.pdf")