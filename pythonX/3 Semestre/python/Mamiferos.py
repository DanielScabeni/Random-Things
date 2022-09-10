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

        if (self.caracteristica == "caminhar"):
            self.numero_de_patas = 4
            return self.numero_de_patas

    def reproduz_som(self, som):
        subprocess.Popen([
            "say", som
        ])



cavalo = Mamiferos("Cavalo", "Equino", "Caminhar")
cachorro = Mamiferos("Cachorro", "doguinho", "caminhar")
morcego = Mamiferos("Batman", "bat", "voa")

#print(cavalo.descobre_numero_de_patas())
#print(cachorro.descobre_numero_de_patas())
#print(morcego.descobre_numero_de_patas())

#cavalo.reproduz_som("uuuuuuuuuuuhhhhhhhlllll")
cachorro.reproduz_som("auauauauauauauauauauauauau")
#morcego.reproduz_som("tititititititititti")