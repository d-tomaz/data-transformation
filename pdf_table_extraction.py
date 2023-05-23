import tabula
import csv
import os
import zipfile

pdf_path = "Anexo_I.pdf"
csv_path = "Anexo_I.csv"

def replace_csv_data(csv_path, column, replacement):
    temporary_name = "temporary.csv"
    with open(csv_path, "r") as file, open(temporary_name, "w", newline = "") as temporary_file:
        reader = csv.reader(file)
        writer = csv.writer(temporary_file)

        for row in reader:
            updated_row = [cell.replace(column, replacement) if cell == column else cell for cell in row]
            writer.writerow(updated_row)
    
    os.replace(temporary_name, csv_path)

tabula.convert_into(pdf_path, csv_path, pages = "all")

replace_csv_data(csv_path, "OD", "Seg. Odontológica")
replace_csv_data(csv_path, "AMB", "Seg. Ambulatorial")

with zipfile.ZipFile("Teste_Daniel.zip", "w") as zip_file:
    zip_file.write(csv_path)