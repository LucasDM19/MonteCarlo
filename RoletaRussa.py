import random
import matplotlib
import matplotlib.pyplot as plt

def roletaRussaSimples(qtd_tambores=6):
   resultado = random.randint(1,qtd_tambores) # De 1 a 6, incluindo ambos
   
   if resultado == 1:
      print( resultado,"Bang! You're dead!!" )
      return False
   #elif 100 > resultado >= 50:
   else:
      print( resultado, "Click! I AM ALIVE!! ")
      return True

def brincaDeRoleta(qtd_tiros=10):
   saldo = 0 # A pessoa comeca sem grana
   saldos = []
   vivo = True
   for pessoa in range(qtd_tiros):
      print("Darei o tiro de #", pessoa, ". Bora brincar")
      if( roletaRussaSimples(qtd_tambores=500) and vivo ):
         saldo+=10000
         saldos.append( saldo )
         print("Ganhei, Uhul!")
      else:
         saldos.append( -1000 )
         vivo = False # Pessoa morreu
         print("Oh, i am DEAD!")
   return saldos
      
def fazMonteCarlo(funcao, epocas=10, grafico=plt ):
   wX = range(epocas)
   for lace in range(epocas) :
      vY = funcao(epocas) # Retorna uma simulacao completa (ciclo)
      plt.plot(wX,vY)
   return plt
   
plt = fazMonteCarlo(funcao=brincaDeRoleta, epocas=100, grafico=plt)   

plt.ylabel('Saldos')
plt.xlabel('Ciclos')
plt.show()