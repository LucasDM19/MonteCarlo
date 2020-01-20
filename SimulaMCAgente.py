import random, string
import operator

class MeioAmbiente():
   def __init__(self, tipo_agente, qtd_agentes=1000):
      self._agentes = [tipo_agente() for agente in range(qtd_agentes)]
      self._afogados = []   # Quem perder todo o patrimonio
      self._geracoes = 0   # Contabiliza as eras
      self._corridas = 0   # Contabiliza as corridas
      
   def recebeAtualizacao(self, numeros):
      [agente.decide(numeros) for agente in self._agentes]
      [self._afogados.append(agente) for agente in self._agentes if agente.estouVivo() == False]   # Quem se afogou sai
      self._agentes =  [agente for agente in self._agentes if agente.estouVivo() == True]    # Sobreviventes
      #melhor_patrimonio = max([agente.patrimonio for agente in self._agentes])
      melhor_retorno = max([agente.lucro_medio for agente in self._agentes])
      #melhorAgente = "<>".join( [str(agente) for agente in self._agentes if agente.patrimonio == melhor_patrimonio] )
      melhorAgente = "<>".join( [str(agente) for agente in self._agentes if agente.lucro_medio == melhor_retorno] )
      #if( self._geracoes % 500 == 0 ): print("Geracao#", self._geracoes, " Vivos:", len(self._agentes), ", afogados=", len(self._afogados), ", Champs=", melhorAgente )
      self._geracoes += 1
      
   def notificaNovoSorteio(self):
      #[agente.novaCorrida() for agente in self._agentes]
      melhor_retorno = max([agente.lucro_medio for agente in self._agentes])
      melhorAgente = "<>".join( [str(agente) for agente in self._agentes if agente.lucro_medio == melhor_retorno] )
      print("Sorteio#", self._corridas, " Vivos:", len(self._agentes), ", afogados=", len(self._afogados), ", Champs=", melhorAgente )
      self._corridas += 1
      
   def __str__ (self):
      desc = "Era "+ str(self._geracoes)
      lista_agentes = [agente for agente in self._agentes if agente.estouVivo() == True]
      while( len(lista_agentes) != 0 ):
         melhor_retorno = max([agente.lucro_medio for agente in lista_agentes])
         melhorAgente = "<>".join( [str(agente) for agente in lista_agentes if agente.lucro_medio == melhor_retorno] )
         desc += melhorAgente + "#"
         lista_agentes = [agente for agente in lista_agentes if agente.lucro_medio != melhor_retorno]
      return desc
      
class AgenteApostadorMegaSena():
   def __init__(self):
      self.iniciaMindset()
      
   def iniciaMindset(self):
      self.nome = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))   # Uma cadeia de letras e numeros de tamanho 10
      self.patrimonio = 100.0   # Mil doletas
      self.somaStack = 0.0 # Capital de giro
      self.lucro_medio = 0.0 # Retorno do investimento
      self.min_aposta = random.randrange(1000, 100000) # Quanto contabiliza antes de comecar a apostar
      self.freq_numeros = {} # Numeros quentes, mornos e frios
      self.idade = 0 # Um bebezito
      
   def estouVivo(self):
      if( self.patrimonio <= 0 ): return False
      return True
      
   def decide(self, numeros):
      VALOR_APOSTA = 4.50
      PREMIO_SENA = 3000000 
      PREMIO_QUINA = PREMIO_SENA/100
      PREMIO_QUADRA = 5000 #PREMIO_QUINA / 50
      premios = {6 : PREMIO_SENA, 5 : PREMIO_QUINA, 4 : PREMIO_QUADRA,  }
      if( self.min_aposta < self.idade ): # Jovem demais para apostar
         sorted_freq_numeros = dict( sorted(self.freq_numeros.items(), key=operator.itemgetter(1),reverse=True))
         conta_num = 0
         numeros_quentes = []
         numeros_mornos = []
         numeros_frios = []
         for s in sorted_freq_numeros:
            if( conta_num <= 20 ): numeros_quentes.append(s) # Quente
            if( conta_num > 20 and conta_num <= 40 ): numeros_mornos.append(s) # Quente
            if( conta_num > 40 ): numeros_frios.append(s) # Quente
            conta_num += 1
            #print(s, sorted_freq_numeros[s])
         #print(numeros_quentes, numeros_mornos, numeros_frios)
         meio_meio = int(len(numeros_mornos)/2)
         n_aposta1 = numeros_mornos[meio_meio-2:meio_meio+1] # Meio dos numeros (o mais morno dos mornos) - tres numeros
         n_aposta2 = numeros_quentes[:3] # Os mais quentes dos mais quentes
         n_aposta3 = numeros_frios[-3:] # Os mais frios dos mais frios
         aposta = n_aposta1 + n_aposta2 + n_aposta3
         n_acertei = [x for x in numeros for y in aposta if x==y]
         if( len(n_acertei) >=4 ):
            print("Ganhou!", self.nome, ", Sorteio#", self.idade, ", saldo=", self.patrimonio, ", acertei=", n_acertei)
            self.patrimonio += premios[len(n_acertei)] # Chuto valor
         else:
            self.patrimonio -= VALOR_APOSTA # Um bilhete
         #print("ap=", aposta, ", qtd=", n_acertei)
         #return True
      self.idade += 1 # Conta essa
      for numero in numeros: 
         if (numero not in self.freq_numeros ): self.freq_numeros[numero] = 0
         self.freq_numeros[numero] += 1
      return False
      
   def __str__ (self):
      return "Nome="+self.nome+", espero="+str(self.min_aposta)+", Grana="+str(round(self.patrimonio,2))
      
if( __name__ == '__main__' ):
   print("Rodo pela linha de comando!")
   mundo = MeioAmbiente(tipo_agente=AgenteApostadorMegaSena, qtd_agentes=5)
   [mundo.recebeAtualizacao(numeros=[1, 2, 3, 4, 5, 6]) for geracoes in range(50)]
   print(mundo)