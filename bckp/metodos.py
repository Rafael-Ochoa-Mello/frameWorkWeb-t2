import os
from pathlib import Path

FILE_PATH = Path(__file__).parent

def checkFile(fileName):
    path = FILE_PATH / fileName
    return os.path.isfile(path)


def showRawData(fileName):
    try:
        with open(f"{FILE_PATH}/{fileName}", 'r') as file:
            data = file.readlines()
            for d in data:
                print(d.strip())
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')

def showNotFound(acc, dataSize):
    if acc >= dataSize:
        print(f"Nenhum jogo foi encontrado...")

###### Game Removal methods #############################################
def removeGame(fileName):
    loadGames(fileName)
    
    gameID = int(input("Informe o número do jogo que desejas remover: "))

    if gameID <= 0:
        return

    if checkFile(fileName):
        rawData = open(f"{FILE_PATH}/{fileName}")
        data = rawData.readlines()
        rawData.close()

        if gameID > len(data):
            print("Invalido, apresente um numero correspondente")
            return 
        
        data.pop(gameID-1)
        
        rawData = open(f"{FILE_PATH}/{fileName}", 'w')
        rawData.write(''.join(data))
        rawData.close()
        print(f"Jogo de número {gameID} removido com sucesso!")
    return
        

###### Game Storing methods #############################################
def newGameString():
    title = input('Nome:')
    genre = input("Gênero:")
    console = input("Console:")
    finished = input("Finalizado ? <Sim> <Nao> :")
    return(f"Titulo:{title}|Genero:{genre}|Console:{console}|Finalizado:{finished}\n")

def writeNewGame(fileName):
    try:
        with open(f"{FILE_PATH}/{fileName}", 'a') as file:
            newGame = newGameString()
            file.write(newGame)
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')

###### loadGames  (display) ##################################
def loadGames(fileName):
    acc = 0
    finished = 0
    try:
        with open(f"{FILE_PATH}/{fileName}", 'r') as file:
            print("\n<<<<<<<<<<<< Listagem de jogos >>>>>>>>>>>>")
            data = file.readlines()
            for d in data:
                acc = acc+1
                game = handleDataOnShow(d)
                finished = isFinished(game, finished)
                showGame(game, acc)
            print(f"\nTotal de jogos registrados :: {acc}")
            print(f"Total de jogos finalizados :: {finished}")
            showFinishedPercentage(acc, finished)
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')


def handleDataOnShow(data):
    data = data.strip()
    return data.split("|")    


def showGame(game, index):
    print(f"\n|------< Jogo {index} > ------------------------------------")
    print(f"|> {game[0]}\n|> {game[1]}\n|> {game[2]}\n|> {game[3]}")
    print(f"|-----------------------------------------------------")


def isFinished(data, acc):
    finished = data[3].split(":")
    if finished[1] == 'Sim':
        return acc+1
    return acc


def showFinishedPercentage(games, finished):
    if(games > 0 and finished > 0):
        perc = (finished / games) * 100 
        print("\nDe todos os jogos, %.2f foram finalizados!" % perc)         
        
def mainMenu():
    print("Bem vindo a biblioteca de jogos (!)")
    
###### FindByName ##################################
def findGame(fileName):
    gameName = str(input("Digite o nome do jogo de deseja pesquisar:")).lower()
    acc = 0
    try:
        with open(f"{FILE_PATH}/{fileName}", 'r') as file:
            data = file.readlines()
            for d in data:
                acc = acc + 1
                game = handleDataOnShow(d)
                titlePart = game[0].split(":")
                title = titlePart[1].lower()
                if gameName == title:
                    showGame(game, acc)
                    return
            showNotFound(acc, len(data))
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')

###### ShowOnlyFinished ##################################
def showFinished(fileName):
    acc = 0
    try:
        with open(f"{FILE_PATH}/{fileName}", 'r') as file:
            print("\n<<<<<<<<<<<< Jogos Finalizados >>>>>>>>>>>>")
            data = file.readlines()
            for d in data:
                acc = acc+1
                game = handleDataOnShow(d)
                finished = isFinished(game, 0)
                if finished > 0:
                    showGame(game, acc)
            showNotFound(acc, len(data))
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')

###### Insert finished game on new file  ##################################
def finishedCopy(fileName):
    if checkFile(fileName):
        oldFinished = open(f"{FILE_PATH}/finished.txt")
        finishedList = oldFinished.readlines()
        oldFinished.close()

    try:
        with open(f"{FILE_PATH}/{fileName}", 'r') as file:
            data = file.readlines()
            for d in data:
                game = handleDataOnShow(d)
                finished = isFinished(game, 0)
                if finished > 0:
                    finishedList.append(d)
            file.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')

    oldFinished = open(f"{FILE_PATH}/finished.txt", 'w')
    oldFinished.write(''.join(finishedList))
    oldFinished.close()
        

