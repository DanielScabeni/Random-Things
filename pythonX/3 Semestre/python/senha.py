senha = input("Digite a senha que você deseja usar (Precisa ter ao menos 1 número e 1 caractere especial): ")
senha = senha.strip()
##confere = randrange(0, len(9)
##if(senha in confere):
  ##print("ok, tem número")
validSenha = input("Agora, digite a sua senha para validarmos: ")
validSenha = validSenha.strip()

if(validSenha == senha):
    print("Senha válida, parabéns!")
else:
    print("Senha inválida!")
    exit()

##arquivo = open("numero.txt")
##caracter = []

##for validacao in arquivo:
##    caracter.append(validacao.strip())
##arquivo.close()

##print(validacao)

##validSenha = input("Agora, digite a sua senha para validarmos: ")
##validSenha = validSenha.strip()

##if(validSenha == senha):
  ##  print("Senha válida, parabéns!")
##else:
  ##  print("Senha inválida!")
    ##exit()
