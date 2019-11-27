# dia 24/11 versao mika
# fiz anotações pra não me perder, não liguem kkkk

import os


def apagarMusica():
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

def criarGenero(nome):
	arquivo = open('Genero.txt','a')
	arquivo.write(nome+'\n')
	arquivo.close()
	print('Genero '+nome+' Criado com sucesso')
	
	print("Digite 5 para voltar ao menu")
	opcao = int(input())
	if opcao:
	  main()
def adcionarMusica():
    # verificando se tem artista, senão já cria
    nomeArtista = input('Digite o nome do artista\n')
    arquivo = open('Artistas.txt','r')
    #Pensar em uma forma de alterar a mensagem (artista já existe, pq nessa função não precisamos dessa informação)
    # mas a função adcionar artista tras essa verificação ... 
    adcionarArtista(nomeArtista,arquivo)
    nome = input('Digite o nome da musica\n')
    arquivo = open('Genero.txt','r')
    # criei um arquivo txt para ter a relação dos generos
    generos = arquivo.readlines()
    cont = -1
    print('Escolha entre a lista de generos')
    print('Se o genero que voce deseja nao esta na lista digite -1')
    for i in generos:
        cont+=1
        print(cont,i[:-1])
    escolha = int(input())
    if(escolha == -1):
        nome = input('Digite o novo genero que deseja adicionar\n')
        criarGenero(nome)
        genero = nome
    if(escolha != -1):
        genero = generos[escolha]
    musica = {'Nome':nome,'Artista':nomeArtista,'Genero':genero[:-1]}
    arquivo = open(nomeArtista + '.txt','a')
    arquivo.write(
        musica['Nome'] +';'+
        musica['Artista'] +';'+ 
        musica['Genero']+';'+'\n')
    print('Musica criada')
    
    print("Digite 5 para voltar ao menu")
    opcao = int(input())
    if opcao:
      main()

def adcionarArtista(Nome,arquivo):
    arquivo.seek(0,0)
    lista = arquivo.readlines()
    print(Nome)
    Achou = False
    for i in (lista):
        if(i[:-1] == Nome):
            print('Já existe esse artista')
            Achou = True
    if(Achou == False):
        arquivo = open('Artistas.txt','a')
        arquivo.write(Nome + '\n')
        arquivo.close()
        print('Artista criado')
        arquivo = open(Nome +'.txt','w')
        arquivo.close()
        
    print("Digite 5 para voltar ao menu")
    opcao = int(input())
    if opcao:
      main()
def main():
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

        if(operador > 6 or operador< 1):
            print('operacao incorreta, volte ao menu')
            contador +=1
            if(contador == 3):
                print('Para ultilizar o sistema faca escolhas entre 1 e 5\n')
        if(operador == 1):
             escolha = 1 
             while(escolha == 1):
                os.system("clear")
                artista = input('Digite o nome do artista\n')
                arquivo = open('Artistas.txt','r')
                adcionarArtista(artista,arquivo)
                print('Deseja adcionar outro artista ?')
                print('1)Se sim')
                print('2)Se não')
                escolha = int(input())
        if(operador == 2):
            os.system("clear")
            escolha = 1
            while(escolha == 1):
                adcionarMusica()
                print('Se deseja adcionar mais uma musica digite 1')
                print('Caso contrario digite 2')
                escolha = int(input())
        if(operador == 3):
            os.system("clear")
            apagarMusica()
   
main()        
