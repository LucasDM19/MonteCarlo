import random
import string

QTD_NOMES = 10
TAMANHO_FRAG_PALAVRA=4
N=QTD_NOMES*TAMANHO_FRAG_PALAVRA

#Separando de 5 em 5 (em grupos)
tec = ''.join(random.choices(string.ascii_lowercase, k=N))
lista_grupos = [ tec[k*TAMANHO_FRAG_PALAVRA:(k+1)*TAMANHO_FRAG_PALAVRA] for k in range(int(len(tec)/TAMANHO_FRAG_PALAVRA)) ] 
print(tec)
print (lista_grupos)

#Adicionar e remover vogais e consoantes - para agradar
for palavra in lista_grupos:
   #print("Antigo=", palavra)
   nome_rpg = palavra[0]
   for idx_letra in range(len(palavra)-1) :
      #print("Atual:", palavra[idx_letra+1] , ", anterior=", palavra[idx_letra] )
      
      if palavra[idx_letra] not in 'aeiou' and palavra[idx_letra+1] not in 'aeiou' :
         #print("Coloco vogal entre consoantes")
         nome_rpg += random.choices('aeiou', k=1)[0] + palavra[idx_letra+1]
      if palavra[idx_letra] in 'aeiou' and palavra[idx_letra+1] in 'aeiou' :
         nome_rpg += random.choices('bcdefghjklmnpqrstvwxyz', k=1)[0] + palavra[idx_letra+1]
         #print("Coloco consoantes entre vogais")
      #else:
      #   print("Padrão")
      #   nome_rpg += palavra[idx_letra]
   if( len(nome_rpg) == 1 ): nome_rpg=palavra
   print("Nome RPG=", nome_rpg)
      