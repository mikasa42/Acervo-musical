
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

    print('\033[1;36m     Ajuste seus fones de ouvido !             ')

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

        valor = trataerro(operador)
        if valor == -2:

            print('Operaçao Invalida ! Tente novamente. ')

            continue

        else:
            
        #tratamento do erro : caso o usuario escreva leras

        # esse tratamento de erro eu tive muitas duvidas de como fazer, e não consegui concluir, mas segue a minha ideia

        #if(type(operador) is str == True):# ver como montar essa linha

         #   print('operacao incorreta, volte ao menu')

         #   operador = int(operador)

         #  continue

            if(operador > 6 or operador < 1):

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

                    valorr = trataerro(opcao)
                    if valorr == -2:

                        print('Operacao Invalida! Tente novamente. ')

                        continue

                    else:
                        
                        if(opcao == 1):

                            os.system('clear')

                            adcionarArtista(artista,arquivo)        
                    
                            print('Deseja adicionar outro artista ?')

                            print('1) Se sim')

                            print('2) Se não')

                            escolha = int(input())
                            valoor = trataerro(escolha)

                            if valoor == -2:

                                print('Operaçao invalida! Tente novamente.')

                                continue

                            else:                        

                                os.system("clear")

                        if opcao == 2:

                            print('Deseja alterar o nome ou ir para o menu ?')

                            print('1) Menu inicial')
                            
                            print('2) Nome')
                            
                            resp = int(input())

                            respp = trataerro(resp)
                            if respp == -2:

                                print('Operaçao Invalida! Tente novamente. ')

                                continue

                            else:
                                
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

                                    valloor = trataerro(opcao)
                                    if valloor == -2:

                                        print('Operaçao invalida! Tnete novamente. ')

                                        continue

                                    else:
                                        
                                    

                                        if(opcao == 1):

                                            adcionarArtista(artista,arquivo)

                                            print('Deseja adicionar outro artista ?')

                                            print('1) Se sim')

                                            print('2) Se não')

                                            escolhaa = int(input())
                                            escolha = trataerro(escolhaa)
                                            if escolhaa == -2:

                                                print('Operaçao Invalida! Tnete novamente. ')

                                                continue

                                            else:
                                                
                                    

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

                        escolhaa = trataerro(escolha)
                        if escolhaa == -1:
                            print('Operaçao invalida! ')
                            continue
                        else:
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

                             valor = trataerro(escolha)
                            if valor == -1:
                                print('Operaçao Invalida!')
                                continue
                            else:


                                if escolha == 1 :

                                    apagarMusica()

                                print('Se deseja apagar mais uma musica digite 1')

                                print('Caso contrario digite 2')

                                escolha = int(input())
                                escolhaa = trataerro(escolha)
                                if escolhaa == -1:
                                    print('Opçao Invalida! ')
                                    continue
                                else:
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
                    opcao = trataerro(opcao)
                    if opcao == -2:
                        print('Opçao Invalida!')
                        continue
                    else:
                        

                        if(opcao == 1):

                            print('Deseja continuar a pesquisa por Artista?')

                            print('Digite:')

                            print('1)Se sim')

                            print('2)se nao')

                            opcao = int(input())
                            opcao = trataerro(opcao)
                            if opcao == -2:
                                print('Operaçao Invalida!')
                                continue
                            else:
                                

                                if(opcao == 1):

                                        pesquisaArtista()



                                if(opcao == 2):

                                    print('Deseja continuar a pesquisa')

                                    print('Digite:')

                                    print('1)Continuar')

                                    print('2)Menu Principal')

                                    escolha = int(input())
                                    escolha = trataerro(escolha)
                                    if escolha == -2:
                                        if elcolha ==-2:
                                            print('Opçao Invalida! ')
                                            continue
                                    else:
                            
                                        if(escolha == 1):

                                            pesquisaArtista()

                                



                            if(opcao == 2):

                                print('Deseja continuar a pesquisa por Musica?')

                                print('Digite:')

                                print('1)Se sim')

                                print('2)se nao')

                                opcao = int(input())
                                opcao = trataerro(opcao)
                                if opcao == -2:
                                    print('Opçao Invalida!')
                                    continue
                                else:
                                    

                                    if(opcao == 1):

                                        pesquisaMusica()

                                    if(opcao == 2):

                                        print('Deseja continuar a pesquisa')

                                        print('Digite:')

                                        print('1)Continuar')

                                        print('2)Menu Principal')

                                        escolha = int(input())

                                        escolha = trataerro(escolha)
                                        if escolha == -2:
                                            print('Opçao Invalida!')
                                            continue
                                        else:
                                            
                                            if(escolha == 1):

                                                pesquisaMusica()

                            if(opcao == 3):

                                print('Deseja continuar a pesquisa por Genero?')

                                print('Digite:')

                                print('1)Se sim')

                                print('2)se nao')

                                opcao = int(input())
                                opcao = trataerro(opcao)
                                if opcao == -2:
                                    print('Opçao Invalida!')
                                    continue
                                else:
                                    

                                    if(opcao == 1):

                                        pesquisaGenero()



                                    if(opcao== 2):

                                        print('Deseja continuar a pesquisa?')

                                        print('Digite:')

                                        print('1)Continuar')

                                        print('2)Menu Principal')

                                        escolha = int(input())
                                        escolha = trataerro(escolha)
                                        if escolha = -2:
                                            print('Opçao Invalida!')
                                            continue
                                        else:
                                            

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
