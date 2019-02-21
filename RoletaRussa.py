import random

def RoletaRussaSimples(qtd_tambores=6):
   resultado = random.randint(1,qtd_tambores) # De 1 a 6, incluindo ambos
   
   if resultado == 1:
      print( resultado,"Bang! You're dead!!" )
      return False
   #elif 100 > resultado >= 50:
   else:
      print( resultado, "Click! I AM ALIVE!! ")
      return True
      
for lace in range(10) :
   resultado = RoletaRussaSimples()
   #print(resultado)