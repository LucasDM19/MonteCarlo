import random
from SimulaMCAgente import MeioAmbiente, AgenteApostadorMegaSena

class SorteadorMegaSena():
   def __init__(self):
      QTD_BOLINHAS = 60
      self.bolinhas_sena = list(range(1,QTD_BOLINHAS))
   def embaralhaBolinhas(self):
      random.shuffle(self.bolinhas_sena) # Embaralha as bolinhas
   def sorteiaMegaSena(self):
      QTD_SORTEIO=6
      return self.bolinhas_sena[0:QTD_SORTEIO]

n_sorteio = 0 # Sorteio da semana
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
