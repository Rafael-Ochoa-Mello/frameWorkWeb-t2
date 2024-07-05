import os
from pathlib import Path

FILE_PATH = Path(__file__).parent

# - Lê e printa um arquivo, aqui vemos uma versão
# alternativa de  verificação de existência do 
# arquivo.

# PS : O método strip arruma os espeços em branco
# de um parágrafo.
def readTextFile(fileName):
   # lines = 0
    try:
        with open(f"{FILE_PATH}/{fileName}", 'r') as file:
            data = file.readlines()
            for d in data:
                print(d.strip())
                #lines = lines+1
            #print(f"total de linhas {lines}")
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')

# - Verifica a existência do arquivo uma segunda
# forma pode ser vista no método 'readTextFile'

def checkFile(fileName):
    path = FILE_PATH / fileName
    return os.path.isfile(path)