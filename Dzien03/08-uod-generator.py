
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

    with open("../misc/uod-kopia.html", "rt", encoding="UTF8") as fd:
        template = fd.read()
        template = template.replace("{IMIE_NAZWISKO}", imie_nazwisko)
        template = template.replace("{ADRES}", adres)
        template = template.replace("{MIASTO}", miasto)
        template = template.replace("{DATA_PRZELEW}", data_koniec)
        template = template.replace("{UMOWA_NR}", nr)
        template = template.replace("{DATA_ZAWARCIA}", data_start)
        template = template.replace("{KWOTA_BRUTTO}", data_start)
        template = template.replace("{KWOTA_KUP}", kup)
        template = template.replace("{KWOTA_NETTO}", netto)

        file_name = f"out/rachunek_{nr.replace('/','_')}.pdf"
        pdfkit.from_string(template, file_name)

    vars = {
        "{NR_UMOWY}" : nr,
        "{DATA_ZAWARCIA}" : data_start,
        "{TYTUL}" : tytul,
        "{KWOTA_BRUTTO}" : brutto
    }
    docx = Document("../misc/uod_tpl-kopia.docx")
    for p in docx.paragraphs:
        inline = p.runs
        for i in range(len(inline)):
            text = inline[i].text
            for k in vars.keys():
                text = text.replace(k, vars[k])
                inline[i].text = text

    file_name = f"out/umowa_{nr.replace('/', '_')}.docx"
    docx.save(file_name)


