
import os
from time import sleep
#Funcao que cria os arquivos necessarios para rodar o programa caso eles nao existam na pasta onde o programa está
def criarArquivo():
    try:
        arquivo = open('Artistas.txt','r+')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open('Artistas.txt','w+')
        
    try:
        arquivo = open('Genero.txt','r+')
        arquivo.close()
    except FileNotFoundError:
        genero = ['Pop','Rock','Rap','Forro','Indie','Sertanejo-Universitario','Funk','Eletronica','Reagge']
        arquivo = open('Genero.txt','w')
        arquivo = open('Genero.txt','r+')
        for i in genero:
            arquivo.write(i+'\n')

    try:    
        arquivo = open('Musicas.txt','r+')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open('Musicas.txt','w+')
def ordena():
    arquivo = open('Musicas.txt','r+')
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    arquivo.close() 
    musicas = []
    cont = 0 
    for line in lista:
        cont +=1
        line = line[:-1] 
        linha_split = line.split(';')
        musica = {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
        musicas +=[musica]   
        aux = ''
        for index1 in range (len (musicas)-1):
                for index2 in range (index1 + 1 , len (musicas)):
                        if musicas[index1]['Nome'] > musicas[index2]['Nome']:
                                aux = musicas[index1]
                                musicas[index1] = musicas[index2]
                                musicas[index2] = aux
    print('lista em ordem alfabetica')
    for i in range(len(musicas)):
        print('Seu atributo identificador:'+musicas[i]['Id']+' /'+
                ' Seu nome :'+musicas[i]['Nome']+' /'+' Seu genero:'+musicas[i]['Genero'])
def pesquisaGenero():
    arquivo = open('Genero.txt','r+')
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    arquivo.close()
    print('\033[1;31m----------------------------------------------')
    print('\033[1;34m     Essa lista a seguir sao seus generos     ')
    print('\033[1;31m----------------------------------------------')
    print('\033[1;35m Se quiser mais musica de algum genero digite o numero correspondente')
    print('\033[1;35m Se sua musica nao esta na lista digite -1 para voltar ao menu inicial')
    cont = 0
    generos = []
    for line in lista:
        cont +=1
        line = line[:-1] 
        print(cont,line)
    id = int(input())
    if(id != -1):
        id = id-1
        genero = lista[id][:-1]
        arquivo = open('Musicas.txt','r+')
        arquivo.seek(0,0)
        lista = arquivo.readlines()
        arquivo.close() 
        musicas = []
        cont = 0 
        for line in lista:
            cont +=1
            line = line[:-1] 
            linha_split = line.split(';')
            musica = {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
            musicas +=[musica]   
        listAux = [] 
        for i in range(len(musicas)):
            if(genero == musicas[i]['Genero']):
                listAux += [musicas[i]]
        for i in range(len(listAux)):
            print('Seu atributo identificador:'+musicas[i]['Id']+
                ' Seu nome :'+musicas[i]['Nome']+' Seu genero:'+musicas[i]['Genero'])
def pesquisaMusica():
    arquivo = open('Musicas.txt','r+')
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    arquivo.close()
    print('\033[1;31m----------------------------------------------')
    print('\033[1;34m     Essa lista a seguir sao suas musicas     ')
    print('\033[1;31m----------------------------------------------')
    print('\033[1;35m Se quiser mais detalhes dessa musica digite o numero correspondente')
    print('\033[1;35m Se sua musica nao esta na lista digite -1 para voltar ao menu inicial')
    cont = 0
    musicas = []
    for line in lista:
        cont +=1
        line = line[:-1] 
        linha_split = line.split(';')
        musica = {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
        musicas +=[musica]
        print(cont,linha_split[1])
    id = int(input())
    if(id == -1):
        print('Sua musica nao existe, voltar ao menu')
    if(id != -1):
        id = id -1
        print('Seu atributo identificador:'+musicas[id]['Id']+
                ' Seu nome :'+musicas[id]['Nome']+' Seu genero:'+musicas[id]['Genero'])
def pesquisaArtista():

    arquivo = open('Artistas.txt','r+')
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    arquivo.close()
    print('\033[1;31m------------------------------------------------------------')
    print("\033[1;34m         Lista de artistas ")
    print('\033[1;31m------------------------------------------------------------')
    print("\033[1;35m Abaixo segue uma lista de de artistas para voce escolher")
    print("\033[1;35m digite o numero correspondente")
    print("\033[1;35m Caso seu artista não esteja aqui, digite (-1),Sendo assim ")
    print("\033[1;35m Voce sera redirecionado para o menu, apartir dai escolha")
    print("\033[1;35m A opcao para criar um novo artista ")
    print('\033[1;31m------------------------------------------------------------')
    cont = 0
    artistas = []
    for line in lista:
        cont+= 1
        line = line[:-1] 
        linha_split = line.split(';')
        artista= {'Id':linha_split[0],'Nome':linha_split[1],'IdMusicas':linha_split[2]}
        artistas +=[artista]
        print(cont,linha_split[1])#organizar de forma que apareça só o nome
    id = int(input())
    id = id -1 #indice da lista artistas, esse id é o artista escolhido pelo usuario.
    idMusica = ''
    for i in range (len(artistas)):
        if(id == i):#caso o id do artista escolhido esteja na lista original do aquivo geral de artistas
            idMusica = artistas[i]['IdMusicas']#pegando o campo idMusicas para buscar suas musicas
    id_split = []
    id_split = idMusica.split(',')  #quebrando esse campo para poder enfim ter o id de todas as musicas daquele artista escolhido
    if(id != -1):
        arquivo = open('Musicas.txt','r+')
        arquivo.seek(0,0)
        lista = arquivo.readlines()
        arquivo.close()
        print('Essa lista a seguir sao suas musicas')#lista de musicas do artista escolhido
        IdAntigo = ''
        cont = 0
        for line in lista:
            cont +=1
            line = line[:-1] 
            linha_split = line.split(';')
            IdAntigo = linha_split[0]
            nome = linha_split[1]
            for i in range (len(id_split)):
                if(IdAntigo == id_split[i]):
                    print(cont,nome)#organizar de forma que apareça só o nome   


def apagarMusica():
    arquivo = open('Artistas.txt','r+')
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    arquivo.close()
    print('\033[1;31m------------------------------------------------------------')
    print("\033[1;34m         Lista de artistas ")
    print('\033[1;31m------------------------------------------------------------')
    print("\033[1;35m Abaixo segue uma lista de de artistas para voce escolher")
    print("\033[1;35m digite o numero correspondente")
    print("\033[1;35m Caso seu artista não esteja aqui, digite (-1),Sendo assim ")
    print("\033[1;35m Voce sera redirecionado para o menu, apartir dai escolha")
    print("\033[1;35m A opcao para criar um novo artista ")
    print('\033[1;31m------------------------------------------------------------')
    cont = 0
    artistas = []
    for line in lista:
        cont+= 1
        line = line[:-1] 
        linha_split = line.split(';')
        artista= {'Id':linha_split[0],'Nome':linha_split[1],'IdMusicas':linha_split[2]}
        artistas +=[artista]
        print(cont,linha_split[1])#organizado de forma que apareça só o nome
    idArtista = int(input())
    idArtista  = idArtista  -1
    idMusica = ''
    for i in range (len(artistas)):
        if(idArtista  == i):
            idMusica = artistas[i]['IdMusicas']
    id_split = []
    id_split = idMusica.split(',')  #campo de artistas idMusica sendo tranformado em lista de ids de musicas do artista desejado
    if(idArtista != -1):
        arquivo = open('Musicas.txt','r+')
        arquivo.seek(0,0)
        lista = arquivo.readlines()
        arquivo.close()
        print('\033[1;31m----------------------------------------------')
        print('\033[1;34m     Essa lista a seguir sao suas musicas     ')
        print('\033[1;31m----------------------------------------------')
        print('\033[1;35m Digite o numero correspondente a sua musica que deseja apagar')
        print('\033[1;35m Caso sua musica nao esteja na lista digite (-1)')
        IdAntigo = ''
        cont = 0
        musicas = []
        for line in lista:
            cont +=1
            line = line[:-1] 
            linha_split = line.split(';')
            musica = {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
            musicas +=[musica]
            IdAntigo = linha_split[0]
            nome = linha_split[1]
            for i in range (len(id_split)):
                if(IdAntigo == id_split[i]):
                    print(cont,nome)#organizar de forma que apareça só o nome
        opcao = int(input())#indice da lista de ids da lista de musicas do artista selecionado
        listAux = []
        if(opcao != -1):
            opcao = opcao -1# acompanhando o indice da lista de ids 
            for i in range(len(musicas)):
                if(id_split[opcao] != musicas[i]['Id']):#id_split é a lista do campo idMusicas do artista
                    listAux += [musicas[i]]
                if(id_split[opcao] == musicas[i]['Id']):
                    print('musica apagada com sucesso')
        arquivo = open('Musicas.txt','w') 
        arquivo.seek(0,0) 
        #lista nova de musicas
        for i in range(len(listAux)):
            arquivo.write(
                listAux[i]['Id'] +';'+
                listAux[i]['Nome'] +';'+ 
                listAux[i]['Genero']+';'+ '\n')
        arquivo.close()
        #idArtista é id do artista escohido
        #idMusica é o id das musicas do artista escolhido
        listAux = []
        for i in range(len(idMusica)):
            if(idMusica[i] != str(id_split[opcao]) and idMusica[i] !=  ',' ):
                    listAux +=[idMusica[i]]

    #atualizando o campo idMusicas do artista
    #depois de ter apagado a musica, deve ser retirado o id da musica apagada do campo idMusicas
        idNovo = ''
        for i in range(len(listAux)):
            idNovo += str(listAux[i])   
        arquivo = open('Artistas.txt','r+')
        arquivo.seek(0,0)
        lista = arquivo.readlines()
        arquivo.close()
        artistas = []
        for line in lista:
            line = line[:-1] 
            linha_split = line.split(';')
            artista= {'Id':linha_split[0],'Nome':linha_split[1],'IdMusicas':linha_split[2]}
            artistas +=[artista]
        idArtista += 1
        for i in range(len(artistas)):
            if(str(idArtista) == artistas[i]['Id']):
                artistas[i]['IdMusicas'] = idNovo
        arquivo = open('Artistas.txt','w') 
        arquivo.seek(0,0) 
        #lista nova de musicas
        for i in range(len(artistas)):
            arquivo.write(
                artistas[i]['Id'] +';'+
                artistas[i]['Nome'] +';'+ 
                artistas[i]['IdMusicas']+';'+ '\n')
        arquivo.close()
    print('Voce sera redirecionado em 5 segundos, aguarde')
    sleep(5)

def atualizarDadosArtista(nome,idNovo):
    arquivo = open('Artistas.txt','r+')
    lista = arquivo.readlines()
    arquivo.close()
    artistas = []
    for line in lista:
        line = line[:-1] 
        linha_split = line.split(';')
        artista= {'Id':linha_split[0],'Nome':linha_split[1],'IdMusicas':linha_split[2]}
        artistas +=[artista]
    posicao = 0
   
    idRef = ''
    for i in range(len(artistas)):
        if(artistas[i]['Nome'] == nome):
            idRef = artistas[i]['IdMusicas']
            posicao = i
    if(len(idRef) == 0):
        idMusica = str(idNovo)
        artistas[posicao]['IdMusicas'] = idMusica
    if(len(idRef) != 0):
        idMusica = idRef +','+str(idNovo)
        artistas[posicao]['IdMusicas'] = idMusica
    arquivo = open('Artistas.txt','r+')
    arquivo.seek(0,0)
    for i in range (len(lista)):
        arquivo.write(
            artistas[i]['Id'] +';'+
            artistas[i]['Nome']+';'+ 
            artistas[i]['IdMusicas']+';'+'\n')
    arquivo.close()
def criarGenero(nome):
    #tratar o erro do enter, e maiusculos e minisculos
	arquivo = open('Genero.txt','a')
	arquivo.write(nome+'\n')
	arquivo.close()
	print('Genero '+nome+' Criado com sucesso')
def adcionarMusica(nomeArtista):
    #chamar funcao para atualizar o idmusica de artista
    nomeMusica = input('Digite o nome da musica\n')
    arquivo = open('Musicas.txt','r+')
    lista = arquivo.readlines()
    arquivo.close()
    musicas = []
    for line in lista:
            line = line[:-1] 
            linha_split = line.split(';')
            Musica = {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
            musicas +=[Musica]
    Achou = False
    for i in range (len(musicas)):
        if(musicas[i]['Nome'] == nomeMusica):
            print('Já existe essa musica')
            Achou = True
    idNovo = ''
    #nessa parte estou pegando o ulltimo id da musica
    #quando adicionar uma nova musica o id dela sera o ultimo id + 1
    if len(musicas) == 0:
        id = 1
        idNovo = str(id)
    else:
        id = int(musicas[len(musicas)-1]['Id']) #transformar essa linha do id
        id = id+1
        idNovo = str(id)
    print (id)
    if(Achou == False):
        arquivo = open('Genero.txt','r+')
        generos = arquivo.readlines()
        cont = 0
        print('Escolha entre a lista de generos')
        print('Se o genero que voce deseja nao esta na lista digite -1')
        for i in generos:
            cont+=1
            print(cont,i[:-1])
        escolha = int(input())
    # para acompanhar o indice da lista 
        escolha = escolha -1
        if(escolha == -1):
            nome = input('Digite o novo genero que deseja adicionar\n')
            nome = nome.strip()
            nome = nome.casefold()
            criarGenero(nome)
            genero = nome
        if(escolha != -1):
            genero = generos[escolha]
            arquivo = open('Musicas.txt','a')
            arquivo.write(
                idNovo+';'+
                nomeMusica+';'+ 
                genero[:-1]+';'+'\n')
            print('Musica criada')
        atualizarDadosArtista(nomeArtista,idNovo)
        arquivo.close()
    print('Voce sera redirecionado em 5 segundos, aguarde')
    sleep(5)

def adcionarArtista(Nome,arquivo):
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    arquivo.close()
    print(Nome)
    artistas = []
    for line in lista:
            line = line[:-1] 
            linha_split = line.split(';')
            artista= {'Id':linha_split[0],'Nome':linha_split[1],'IdMusicas':linha_split[2]}
            artistas +=[artista]
    Achou = False
    for i in artistas:
        if(i['Nome'] == Nome):
            print('Já existe esse artista')
            Achou = True
    if(Achou == False):
        arquivo = open('Artistas.txt','a')
        if len(artistas) != 0:
            idArtista = artistas[len(artistas)-1]['Id']
            id = int(idArtista)
            id = id + 1
        if len(artistas) == 0 : 
            id = 1
        letras = ''
        for i in range(len(Nome)):
            if(Nome[i] != ' '):
                letras += Nome[i]
        if letras != ' ':
            arquivo.write(
                     str(id) +';'+
                     Nome+';'+ 
                     ""+';'+'\n')
            print('Artista criado')
        arquivo.close()
    print('Voce sera redirecionado em 5 segundos, aguarde')
    sleep(5)
def trataerro(nome):
    nome= nome.strip()
    alfabeto = ['a' , 'b' , 'c', 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'x' , 'w' , 'y' , 'z' ,'ç' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'X' , 'W' , 'Y' , 'Z' , 'Ç' , '!' , '@' , '$' , '%' , '¨' , '&' , ' * ' , '(' ,' )' , ' # ' ,  '_' , '+' ,   '/' , '*' , '-' , ':' , '>' , '<' ,  ';'   ,   '.'  ,  '}' , '{' , '^' , '~' , ']' , '[' , 'º' , 'ª' , '§' , '¬' , '¢' , '£' , '³' , '²' , '¹' , ]
    numero = ['0','1','2','3','4','5','6','7','8','9']
   
    for v in alfabeto :
        if v == nome:
            i = -2
            return i
    for l in numero:
        if l == nome:
            valor = int(nome)
            print(valor)
            return valor


def main():
    criarArquivo()
    os.system("clear")
    operador = 1
    while(operador !=6):
        print('\033[1;31m----------------------------------------')
        print('\033[1;36m            MENU PRINCIPAL              ')
        print('\033[1;31m----------------------------------------')

        print('\033[1;34m          ESCOLHA UMA OPÇÃO             ')
        print('\033[1;34m 1-''\033[1;35m Incluir novo artista                ')
        print('\033[1;34m 2-''\033[1;35m Acresentar nova musica              ')
        print('\033[1;34m 3-''\033[1;35m Apagar musica em artista            ')
        print('\033[1;34m 4-''\033[1;35m Pesquisar                           ')
        print('\033[1;34m 5-''\033[1;35m Exibir lista ordenada por musica    ')
        print('\033[1;34m 6-''\033[1;35m Sair                                ')
        print('\033[1;31m----------------------------------------')
        
        operador = int(input())
        #tratamento do erro : caso o usuario escreva leras
        valor = trataerro(operador)
        if(valor == -2):
            print('operacao incorreta, volte ao menu')
            operador = 10 # pois
            continue
         if(valor != -2):
            if(valor > 6 or valor < 1):
            print('operacao incorreta, volte ao menu')
            continue
        if(operador == 1):
             escolha = 1 
             while(escolha == 1):
                os.system("clear")
                artista = input('Digite o nome do artista(No minimo 1 caractere)\n')
                artista = artista.casefold()
                artista = artista.strip()
                arquivo = open('Artistas.txt','r+')
                print('Confimacao, este é o artista desejado?'+ ' '+artista)
                print('1) Se sim')
                print('2) Se não')
                opcao = int(input())
                if(opcao == 1):
                    os.system('clear')
                    adcionarArtista(artista,arquivo)
                    print('Deseja adicionar outro artista ?')
                    print('1) Se sim')
                    print('2) Se não')
                    escolha = int(input())
                    os.system("clear")
                if opcao == 2:
                    print('Deseja alterar o nome ou ir para o menu ?')
                    print('1) Menu inicial')
                    print('2) Nome')
                    resp = int(input())
                    if(resp == 1):
                        escolha = 2
                    if(resp == 2):
                        print('Digite o nome do artista desejado de novo')
                        artista = input() 
                        artista = artista.casefold()
                        artista = artista.strip()
                        print('Confimacao, este é o artista desejado?'+ " " + artista)
                        print('1) sim')
                        print('2) Nao')
                        opcao = int(input())
                        if(opcao == 1):
                            adcionarArtista(artista,arquivo)
                            print('Deseja adicionar outro artista ?')
                            print('1) Se sim')
                            print('2) Se não')
                            escolha = int(input())
                        
        if(operador == 2):
            os.system("clear")
            escolha = 1
            while(escolha == 1):
                arquivo = open('Artistas.txt','r+')
                arquivo.seek(0,0)
                lista = arquivo.readlines()
                arquivo.close()
                print('\033[1;31m------------------------------------------------------------')
                print("\033[1;34m         Lista de artistas ")
                print('\033[1;31m------------------------------------------------------------')
                print("\033[1;35m Abaixo segue uma lista de de artistas para voce escolher")
                print("\033[1;35m digite o numero correspondente")
                print("\033[1;35m Caso seu artista não esteja aqui, digite (-1),Sendo assim ")
                print("\033[1;35m Voce sera redirecionado para o menu, apartir dai escolha")
                print("\033[1;35m A opcao para criar um novo artista ")
                print('\033[1;31m------------------------------------------------------------')
                cont = 0
                nome = []
                for line in lista:
                    cont+= 1
                    line = line[:-1] 
                    linha_split = line.split(';')
                    print(cont,linha_split[1])#organizar de forma que apareça só o nome
                    nome +=[linha_split[1]]
                id = int(input())
                #para acompanhar o indice da lista
                
                if(id != -1):
                    id = id -1
                    Nome = nome[id] 
                    os.system('clear')
                    adcionarMusica(Nome)
                    os.system('clear')
                    print('Se deseja adicionar mais uma musica digite 1')
                    print('Caso contrario digite 2')
                    escolha = int(input())
                    os.system('clear')
                if id == -1:
                    escolha = 2

        if(operador == 3):
            os.system("clear")
            escolha = 1
            while(escolha == 1):
                        print('Deseja continuar nessa operacao?')
                        print('1)Se sim')
                        print('2)Se nao,voltara para o menu incial')
                        escolha = int(input())
                        if escolha == 1 :
                            apagarMusica()
                        print('Se deseja apagar mais uma musica digite 1')
                        print('Caso contrario digite 2')
                        escolha = int(input())
                        os.system("clear")
        if(operador == 4):
            os.system("clear")
            escolha = 1
            while(escolha == 1):
                print('\033[1;31m------------------------------------------------------')
                print('\033[1;34m Deseja pesquisar por, caso deseje sair digite(-1)')
                print('\033[1;31m------------------------------------------------------')
                print('\033[1;34m 1-''\033[1;35m Por Artista')
                print('\033[1;34m 2-''\033[1;35m Por Musica')
                print('\033[1;34m 3-''\033[1;35m Por Genero')
                opcao = int(input())
                if(opcao == 1):
                    print('Deseja continuar a pesquisa por Artista?')
                    print('Digite:')
                    print('1)Se sim')
                    print('2)se nao')
                    opcao = int(input())
                    if(opcao == 1):
                        pesquisaArtista()

                    if(opcao == 2):
                        print('Deseja continuar a pesquisa')
                        print('Digite:')
                        print('1)Continuar')
                        print('2)Menu Principal')
                        escolha = int(input())
                        if(escolha == 1):
                            pesquisaArtista()
                

                if(opcao == 2):
                    print('Deseja continuar a pesquisa por Musica?')
                    print('Digite:')
                    print('1)Se sim')
                    print('2)se nao')
                    opcao = int(input())
                    if(opcao == 1):
                        pesquisaMusica()
                    if(opcao == 2):
                        print('Deseja continuar a pesquisa')
                        print('Digite:')
                        print('1)Continuar')
                        print('2)Menu Principal')
                        escolha = int(input())
                        if(escolha == 1):
                            pesquisaMusica()
                if(opcao == 3):
                    print('Deseja continuar a pesquisa por Genero?')
                    print('Digite:')
                    print('1)Se sim')
                    print('2)se nao')
                    opcao = int(input())
                    if(opcao == 1):
                        pesquisaGenero()

                    if(opcao== 2):
                        print('Deseja continuar a pesquisa?')
                        print('Digite:')
                        print('1)Continuar')
                        print('2)Menu Principal')
                        escolha = int(input())
                        if(escolha == 1):
                            pesquisaGenero()
                if(opcao == -1):
                    escolha = 2
                sleep(5)
                os.system("clear")
        if(operador == 5):
            os.system('clear')
            ordena()

main()        

