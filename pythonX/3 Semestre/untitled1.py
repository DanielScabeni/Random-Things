# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PzShbq0lgwezQnTVgmIeQ8mdWiHHuDqL
"""

import random
print("Bem vindo a forca")
 
arquivo = open("palavras.txt")

palavras = []

for linha in arquivo:
   palavras.append(linha.strip())
arquivo.close()

#print(palavras)

numero = random.randrange(0, len(palavras))

palavra_objetivo = palavras[numero].upper()

print(palavra_objetivo)

letras_encontradas = ["_" for letra in palavra_objetivo]

enforcado = False
acerto = False
erros = 0

print(letras_encontradas)

while (not enforcado and not acerto):
    chute = input("Qual letra voce acha que tem na palavra: ")
    chute = chute.strip().upper()

    if(chute in palavra_objetivo):
      index = 0
      for letra in palavra_objetivo:
        if (chute == letra):
          letras_encontradas[index] = letras_encontradas
          index += 1
    else:
      erros += 1
    
    enforcado = erros == 6
    acerto = "_" in letras_encontradas

    print(letras_encontradas)

if(acerto):
  print("Parabéns meu gajo, você venceu!!")
else:
    print("Errrrouuuuuu")

print("Fim de jogo")

from google.colab import drive
drive.mount('/content/drive')

