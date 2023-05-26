# Importando as bibliotecas necessárias
import tabula
import csv
import os
import zipfile

# Caminhos dos arquivos PDF e CSV
pdf_path = 'Anexo_I.pdf'
csv_path = 'Anexo_I.csv'

# Função para substituir dados no arquivo CSV
def replace_csv_data(csv_path, column, replacement):
    # Nome temporário para o arquivo CSV
    temporary_name = 'temporary.csv'
    
    # Abrindo o arquivo CSV original e o arquivo temporário
    with open(csv_path, 'r') as file, open(temporary_name, 'w', newline='') as temporary_file:
        reader = csv.reader(file)  # Leitor do arquivo CSV original
        writer = csv.writer(temporary_file)  # Escritor do arquivo temporário
        
        # Iterando pelas linhas do arquivo CSV original
        for row in reader:
            # Atualizando a linha substituindo o valor da coluna especificada
            updated_row = [cell.replace(column, replacement) if cell == column else cell for cell in row]
            writer.writerow(updated_row)  # Escrevendo a linha atualizada no arquivo temporário
        
    # Substituindo o arquivo CSV original pelo arquivo temporário
    os.replace(temporary_name, csv_path)

# Convertendo o PDF para CSV usando a biblioteca tabula
tabula.convert_into(pdf_path, csv_path, pages='all')

# Substituindo os dados no arquivo CSV
replace_csv_data(csv_path, 'OD', 'Seg. Odontológica')
replace_csv_data(csv_path, 'AMB', 'Seg. Ambulatorial')

# Criando um arquivo zip contendo o arquivo CSV
with zipfile.ZipFile('Teste_Daniel.zip', 'w') as zip_file:
    zip_file.write(csv_path)
