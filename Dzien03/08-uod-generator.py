
# Wykorzystanie plików XLSX, DOCX, PDF w Pythonie
import openpyxl
import pdfkit
from docx import Document

# Przyjmijmy, że plik ma lokalizacje c:\tmp\test.txt
file_name = "c:\\tmp\\test.txt"
file_name = "c:/tmp/test.txt"
file_name = r"c:\tmp\test.txt"

wb = openpyxl.load_workbook("../misc/uod-kopia.xlsx", data_only=True)
sheet = wb.active
for index, row in enumerate(sheet.iter_rows()):
    if index==0:
        continue
    nr = row[0].value
    if nr.upper()=="END":
        break
    data_start = str(row[1].value)[:10]
    data_koniec = str(row[2].value)[:10]
    brutto = f"{row[3].value:.2f}".replace(".",",")
    kup = f"{row[4].value:.2f}".replace(".",",")
    pit = f"{row[5].value:.2f}".replace(".",",")
    netto = f"{row[6].value:.2f}".replace(".",",")
    tytul = row[7].value
    imie_nazwisko = row[8].value
    adres = row[9].value
    miasto = row[10].value
    pesel = row[11].value
