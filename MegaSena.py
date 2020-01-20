import random
from SimulaMCAgente import MeioAmbiente, AgenteApostadorMegaSena

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
   if( len(mundo._agentes) == 0 ):
      print("Todos morreram! Sorteio#", n_sorteio)
      sair = True
   n_sorteio += 1
