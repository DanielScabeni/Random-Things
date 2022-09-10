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

#print(palavra_objetivo)

letras_encontradas = ["_" for letras in palavra_objetivo]

enforcado = False
acerto = False
erros = 0

print(letras_encontradas)

while(not enforcado and not acerto):
    chute = input("Qual letra você acha que tem na palavra: ")
    chute = chute.strip().upper()

    if(chute in palavra_objetivo):
        index = 0
        for letra in palavra_objetivo:
            if(chute == letra):
                letras_encontradas[index] = letra
            index += 1
        print(letras_encontradas)