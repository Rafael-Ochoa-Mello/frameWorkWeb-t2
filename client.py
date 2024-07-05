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
        print(resp)

def format

###<< User Menu >>########################################################
while True:
    print('\n\nGaming Data - Rafael Ochoa Mello')
    print('1. Inclusão de jogo')
    print('2. Listagem de jogos')
    print('3. Pesquisa por título')
    print('4. Exclusão de jogo')
    print('5. Listar finalizados')
    print('6. Gerar arquivo de finalizados')
    print('7. Finalizar\n\n')
    opcao = int(input('Opção: '))
    if opcao == 1:
        newGameString()
    elif opcao == 2:
        showAllGames()
    elif opcao == 3:
        findGame("games.txt")
    elif opcao == 4:
        removeGame("games.txt")
    elif opcao == 5:
        showFinished("games.txt")
    elif opcao == 6:
        finishedCopy("games.txt")
    else:
        break