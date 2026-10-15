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
    frota[nome_navio]= [define_posicoes(linha,coluna,orientacao,tamanho)]
    return frota

