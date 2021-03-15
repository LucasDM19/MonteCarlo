"""
3% ao dia - juros simples
5% sobre o capital investido
20% sobre o lucro na hora do saque
quantos dias ou qual o lucro ideal para fazer o reinvestimento
"""
from random import randrange

capital = 1000.0 # Inicio
juros_simples = 0.03
taxa_saque = 0.2 #sobre o lucro na hora do saque
taxa_invest = 0.05 #sobre o capital investido
n_popu = 500 # Quantos terao ao mesmo tempo
dias_max = 500 # Maximo dias
n_sim = 1000
estrategias = [{'idade' : 0, 'max_dias' : randrange(1,dias_max), 'saldo' : capital, 'capital' : capital} for q_r in range(n_popu) ]
for n in range(1, n_sim):
   for e in estrategias:
      if(n % e['max_dias'] == 0): # Hora de sacar
         e['saldo'] -= (e['saldo'] - e['capital']) * taxa_saque # Retira taxa de saque
         e['saldo'] -= e['saldo'] * taxa_invest # Taxa para investimento
         e['capital'] = e['saldo'] # Comeca tudo novamente
      else:
         e['saldo'] += e['capital']*(juros_simples)
      e['idade'] += 1
print([est for est in estrategias if est['saldo'] == max([ee['saldo'] for ee in estrategias])])