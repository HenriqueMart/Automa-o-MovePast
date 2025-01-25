#Essa Biblioteca permiti utilizar funções do Sistema operacioanl em Python
import os
#Permiti copiar arquivos, várias funções de manipulação de arquivos e coleções de arquivos. 
import shutil
#Permiti que acesse os diretório e manipular os diretório
from pathlib import Path

#Atributos
pastaDeOrigem = "Não Definido"
pastaDestino = "Não Definido"

def informacao_sistema():
    os.system('cls')
    print("============== Automação de Sistema =================")
    print("======= Sobre o Sistema =========")
    #Permiti pegar o nome do Dispositivo utilizando
    username = os.environ.get('USERNAME')
    print(f"Usuário Acessando o Sistema: {username}")
    print("Desenvolvido por José Henrique Martins")
    print("Versão: 1.0")
    print("==========================")

#Pegando a pasta do sistema Operacional
pastaDoSistema = Path.home() / 'MovePast.txt'
#Verificação

#Verifica ser o arquivo na pasta principal do sistema no nome do arquivo salvo. Verifica ser essa pasta está criada
ConfiguracaoCriada = os.path.exists(pastaDoSistema)

#Verifica ser o usuário deseja alterar
if(ConfiguracaoCriada):
    resposta = input("Deseja Carregar configuração Salva?\n[1] Sim\n[2] Não\nDigita o número a baixo:")

#Caso existe e o usuário deseja pegar informação ele carrega todas as informações salvas
if(ConfiguracaoCriada and resposta == '1'):
    #Pega o arquivo em cada linha tirando espaço linhas aspas e quebra de linha
    with open(pastaDoSistema, 'r') as arquivos:
            pastaDeOrigem = arquivos.readline().strip().strip('\'"')
            pastaDestino = arquivos.readline().strip().strip('\'"')
else:
    #Caso ele não tenha salvo, solicita um novo endereço 
    os.system('cls')
    informacao_sistema()
    print("-------------------Configuração-----------")
    # Entrada das pastas
    pastaDeOrigem = input("Digite a pasta de Origem: ").strip('\'"')
    pastaDestino = input("Digite a pasta de Destino: ").strip('\'"')

    if(input("Deseja salvar essa configuração?\n[1] Sim\n[2] Não\nDigita o número a baixo:") == '1'):
        print("Salvando Configuração...")
        #Salvo o arquivo no tipo 'w' enviando como string e com quebra de linha
        with open(pastaDoSistema, 'w') as arquivos:
            arquivos.write(str(pastaDeOrigem) +  "\n" + str(pastaDestino))

# Verifica se a pasta de origem e a de destino existem
if not os.path.exists(pastaDeOrigem):
    print(f"A pasta de origem '{pastaDeOrigem}' não existe.")
else:
    print(f"Pasta de origem '{pastaDeOrigem}' encontrada.")

if not os.path.exists(pastaDestino):
    print(f"A pasta de destino '{pastaDestino}' não existe.")
else:
    print(f"Pasta de destino '{pastaDestino}' encontrada.")

# Função para mover os arquivos
def mover_arquivos(pasta_origem, pasta_destino):
    os.system('cls')
    # Pegando Informações do sistema
    informacao_sistema()

    print("============ Diretórios Informados ================")
    print(f"Pasta de Origem: {pasta_origem}")
    print(f"Pasta de Destino: {pasta_destino}")
    print("==============================")

    #Verificando pastas e SubPasta para pegar todos os arquivos em formato PDF para enviar para o diretório de Destino
    #os.walk -> Ele percorre a árvore do diretório, ele gera os nomes dos (Diretório, SubPasta, Arquivo)
    #Verifico como se fosse matriz de diretório com todos as suas subpastas com todos os seus arquivos utilizando for
    for diretorio, subpasta, arquivos in os.walk(pasta_origem):
        #Pego arquivos por arquivos para transferir os PDF
        for arquivo in arquivos:
            #Join -> Concatenar os segmentos ou parâmetros passados
            origem = os.path.join(diretorio, arquivo)
            destino = os.path.join(pasta_destino, arquivo)
            
            if arquivo.endswith(".pdf"):  # Verifica se o arquivo é PDF retorna um valor booleano
                # Verifica se o arquivo já existe no destino
                if os.path.exists(destino):
                    print(f"Arquivo '{arquivo}' já existe na pasta de destino. Ignorando.")
                else:
                    #Caso não exita esse arquivos, realizo a cópia do arquivo de origim para o destino
                    shutil.copy2(origem, destino)
                    print(f"Arquivo '{arquivo}' copiado para a pasta de destino: '{destino}'")


# Chama a função para mover os arquivos
mover_arquivos(pastaDeOrigem, pastaDestino)