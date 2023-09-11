#trabalhando com arquivos
import teste

try:
    arquivo = open("teste.txt", "x")
except FileExistsError as e:
    pass

arquivoLer = open("teste.txt", "r")
