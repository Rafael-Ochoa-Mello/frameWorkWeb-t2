#########################################################################
#                                                                       #
# << Trabalho 1 :: Módulos e manipulação de arquivos de texto >>        #
#                                                                       #
# - Nome   :: Rafael Ochôa Mello                                        #  
# - e-mail :: rafaelochoamello@gmail.com                                #
# - Disc.  :: Automação em Programabilidade em Redes                    #
#                                                                       #
#########################################################################

import os
from metodos import *


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
        writeNewGame("games.txt")
    elif opcao == 2:
        loadGames("games.txt")
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