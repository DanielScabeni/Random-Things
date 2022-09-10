import subprocess

class Mamiferos:
    def __init__(self, nome, especie, caracteristica):
        self.nome = nome
        self.especie = especie
        self.caracteristica = caracteristica
        self.numero_de_patas = 0

    def descobre_numero_de_patas(self):
        if (self.caracteristica == "voa"):
            self.numero_de_patas = 2
            return self.numero_de_patas
        
        if (self.caracteristica == "nada"):
            self.numero_de_patas = 0
            return self.numero_de_patas
        
        if (self.caracteristica == "caminha"):
            self.numero_de_patas = 4
            return self.numero_de_patas
    def reproduz_som(self, som):
        subprocess.Popen([
            "say", som
        ])

cavalo = Mamiferos("Cavalo", "Equino", "caminhar")
cachorro = Mamiferos("Cavalo", "catioro", "caminhar")
morcego = Mamiferos("batman", "bat", "voa")

#print(cavalo.descobre_numero_de_patas())
#print(cachorro.descobre_numero_de_patas())
#print(morcego.descobre_numero_de_patas())

cavalo.reproduz_som("crzrcrzcrzcrzcrzcrzcrzcrzczcr brgrbrgrbrgrbrgrbrgrbrgrbrgrbrgrbrgrbrgrbrgrbrgrbrgrbrgr")
cachorro.repruduz_som("auauauauauauau")
morcego.reproduz_som("tititititiit")
