import requests as r 
from colorama import Fore as F 
import os as sistema 
import re, sys
import argparse as arg 
sistema.system('cls' if sistema.name == 'nt' else 'reset')

# CORES
RED = F.RED
WHITE = F.WHITE
YELLOW = F.YELLOW
GREEN = F.GREEN
BLUE = F.BLUE
CYAN = F.CYAN

def arruma(url):
	if url[-1] != "/":
		url = url + "/"
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url

index = r"""{}
    __  __                             ______                   
   / / / /_  ______  ____ ________  __/ ____/________ __      __
  / /_/ / / / / __ \/ __ `/ ___/ / / / /   / ___/ __ `/ | /| / /
 / __  / /_/ / / / / /_/ / /  / /_/ / /___/ /  / /_/ /| |/ |/ / 
/_/ /_/\__,_/_/ /_/\__, /_/   \__, /\____/_/   \__,_/ |__/|__/  
                  /____/     /____/                             
                

              Hungry Craw v1 (BETA) 
              Criado por {}Supr3m0 && W4r1o6k
              {}Equipe: {}Yunkers Crew

              {}Facebook: {}fb/yunkers01
              {}Github: {}@2inf3rnal
              {}Skype: {}inf3rnal.king
              """.format(F.CYAN, F.WHITE, F.CYAN, F.WHITE, F.CYAN, F.WHITE, F.CYAN, F.WHITE, F.CYAN, F.WHITE)
manual = r"""{}--url       {}Alvo (--url www.site.com)
{}--threads   {}Tempo para cada requisição (--threads 10)
{}--salvar    {}Salvar todos diretórios em um arquivo log.txt (--salvar)
""".format(CYAN, WHITE, CYAN, WHITE, CYAN, WHITE)

if len(sys.argv) == 1:
	print(index)
	print(manual)
	exit()

parser = arg.ArgumentParser()
parser.add_argument("--url","-u", action='store')
parser.add_argument("--threads","-t", action="store", type = int, default = "10")
parser.add_argument("--salvar","-s", action="store_true")
param = parser.parse_args()

if not param.url:
	print(index)
	print("{}[ERRO] {}Insira uma URL! (ex: --url www.google.com)".format(RED, WHITE))
	exit()

ok_diretorios = []
url = arruma(param.url)

print(index)
print("{}[+] {}Site alvo: {}".format(GREEN, WHITE, url))
print("{}[+] {}Tempo para cada requisição: {}".format(GREEN, WHITE, param.threads))

try:
	checa = r.get(url, timeout=param.threads)
	if checa.status_code == 200:
		print("{}\n[=] {}Conexão estável.".format(GREEN, WHITE))
	else:
		print("{}[X] {}Conexão rejeitada!".format(RED, WHITE))
		exit()
except Exception as err:
	print("{}[ERRO] {}Aconteceu um erro ao fazer a conexão no site {}\nErro: {}".format(RED, WHITE, url, err))
	exit()

print("\n{}[*] {}Buscando diretórios na página inicial.".format(BLUE, WHITE))

requisicao = r.get(url).text
x_sites = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", requisicao)

if not x_sites:
	print("{}[OPS] {}Nenhum diretório foi encontrado :/.".format(RED, WHITE))
	exit()

for sit in x_sites:
	if sit[6:] in ok_diretorios:
		continue
		# H T T P S : / / 
	if url[9:] in sit:
		ok_diretorios.append(sit)
	elif url[8:] in sit:
		ok_diretorios.append(sit)
	else:
		continue

print("{}    [+] {}Total de diretório(s) encontrado na página inicial: {}".format(GREEN, WHITE, str(len(ok_diretorios))))
input("{}    Pressione {} para listar os diretórios\n".format(WHITE, "Enter"))
for y in ok_diretorios:
	print("{}    [DIR] {}{}".format(YELLOW, WHITE, y))

if param.salvar:
	print("\n{}[*] {}Salvando resultados... (log.txt)".format(BLUE, WHITE))
	arquivo = open("log.txt", "w")
	arquivo.write("::: Hungry Craw :::\nVisite: www.facebook.com/yunkers01/\n\n")
	for linha in ok_diretorios:
		arquivo.write(linha + "\n")
	print("{}[+] {}Salvo!".format(GREEN, WHITE))
print("\n{}[=] {}Busca finalizada :)".format(GREEN, WHITE))
exit()
