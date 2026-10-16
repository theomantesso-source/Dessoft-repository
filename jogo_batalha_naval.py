import Funcoes.py 

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 

quant_inicial = 0
tam_inicial = 5
for navio,tamanho in frota:
    i = 0
    quant_inicial+=1
    tamanho-=1
    while quant_inicial>i:
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tam_inicial}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if navio!= "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal: "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        i+=1
    