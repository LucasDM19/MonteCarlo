import random
from SimulaMCAgente import MeioAmbiente, AgenteApostadorMegaSena

QTD_BOLINHAS = 60
QTD_SORTEIO = 6
VALOR_APOSTA = 4.50
PREMIO_SENA = 3000000 
PREMIO_QUINA = PREMIO_SENA/100
PREMIO_QUADRA = 5000 #PREMIO_QUINA / 50
premios = {6 : PREMIO_SENA, 5 : PREMIO_QUINA, 4 : PREMIO_QUADRA,  }
saldo = 5000.0

class SorteadorMegaSena():
   def __init__(self):
      QTD_BOLINHAS = 60
      self.bolinhas_sena = list(range(1,QTD_BOLINHAS))
   def embaralhaBolinhas(self):
      random.shuffle(self.bolinhas_sena) # Embaralha as bolinhas
   def sorteiaMegaSena(self):
      QTD_SORTEIO=6
      return bolinhas_sena[0:QTD_SORTEIO]

bolinhas_sena = list(range(1,QTD_BOLINHAS))
n_sorteio = 0 # Sorteio da semana
anterior = [] # Sorteio anterior
sair = False
#for semana in range(QTD_SEMANAS):
mundo = MeioAmbiente(tipo_agente=AgenteApostadorMegaSena, qtd_agentes=100)   # Crio mundo
benchmark = AgenteApostadorMegaSena()
benchmark.defineAtributos(nome="YPSJD0NBCI", min_aposta=31899) # Bizarro
mundo._agentes.append( benchmark )
sena = SorteadorMegaSena()
while( not sair ):
   sena.embaralhaBolinhas() 
   sorteioMegaSena = sena.sorteiaMegaSena()   # Sao 6 numeros 
   mundo.recebeAtualizacao(sorteioMegaSena)
   mundo.notificaNovoSorteio() # Somente para display
   #n_acertei = [x for x in sorteioMegaSena for y in anterior if x==y]
   #if( len(n_acertei) >=4 ):
   #if( sorted(sorteioMegaSena) == sorted(anterior) ):
      #print("Ganhou! Sorteio#", n_sorteio, ", saldo=", saldo, ", acertei=", n_acertei)
      #saldo += premios[len(n_acertei)] # Chuto valor
   #else:
      #saldo -= VALOR_APOSTA # Um bilhete
   #if( saldo <= 0 ):
   if( len(mundo._agentes) == 0 ):
      print("Todos morreram! Sorteio#", n_sorteio)
      sair = True
   n_sorteio += 1
   #anterior = sorteioMegaSena
   #if( n_sorteio % 1000 == 0 ): print("Sorteio#", n_sorteio)

