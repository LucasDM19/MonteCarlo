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

def simulaMundoApostadores():
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

def estatisticasMegaSena():
   qtd_sorteios = 50063860
   n_sorteio = 1 # Sorteio da semana
   qtd_senas = 0
   qtd_quinas = 0
   qtd_quadras = 0
   sena = SorteadorMegaSena()
   for s in range(n_sorteio, qtd_sorteios):
      print("Vamos #", s, ", de ", qtd_sorteios, ", 4as=", qtd_quadras, "(", round(100.0*qtd_quadras/s,4) ,"), 5as=", qtd_quinas, "(", round(100.0*qtd_quinas/s,4) ,"), 6as=", qtd_senas, "(", round(100.0*qtd_senas/s,6) ,")"  )
      sena.embaralhaBolinhas()
      sorteioMegaSena = sena.sorteiaMegaSena()
      #sorteioMegaSena = [random.randint(1, 60) for n in range(6)] # Vamos testar
      palpite = [random.randint(1, 60) for n in range(6)] #Seis nomeros aleatorios
      sena.embaralhaBolinhas()
      palpite = sena.sorteiaMegaSena() # Vamos testar
      n_acertei = [x for x in sorteioMegaSena for y in palpite if x==y]
      if( len(n_acertei) == 4 ): qtd_quadras += 1
      if( len(n_acertei) == 5 ): qtd_quinas += 1
      if( len(n_acertei) == 6 ): qtd_senas += 1
   print("Total de sorteios:", qtd_sorteios, ", 4as=", qtd_quadras, "(", 100.0*qtd_quadras/qtd_sorteios ,"), 5as=", qtd_quinas, "(", 100.0*qtd_quinas/qtd_sorteios ,"), 6as=", qtd_senas, "(", 100.0*qtd_senas/qtd_sorteios ,")"  )

if( __name__ == '__main__' ):
   #simulaMundoApostadores()
   estatisticasMegaSena()
   