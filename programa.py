from Funcoes import posicao_valida 
from Funcoes import define_posicoes
from Funcoes import preenche_frota



frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 

quant_inicial = 0
tamanho = 5
dicio_navio = {}
for navio in frota.keys():
    i = 0
    quant_inicial+=1
    tamanho-=1
    while quant_inicial>i:
        orientacao = 0 
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if navio!= "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal: "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        if posicao_valida(frota,linha,coluna,orientacao,tamanho) == False:
            print("Esta posição não está válida!")
        else: 
            define_posicoes(linha,coluna,orientacao,tamanho)
            preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
            i+=1

print(frota)

#Até aqui feito o programa para perguntar as frotas(Linha, Coluna e Direcao), verificar se pode ser colocada no
# local pedido e colocalas, fazendo isso para todas as frotas 
