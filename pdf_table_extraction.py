import tabula
import csv
import os
import zipfile

pdf_path = "Anexo_I.pdf"
csv_path = "Anexo_I.csv"

def replace_csv_data(csv_path, column, replacement):
    temporary_name = "temp.csv"
    with open(csv_path, "r") as csv_file, open(temporary_name, "w", newline = "") as temporary_file:
        csv_reader = csv.DictReader(csv_file)
        header = csv_reader.fieldnames

        csv_writer = csv.DictWriter(temporary_file, fieldnames = header)
        csv_writer.writeheader()

        for row in csv_reader:
            row[column] = replacement
            csv_writer.writerow(row)

    os.replace(temporary_name, csv_path)

tabula.convert_into(pdf_path, csv_path, pages = "all")

replace_csv_data(csv_path, "OD", "Seg. Odontológica")
replace_csv_data(csv_path, "AMB", "Seg. Ambulatorial")