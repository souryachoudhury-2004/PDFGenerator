from fpdf import FPDF
import pandas as pd

# FPDF creates pdf object instances

pdf = FPDF(orientation="P", unit="mm", format="A4")
# 'P' stands for portrait

#pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)

# w = 0: setting width to zero means the text will run till the end of the page
# border sets a border line around the cell
# h sets the height of the cell
# ln = 1 ensures that you go to the next line when you create the next cell
# txt contains the text inside the cell

# pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)
# pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1, border=1)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # each pandas dataframe row acts like a dictionary
    pdf.set_font("Times", size=26, style="B")
    # sets text colour to grey
    pdf.set_text_color(50, 50, 50)
    pdf.cell(w=0, h=12, txt=f"{row['Order']}) {row['Topic']}:", ln=1)
    pdf.line(10, 23, 200, 23)
    extra_pages = int(row["Pages"])-1
    if extra_pages > 0:
        for i in range(0, extra_pages):
            pdf.add_page()









pdf.output("testoutput.pdf")



