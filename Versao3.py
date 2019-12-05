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
        


def apagarMusica():
    #em artista eu coloquei um '-' pra mostrar que não tem musicas daquele artista
    artista = input('Digite o nome do artista\n')
    arquivo = open('Artistas.txt','r')
    lista = arquivo.readlines()
    arquivo.close()
    Achou = False
    for i in (lista):
        if(i[:-1] == artista):
            print('Esse artista existe')
            Achou = True
        
    if(Achou == False):
        print('Esse artista não existe')
    if(Achou == True):
        musicas = []
        nomeMusica = input('Entre com a musica\n')
        arquivo = open(artista+'.txt','r+')
        arquivo.seek(0,0)
        lista = arquivo.readlines()
        for line in lista:
            line = line[:-1] 
            linha_split = line.split(';')
            musica = {'Nome':linha_split[0],'Artista':linha_split[1],'Genero':linha_split[2]}
            musicas +=[musica]
        print(len(musicas))
        print(musicas)
        arquivo.seek(0,0)
        for i in range(len(musicas)):
            #print(i)
            print(musicas[i]['Nome'])
            print(nomeMusica)
            arquivo = open(artista + '.txt','w')
            if(musicas[i]['Nome'] != nomeMusica):
	      #print("a")
                 arquivo.write(
                     musicas[i]['Nome'] +';'+
                     musicas[i]['Artista'] +';'+ 
                     musicas[i]['Genero']+';'+'\n')
        arquivo.close()

    print("Digite 5 para voltar ao menu")
    opcao = int(input())
    if opcao:
      main()
def atualizarDadosArtista(nome,id):
    arquivo = open('Artistas.txt','r+')
    lista = arquivo.readlines()
    arquivo.close()
    artistas = []
    for line in lista:
        line = line[:-1] 
        linha_split = line.split(';')
        artista= {'Id':linha_split[0],'Nome':linha_split[1],'IdMusicas':linha_split[2]}
        artistas +=[artista]
    for i in range(len(artistas)):
        if(artistas[i]['Nome'] == nome):
            artistas[i]['IdMusicas'] += [id]
    arquivo = open('Artistas.txt','r+')
    arquivo.seek(0,0)
    for i in range (len(lista)):
        arquivo.write(
            artistas[i]['Id'] +';'+
            artistas[i]['Nome']+';'+ 
            artistas[i]['IdMusicas']+';'+'\n')
    
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
            Musica= {'Id':linha_split[0],'Nome':linha_split[1],'Genero':linha_split[2]}
            musicas +=[Musica]
    Achou = False
    for i in range (len(musicas)):
        if(musicas[i]['Nome'] == nomeMusica):
            print('Já existe essa musica')
            Achou = True
    idNovo = ''
    if len(musicas) == 0:
        id = '00000000'
    else:
        id = int(musicas[len(musicas)-1]['Id'])# tranformar essa linha do id
        print(id)
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
    print(len(lista))
    print(lista)
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
            print(id)
            print(idArtista)
        else: idArtista = '00000000'#na hora de contar, converter pra int e somar 1
        print (idArtista)
        letras = ''
        for i in range(len(Nome)):
            if(Nome[i] != ' '):
                letras += Nome[i]
        if letras != ' ':

            arquivo.write(
                     idArtista +';'+
                     Nome+';'+ 
                     " "+';'+'\n')
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
        print('Escolha uma opcao')
        print('1) incluir novo artista')
        print('2) Acresentar nova musica')
        print('3) apagar musica em artista')
        print('4) pesquisar')
        print('5) exibir lista ordenada por musica')
        print('6) sair')
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
                for line in lista:
                    cont+= 1
                    print(cont,line[:-1])#organizar de forma que apareça só o nome
                id = int(input())
                #para acompanhar o indice da lista
                id = id - 1
                if(id != -1):
                    Nome = lista[id][:-1]
                    print(Nome)
                    adcionarMusica(Nome)
                    print('Se deseja adicionar mais uma musica digite 1')
                    print('Caso contrario digite 2')
                    escolha = int(input())
                if id == -1:
                    escolha = 2
        if(operador == 3):
            os.system("clear")
            apagarMusica()
   
main()        

