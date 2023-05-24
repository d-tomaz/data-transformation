import tabula
import csv
import os
import zipfile

# Caminho do arquivo PDF de entrada
pdf_path = "Anexo_I.pdf"

# Caminho do arquivo CSV de saída
csv_path = "Anexo_I.csv"

def replace_csv_data(csv_path, column, replacement):
    """
    Substitui os dados em uma coluna específica do arquivo CSV.

    Args:
        csv_path (str): Caminho do arquivo CSV.
        column (str): Valor da coluna a ser substituída.
        replacement (str): Valor de substituição.

    Returns:
        None
    """
    temporary_name = "temporary.csv"
    with open(csv_path, "r") as file, open(temporary_name, "w", newline="") as temporary_file:
        reader = csv.reader(file)
        writer = csv.writer(temporary_file)

        for row in reader:
            updated_row = [cell.replace(column, replacement) if cell == column else cell for cell in row]
            writer.writerow(updated_row)
    
    os.replace(temporary_name, csv_path)

# Conversão do PDF para CSV
tabula.convert_into(pdf_path, csv_path, pages="all")

# Substituição de dados no arquivo CSV
replace_csv_data(csv_path, "OD", "Seg. Odontológica")
replace_csv_data(csv_path, "AMB", "Seg. Ambulatorial")

# Criação do arquivo zip
with zipfile.ZipFile("Teste_Daniel.zip", "w") as zip_file:
    zip_file.write(csv_path)