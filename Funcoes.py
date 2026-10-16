def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_nova = [0]*tamanho
    lista_nova[0] = [linha,coluna]
    if orientacao == "vertical":
        i = 1
        while i<tamanho: 
            linha+=1
            lista_nova[i] = [linha,coluna]
            i+=1
    if orientacao == "horizontal":
            i = 1
            while i<tamanho: 
                coluna+=1
                lista_nova[i] = [linha,coluna]
                i+=1
    return lista_nova

#funcao feita para definir as posicoes do navio na grade, mostra o ponto inicial de linha e coluna,
#  se é vertical ou horizontal e o tamanho

def preenche_frota (frota, nome_navio ,  linha, coluna, orientacao,tamanho):
    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha,coluna,orientacao,tamanho))
    else:
        frota[nome_navio]= [define_posicoes(linha,coluna,orientacao,tamanho)]
    return frota

#funcao para armazenar os navios e suas respectivas posicoes, usando a funcao define_posicoes

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
          tabuleiro[linha][coluna] == 'X'
    else:
         tabuleiro[linha][coluna] == '-'
    return tabuleiro

# funcao que retorna se o barco foi acertado ou nao pelo adversario

def posiciona_frota(frota):
    i=0
    tabuleiro=[]
    while i < 10: 
        linha= [0] * 10 
        tabuleiro.append(linha)
        i+=1
        return tabuleiro

    for nome_navio in frota:
        f=0
        lista_navio= frota[nome_navio]
        while f < len(lista_navio):
            a=0
            while a < len(lista_navio[f]):
                linha = lista_navio[f][a][0]
                coluna = lista_navio[f][a][1]
                tabuleiro[linha][coluna]= 1
                a+=1
            f+=1

    return tabuleiro

def afundados(dicio_navios,tabuleiro):
    navio_afundado = 0
    for navio,posicao in dicio_navios.items(): 
        i = 0 
        while i<len(posicao):
            f = 0 
            contagem = 0 
            while f<len(posicao[i]):
                x = posicao[i][f][0]
                y = posicao[i][f][1]
                if tabuleiro[x][y] == "X":
                    contagem+=1
                f+=1
            if contagem == f:
                navio_afundado+=1
            i+=1

    return navio_afundado

# funcao para descobrir os atuais navios afundados, recebe um dicionario de navios e a situacao atual do navio
# e retorna quantos navios estao afundados

def posicao_valida(dicio_navios,linha,coluna,orientacao,tamanho):
    if coluna>9 or linha>9:
        return False
    lista = define_posicoes(linha,coluna,orientacao,tamanho)
    for y in lista:
        if any(numero>9 for numero in y) == True:
            return False

    for posicao in dicio_navios.values():
        for navios in posicao:
            for navio in navios:
                if navio in lista:
                    return False

    return True

# para ver se o navio que será posicionado pode ser posicionado, ou seja, se cabe no tabueiro 
# e se nao tem nenhum barco na posicao desejada

