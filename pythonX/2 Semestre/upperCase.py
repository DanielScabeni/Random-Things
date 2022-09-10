#frase = (input("Informe uma frase 2: "))
#frase = frase.strip().upper()
#print(frase)

class Uppercase:
    def __init__(self, frase):
        self.frase = frase

    def uppercase(self):
        self.frase = self.frase.strip().upper()
        return self.frase

frase1 = Uppercase((input("Informe uma frase: ")))
print(frase1.uppercase())