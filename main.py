#Essa Biblioteca permiti utilizar funções do Sistema operacioanl em Python
import os
#Permiti copiar arquivos, várias funções de manipulação de arquivos e coleções de arquivos. 
import shutil

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

informacao_sistema()

# Entrada das pastas
pastaDeOrigem = input("Digite a pasta de Origem: ").strip('\'"')
pastaDestino = input("Digite a pasta de Destino: ").strip('\'"')

# Verifica se a pasta de origem e a de destino existem
if not os.path.exists(pastaDeOrigem):
    print(f"A pasta de origem '{pastaDeOrigem}' não existe.")
else:
    print(f"Pasta de origem '{pastaDeOrigem}' encontrada.")

if not os.path.exists(pastaDestino):
    print(f"A pasta de destino '{pastaDestino}' não existe. Criando...")
    os.makedirs(pastaDestino, exist_ok=True)
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
mover_arquivos(pastaDeOrigem,pastaDestino)