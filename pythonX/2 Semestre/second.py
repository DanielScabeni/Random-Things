import random

print("Bem vindo a FORCA")

arquivo = open("palavras.txt")

palavras = []

for linha in arquivo:
    palavras.append(linha.strip())
arquivo.close()

#print(palavras)

numero = random.randrange(0, len(palavras))

palavra_objetivo = palavras[numero].upper()

letras_encontradas = ["_" for letra in palavra_objetivo] #Chega da um NOJO

enforcado = False
acerto = False
erros = 0

print(letras_encontradas)

while (not enforcado and not acerto):
    chute = input("Qual letra voce acha q tem na palavara: ")
    chute = chute.strip().upper()

    if(chute in palavra_objetivo):
        index = 0
        for letra in palavra_objetivo:
            if(chute == letra):
                letras_encontradas[index] = letra
            index += 1
    else:
        erros += 1
    
    enforcado = erros == 6
    acerto = "_" in palavra_objetivo

    print(letras_encontradas)

if(acerto):
    print("Parabens vc GANHOU")
else:
    print("Parabens vc PERDEU")