# dia 24/11 versao mika

import os


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
    print('Essa lista a seguir sao seus generos')
    print('Se quiser mais musica de algum genero digite o numero correspondente')
    print('Se sua musica nao esta na lista digite -1 para voltar ao menu inicial')
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
    print('Essa lista a seguir sao suas musicas')
    print('Se quiser mais detalhes dessa musica digite o numero correspondente')
    print('Se sua musica nao esta na lista digite -1 para voltar ao menu inicial')
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
    print(" Abaixo segue uma lista de de artistas para voce escolher")
    print(" digite o numero correspondente")
    print(" Caso seu artista não esteja aqui, digite (-1),Sendo assim ")
    print(" voce sera redirecionado para o menu, apartir dai escolha")
    print(" a opcao para criar um novo artista ")
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
    id = id -1
    idMusica = ''
    for i in range (len(artistas)):
        if(id == i):
            idMusica = artistas[i]['IdMusicas']
    id_split = []
    id_split = idMusica.split(',')  
    if(id != -1):
        arquivo = open('Musicas.txt','r+')
        arquivo.seek(0,0)
        lista = arquivo.readlines()
        arquivo.close()
        print('Essa lista a seguir sao suas musicas')
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


def apagarMusica(nomeArtista):
    print('aaaaaaaaaa')
    arquivo = open('Artistas.txt','r')
    lista = arquivo.readlines()
    arquivo.close()
    artistas =[]
    #Pegando os artistas
    for line in lista:
            line = line[:-1] 
            linha_split = line.split(';')
            artista = {'Id':linha_split[0],'Nome':linha_split[1],'IdMusica':linha_split[2]}
            artistas +=[artista]
    IdMusica = ''
    musicas = []
    Achou = False
    #conferindo se ele existe
    for i in range (len(artistas)):
        if(artistas[i]['Nome'] == nomeArtista):
            Achou = True
            IdMusica = artistas[i]['IdMusica'] #pegando o idMusicas para buscar as musicas daquele artista
    if(Achou == False):
        print('Algo deu errado')
    if(Achou == True):
        arquivo = open('Musicas.txt','r+')
        lista = arquivo.readlines()
        arquivo.close()
        #pegando a lista de musicas do programa
        for line in lista:
            line = line[:-1] 
            linha_split = line.split(';')
            musica = {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
            musicas +=[musica]
         
        id_split = IdMusica.split(',')
            
        print(id_split)
        listaMus = []
        print(len(musicas))
        print(musicas)
        #pegando as musicas do artista selecionado
        for i in range(len(id_split)):#mudar para len musicas
            if(musicas[i]['Id'] == id_split[i]):
                listaMus +=[musicas[i]]
        print('aaaaa',listaMus)
        print('Digite o numero correspondente a sua musica desejada')
        print('Caso ela não esteja na lista digite (-1), e voce sera redirecionado ao menu')

        #mostrando a lista de musicas do artista
        for i in range(len(listaMus)):
            print(i,listaMus[i]['Nome'])
        resp = int(input())
        listAux = []
        print(musicas)
        if(resp != -1):
            for i in range(len(listaMus)):
                if( i != resp):
                    listAux += [musicas[i]]
            print('Musica apagada com sucesso')
            arquivo = open('Musicas.txt','r+') 
            arquivo.seek(0,0) 
            #lista nova de musicas
            print(listAux)     
            for i in range(len(listAux)):
                 arquivo.write(
                     listAux[i]['Id'] +';'+
                     listAux[i]['Nome'] +';'+ 
                     listAux[i]['Genero']+';'+'\n')
            arquivo.close()
#atualizar o arquivo artistas com a alteracaodas musicas
    print("Digite 5 para voltar ao menu")
    opcao = int(input())
    if opcao:
      main()
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
    #tratar o erro de minusculos e maiusculos
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
    print("Digite 5 para voltar ao menu")
    opcao = int(input())
    if opcao:
      main()



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
            id = int(idArtista)#nao esta funcionando !
            id = id + 1
        if len(artistas) == 0 : 
            id = 1#na hora de contar, converter pra int e somar 1
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
        #testando o caso do enter, mas não consegui resolver
        if letras == ' ':
            print('hahahahaha')
        arquivo.close()
def main():
    criarArquivo()
    os.system("clear")
    operador = 1
    while(operador !=6):
        print('* * * * * * * * * * * * * * * * * * * *')
        print('*Escolha uma opcao                    *')
        print('*1) incluir novo artista              *')
        print('*2) Acresentar nova musica            *')
        print('*3) apagar musica em artista          *')
        print('*4) pesquisar                         *')
        print('*5) exibir lista ordenada por musica  *')
        print('*6) sair                              *')
        print('* * * * * * * * * * * * * * * * * * * *')
        operador = int(input())

        if(operador > 6 or operador < 1):
            print('operacao incorreta, volte ao menu')
            continue
        
        if(operador == 1):
             escolha = 1 
             while(escolha == 1):
                os.system("clear")
                artista = input('Digite o nome do artista(No minimo 3 caracteres)\n')
                arquivo = open('Artistas.txt','r+')
                print('Confimacao, este é o artista desejado?'+artista)
                print('1) Se sim')
                print('2) Se não')
                opcao = int(input())
                while opcao == 2:
                    print('Deseja alterar o nome ou ir para o menu ?')
                    print('1) Menu')
                    print('2) Nome')
                    opcao = int(input())
                    if(opcao == 2):
                        print('Digite o nome do artista desejado de novo')
                        artista = input()
                        print('Confimacao, este é o artista desejado?'+artista)
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
                print(" Abaixo segue uma lista de de artistas para voce escolher")
                print(" digite o numero correspondente")
                print(" Caso seu artista não esteja aqui, digite (-1),Sendo assim ")
                print(" voce sera redirecionado para o menu, apartir dai escolha")
                print(" a opcao para criar um novo artista ")
                cont = 0
                nome = []
                for line in lista:
                    cont+= 1
                    line = line[:-1] 
                    linha_split = line.split(';')
                    print(cont,linha_split[1])#organizar de forma que apareça só o nome
                    nome +=[linha_split[1]]
                print(linha_split)
                id = int(input())
                #para acompanhar o indice da lista
                
                if(id != -1):
                    id = id -1
                    Nome = nome[id] 
                    print(Nome)
                    adcionarMusica(Nome)
                    print('Se deseja adicionar mais uma musica digite 1')
                    print('Caso contrario digite 2')
                    escolha = int(input())
                if id == -1:
                    escolha = 2
        if(operador == 3):
            os.system("clear")
            escolha = 2
            while(escolha == 2):
                arquivo = open('Artistas.txt','r+')
                arquivo.seek(0,0)
                lista = arquivo.readlines()
                arquivo.close()
                print(" Abaixo segue uma lista de de artistas para voce escolher")
                print(" digite o numero correspondente")
                print(" Caso seu artista não esteja aqui, digite (-1), pois ele nao existe,Sendo assim ")
                print(" voce sera redirecionado para o menu, apartir dai escolha")
                print(" a opcao para criar um novo artista ")
                cont = 0
                nome = []
                for line in lista:
                    cont+= 1
                    line = line[:-1] 
                    linha_split = line.split(';')
                    print(linha_split[1])
                    print(cont,linha_split[1])#organizar de forma que apareça só o nome
                    nome +=[linha_split[1]]
                id = int(input())
                #para acompanhar o indice da lista
                id =id -1
                if(id != -1):
                    print('Deseja selecionar esse artista mesmo?')
                    print('1)Se sim')
                    print('2)Se nao')
                    escolha = int(input())
                    if(escolha == 2):
                        print('Deseja continuar nessa operacao?')
                        print('1)Se sim')
                        print('2)Se nao,voltara para o menu')
                        opcao = int(input())
                        if opcao == 1:
                            continue
                        if opcao == 2 :
                            os.system("clear")
                            main()
                    print(id)
                    id = id -1
                    Nome = nome[id] 
                    print(Nome)
                    apagarMusica(Nome)
                    print('Se deseja apagar mais uma musica digite 2')
                    print('Caso contrario digite 1')
                    escolha = int(input())
        if(operador == 4):
            os.system("clear")
            escolha = 1
            while(escolha == 1):
                print('Deseja pesquisar por')
                print('1)Por Artista')
                print('2)Por Musica')
                print('3)Po Genero')
                opcao = int(input())
                if(opcao == 1):
                    print('Deseja continuar a pesquisa por Artista?')
                    print('Digite:')
                    print('1)Se sim')
                    print('2)se nao')
                    escolha = int(input())
                    if(escolha == 2):
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
                    escolha = int(input())
                    if(escolha == 2):
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
                    escolha = int(input())
                    if(escolha == 2):
                        print('Deseja continuar a pesquisa?')
                        print('Digite:')
                        print('1)Continuar')
                        print('2)Menu Principal')
                        escolha = int(input())
                        if(escolha == 1):
                            pesquisaGenero()
                if(operador == 5):
                    os.system('clear')
                    ordena()

main()        

