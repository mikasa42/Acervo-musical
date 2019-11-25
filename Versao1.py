# dia 24/11 versao mika
# fiz anotações pra não me perder, não liguem kkkk
def apagarMusica():
    artista = input('Digite o nome do artista')
    arquivo = open('Artistas.txt','r')
    lista = arquivo.readlines()
    Achou = False
    for i in (lista):
        if(i[:-1] == artista):
            print('Esse artista existe')
            Achou = True
    if(Achou == True):
        musica = input('Entre com a musica')
        #Entrar no arquivo do artista onde tem todas as musicas dele e fazer uma busca por lá
        #Para apagar a musica é só passar os dados do arquivo para dicionario e apagar o indice da lista
        # E atualizar com uma lista nova 
def criarGenero():
    #duvidas nessa parte poisn pode gerar muitos erros a propria pessoa digitando...
def acdionarMusica():
    musicas = []
    musica = {'Nome':nome,'Artista':artista,'Genero':genero}
    # verificando se tem artista, senão já cria
    nomeArtista = input('Digite o nome do artista')
    arquivo = open('Artistas.txt','r')
    adcionarArtista(nomeArtistas,arquivo)
    nome = input('Digite o nome da musica')
    arquivo = open('Genero.txt','r')
    # criei um arquivo txt para ter a relação dos generos
    generos = arquivo.readlines()
    cont = 0
    print('Escolha entre a lista de generos')
    print('Se o genero que voce deseja nao esta na lista digite -1')
    for i in generos:
        print(cont+=1,i[:-1])
    escolha = int(input())
    if(escolha == -1):
        criarGenero()
    genero = genero[escolha]
    musicas+=[musica]
    print('Deseja adcionar mais uma musica?')
    print('1)Se sim ')
    print('2)Se nao')
    escolha = int(input())
    if(escolha == 1):
        adcionarMusica()
    # cada artista tem um arquivo só para as musicas dele ... os campos, nomeMusica, artista, genero(pensei que tinha album)
    # mas aco que voces tiraram...
    arquivo = open(nomeArtista + '.txt','r')
    for i in range(len(musicas)):
    arquivo.write(
      musicas[i]['Nome'] +';'+
      musicas[i]['Artista'] +';'+ 
      musicas[i]['Genero']+';'
      
      '\n')
    print('Musica criada')
def adcionarArtista(Nome,arquivo):
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
        print('Artista criado')
        arquivo = open(Nome +'.txt','w')
    arquivo.close()
def main():
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
            print('operacoa incorreta, volte ao menu')
            contador +=1
            if(contador == 3):
                print('Para ultilizar o sistema faca escolhas entre 1 e 5\n')
        if(operador == 1):
            artista = input('Digite o nome do artista\n')
            arquivo = open('Artistas.txt','r')
            adcionarArtista(artista,arquivo)
            print('Deseja adcionar outro artista ?')
            print('1)Se sim')
            print('2)Se não')
            escolha = int(input())
            #Pensar numa forma de loop para adcionar outro artista, mais de uma vez
            if(escolha == 1):
                arquivo = open('Artistas.txt','r')
                artista = input('Digite o nome do artista\n')
                adcionarArtista(artista,arquivo)
        if(operador == 2):
            adcionarMusica()
        if(operador == 3):
            apagarMusica()
        if(operador == 4):
        if(operador == 5):
main()        
