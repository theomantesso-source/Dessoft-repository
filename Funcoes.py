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
