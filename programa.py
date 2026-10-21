from funcoes import posicao_valida 
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import posiciona_frota
from funcoes import monta_tabuleiros
from funcoes import faz_jogada
from funcoes import afundados
import random

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

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

#Até aqui feito o programa para perguntar as frotas(Linha, Coluna e Direcao), verificar se pode ser colocada no
# local pedido e colocalas, fazendo isso para todas as frotas 

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))
tentativas = []
tentativas_oponente = []
continuar = True
while continuar == True:
    acesso = False
    linha = int(input("Jogador, qual linha deseja atacar?"))
    while linha<0 or linha>9:
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar?"))
    coluna = int(input("Jogador, qual coluna deseja atacar?"))
    while coluna<0 or coluna>9:
        print("Coluna inválida!")
        coluna = int(input("Jogador, qual coluna deseja atacar?"))
    tentativa_atual = [linha,coluna]
    if tentativa_atual not in tentativas : 
        tentativas.append(tentativa_atual)
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linha,coluna)
        Quant_afundados = afundados(frota_oponente,tabuleiro_oponente)
        acesso = True
    else:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue

    if Quant_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break

    tentativa_atual_oponente = [random.randint(0,9),random.randint(0,9)]
    while tentativa_atual_oponente in tentativas_oponente:
        tentativa_atual_oponente = [random.randint(0,9),random.randint(0,9)]

    tentativas_oponente.append(tentativa_atual_oponente)
    tabuleiro_jogador = faz_jogada(tabuleiro_jogador,tentativa_atual_oponente[0],tentativa_atual_oponente[1])
    print(f'Seu oponente está atacando na linha {tentativa_atual_oponente[0]} e coluna {tentativa_atual_oponente[1]}')

    Quant_afundados_oponente = afundados(frota,tabuleiro_jogador)
    if Quant_afundados_oponente == 10:
        print('Xi! O oponente derrubou toda a sua frota =(')
        break

    if acesso == True:
        print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))

