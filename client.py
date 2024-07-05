#########################################################################
#                                                                       #
# << Trabalho 2 ::Manipulação de Arquivos com conexões Cliente/Servidor #
#                                                                       #
# - Nome   :: Rafael Ochôa Mello                                        #  
# - e-mail :: rafaelochoamello@gmail.com                                #
# - Disc.  :: Automação em Programabilidade em Redes                    #
#                                                                       #
#########################################################################

#########################################################################
#                                                                       #
#  - Adapta a aplicação de manipulação de arquivos do trabalho          #
#    anterior, para se utilizar das conexões de socket                  #
#                                                                       #
#########################################################################

import os
import socket

host = "127.0.0.1"          
porta = 1061

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, porta))

def newGameString():
    title = input('Nome:')
    genre = input("Gênero:")
    console = input("Console:")
    finished = input("Finalizado ? <Sim> <Nao> :")
    player = input("Digite seu nick:")
    
    dataSend =f"1;Titulo:{title}|Genero:{genre}|Console:{console}|Finalizado:{finished}|Player:{player}\n"

    client.send(dataSend.encode())
    resp = client.recv(2048).decode()

    if resp == '1':
        print('Jogo cadastrado com sucesso')
    else:
        print('Erro no cadastro no servidor!')

def showAllGames():
    client.send('2'.encode())
    resp = client.recv(1024).decode()
    if resp == '0':
        print('Não foi possível receber a lista de jogos')
    elif resp == '1':
        print('Lista vazia, registre novos jogos')
    else:
        acc = 0
        games = resp.strip().split('\n')
        print("\n<<<<<<<<<<<< Listagem de jogos >>>>>>>>>>>>\n")
        for g in games:
            acc = acc + 1
            aux = handleSplitData(g)
            handleShowData(aux, acc)
        # print(resp)

def handleSplitData(data):
    data = data.strip()
    return data.split("|")    

def handleShowData(game, index):
    print(f"\n|------< Jogo {index} > ------------------------------------")
    print(f"|> {game[0]}\n|> {game[1]}\n|> {game[2]}\n|> {game[3]}\n|> {game[4]}")
    print(f"|-----------------------------------------------------")

def removeGame():
    showAllGames()
    gameID = input('Indique o número do jogo que desejas remover: ')
    dataSend = f'4;{gameID}'
    client.send(dataSend.encode())

    resp = client.recv(2048).decode()

    if resp == '0':
        print('Nenum jogo com este valor foi encontrado...')
    else:
        print('Jogo Removido com sucesso!')

def findGame():
    gameName = str(input("Digite o nome do jogo de deseja pesquisar:")).lower()
    dataSend = f'3;{gameName}'
    client.send(dataSend.encode())

    resp = client.recv(2048).decode()

    if resp == '0':
        print('Nenum jogo com este valor foi encontrado...')
    else:
       print(resp)

###<< User Menu >>########################################################
while True:
    print('\n\nGaming Data - Rafael Ochoa Mello')
    print('1. Inclusão de jogo')
    print('2. Listagem de jogos')
    print('3. Pesquisa por título')
    print('4. Exclusão de jogo')
    print('5. Finalizar\n\n')
    opcao = int(input('Opção: '))
    if opcao == 1:
        newGameString()
    elif opcao == 2:
        showAllGames()
    elif opcao == 3:
        findGame()
    elif opcao == 4:
        removeGame()
    else:
        break