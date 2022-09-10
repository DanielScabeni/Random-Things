import random

print("Seja bem vindo")



#print(numero_a_ser_descoberto)

#Definindo variaveis importantes do projeto
numero_a_ser_descoberto = random.randrange(1,101)
numero_de_tentativas = 0
tentativa = 1
numero_de_pontos = 1000

print("Dificuldade: ")
print("(1) Fácil | (2) Médio | (3) Hard")

dificuldade = int(input("Selecione um nível de dificuldade: "))

if(dificuldade == 1):
    numero_de_tentativas = 15
    elif(dificuldade == 2):
        numero_de_tentativas = 10
        else:
            numero_de_tentativas = 5

while(tentativa <= numero_de_tentativas):
    print(f"Aí mermao, qual o numero que tu acha que saiu? - Número da tentativa: {tentativa}")
    chute = int(input("Qual o chute (1-100): "))

    if(chute < 1 or  chute >10):
        print("Você não leu a minha mensagem. Vergonha da prroffission!")
        exit()
    acerto = chute == numero_a_ser_descoberto
    maior = chute > numero_a_ser_descoberto
    menor = chute < numero_a_ser_descoberto

    print("Mano, você chutou o número: {chute}")

    if(acerto):
        print("Parabéns, você não é burro! Você fez: {numero_de_pontos}")
        break
    else:
        if(maior):
            print("Você chutou um número maior que o sorteado")
        elif(menor):
            print("Você chutou um número menor que o sorteado")
        pontos_perdidos = 15
        #numero_de_pontos -= pontos_perdidos

        tentativa += 1;
    print("Fim de jogo! O número sorteado era: {numero_a_ser_descoberto}")