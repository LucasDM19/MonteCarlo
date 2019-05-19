# Estrategia
# EST001 - Comprar opcao de compra (PREEXE_opcao > PREULT_acao ) - as mais baratas
# EST002 - apenas a mais barata
# EST003 - Comprar opcao de venda (PREEXE_opcao < PREULT_acao) - as mais baratas
# EST004 - apenas a mais barata

from csv import reader

LOTE_PADRAO = 2   # Código de uma ação padrão
CALL=78 #Compra
PUT=82 #Venda
ACAO='VALE' #Padrao no nome

def s(a,i,f): return a[i-1:f].strip()
def f(a,i,f): return float(a[i-1:f])/100
def i(a,i,f): return int(a[i-1:f])

tabela_acoes=[]
tabela_opcoes_compra=[]
tabela_opcoes_venda=[]
for arquivo in ['COTAHIST_A2017.TXT']:
    with open('./'+arquivo,'r', encoding='ISO-8859-1') as arquivo_txt:
        for linha in reader(arquivo_txt):
            linha=linha[0] #Vetor com um único item vira uma string

            TIPREG=i(linha,1,2)
            if TIPREG==0 or TIPREG==99: continue;
            
            DATA=i(linha,3,10)
            CODBDI=i(linha,11,12)
            CODNEG=s(linha,13,24)
            TPMERC=s(linha,25,27)
            NOMRES=s(linha,28,39)
            ESPECI=s(linha,40,49).strip()
            PREABE=f(linha,57,69)
            PREMAX=f(linha,70,82)
            PREMIN=f(linha,83,95)
            PREMED=f(linha,96,108)
            PREULT=f(linha,109,121)
            TOTNEG=i(linha,148,152)
            QUATOT=i(linha,153,170)
            VOLTOT=f(linha,171,188)
            PREEXE=f(linha,189,201)
            INDOPC=i(linha,202,202)
            DATVEN=i(linha,203,210)
            FATCOT=i(linha,211,217)

            #Se for uma ação lista a data, o código de negociação e o último preço negociado
            if CODBDI==LOTE_PADRAO and ACAO in CODNEG :
                tabela_acoes+=[[DATA, CODNEG,PREULT,]]
            if CODBDI==CALL and ACAO in CODNEG :
                tabela_opcoes_compra+=[[DATA, CODNEG,PREULT,PREEXE, DATVEN]]
            if CODBDI==PUT and ACAO in CODNEG :
                tabela_opcoes_venda+=[[DATA, CODNEG,PREULT,PREEXE, DATVEN]]

#print(len(tabela_acoes))
#print(len(tabela_opcoes_compra))
#print(len(tabela_opcoes_venda))

carteira = {}
saldo = 1000

for a in tabela_acoes:
   data, c, preco_acao = a
   print("Data=", data, ", preco=", preco_acao)
   opcoes_compra_OTM = [d for d in tabela_opcoes_compra if d[0] == data and d[3] > preco_acao ]
   #print("Opcoes compra OTM=", opcoes_compra_OTM )
   
   #Atualiza a carteira
   for i in carteira:
      op_i = [d[2] for d in tabela_opcoes_compra if d[0] == data and d[1]==i ]
      #print("i=", op_i)
      if( len(op_i) == 0 ): #Opcao virou po
         #print("Virou po!")
         #del carteira[i]
         carteira[i][1] = 0  # Sem valor algum
      else: # ainda existe
         carteira[i][1] = [d[2] for d in tabela_opcoes_compra if d[0] == data and d[1]==i ][0]# Atualizo valor corrente da opcao
      #Atualizar o saldo, com base na carteira
      saldo += (carteira[i][1] - carteira[i][0])*carteira[i][2]
   
   #Novos itrens na carteira
   menor_preco = min([o_c_atm[2] for o_c_atm in opcoes_compra_OTM])
   opcoes_compra_OTM_baratas = [o_c_atm for o_c_atm in opcoes_compra_OTM if o_c_atm[2] == menor_preco]
   #print("OTM mais barata:", opcoes_compra_OTM_baratas )
   for oc in opcoes_compra_OTM_baratas:
      stake = 1 # Sempre pago uma unidade em cada opcao. Sem importar com o preco
      carteira[oc[1]] = [oc[2], oc[2], stake] # Comprei opcao XPTO -> paguei X, vale Y, comprei Z
      
   print("Saldo parcial=", saldo )

print("Carteira=", carteira)
print("Saldo=", saldo)