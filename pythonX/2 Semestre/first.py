import random;

print("Seja bem vindo")

numero_a_ser_descoberto = random.randrange(1,101)

#Definindo variveis importantes do projeto

numero_de_tentativas = 0
tentativa = 1
numero_de_pontos = 1000

print("Dificuldade: ")
print("(1) Fácil | (2) Médio | (3) Dificil | (4) Insano | (5) Impossivel")

dificuldade = int(input("Selecione um nivel de dificuldade: "))

if(dificuldade == 1):
    numero_de_tentativas = 25
elif(dificuldade == 2):
    numero_de_tentativas = 12
elif(dificuldade == 3):
    numero_de_tentativas = 7
elif(dificuldade == 3):
    numero_de_tentativas = 3
else:
    print("Tu ta fudido meu parcero")
    numero_de_tentativas = 1

while(tentativa <= numero_de_tentativas):
    print(f"Qual numero tu acha q saiu? - Nùmero da tentativa: {tentativa}")
    chute = int(input("Qual o chute (1-100): "))

    if(chute < 1 or chute > 100):
        print("DE 1 À 100 ANTA CEGA!!!!")
        exit()
    acerto = chute == numero_a_ser_descoberto
    maior = chute > numero_a_ser_descoberto
    menor = chute < numero_a_ser_descoberto

    print("Voce chutou o numero : {chute}")

    if(acerto):
        print("Parabens! voce nao eh burro! {numero_de_pontos}")
        break
    else:
        if(maior):
            print("voce chutou um numero maior q o sorteado")
        elif(menor):
            print("voce chutou um numero manor q o sorteado")
        pontos_perdidos = 15
        numero_de_pontos -= pontos_perdidos
    tentativa += 1
print(f"Fim de jogo! o numero sorteado era {numero_a_ser_descoberto}")

