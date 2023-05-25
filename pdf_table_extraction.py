import tabula                              # Importa o módulo tabula para extrair dados de tabelas de um arquivo PDF
import csv                                 # Importa o módulo csv para manipular arquivos CSV
import os                                  # Importa o módulo os para interagir com o sistema operacional
import zipfile                             # Importa o módulo zipfile para manipular arquivos compactados em formato ZIP

pdf_path = "Anexo_I.pdf"                   # Define o caminho do arquivo PDF a ser convertido em CSV
csv_path = "Anexo_I.csv"                   # Define o caminho do arquivo CSV resultante da conversão

def replace_csv_data(csv_path, column, replacement):
    # Define um nome temporário para o arquivo CSV modificado
    temporary_name = "temporary.csv"
    
    # Abre o arquivo CSV original para leitura e o arquivo temporário para escrita
    with open(csv_path, "r") as file, open(temporary_name, "w", newline="") as temporary_file:
        reader = csv.reader(file)             # Cria um objeto reader para ler o arquivo CSV
        writer = csv.writer(temporary_file)   # Cria um objeto writer para escrever no arquivo temporário
        
        for row in reader:                    # Itera sobre cada linha no arquivo CSV original
            updated_row = [cell.replace(column, replacement) if cell == column else cell for cell in row]
                                              # Cria uma nova lista de células substituindo os valores da coluna especificada
            writer.writerow(updated_row)      # Escreve a linha atualizada no arquivo temporário
        
    os.replace(temporary_name, csv_path)     # Substitui o arquivo original pelo arquivo temporário

tabula.convert_into(pdf_path, csv_path, pages="all")
                                           # Converte o arquivo PDF em CSV usando o módulo tabula

replace_csv_data(csv_path, "OD", "Seg. Odontológica")
                                           # Substitui o valor "OD" pela string "Seg. Odontológica" no arquivo CSV

replace_csv_data(csv_path, "AMB", "Seg. Ambulatorial")
                                           # Substitui o valor "AMB" pela string "Seg. Ambulatorial" no arquivo CSV

with zipfile.ZipFile("Teste_Daniel.zip", "w") as zip_file:
                                           # Abre um arquivo ZIP chamado "Teste_Daniel.zip" para escrita
    zip_file.write(csv_path)               # Adiciona o arquivo CSV ao arquivo ZIP
