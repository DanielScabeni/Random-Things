# -*- coding: utf-8 -*-
"""novo_notebook_2_amanda_revisado_de_novo_pelo_doug.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HYry0pnoeFOtXCMtoObVZeRbNDNSbR2V
"""

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

    
cavalo = Mamifero("Cavalo", "Cleyton", "Caminhar")
cachorro = Mamifero("Dog", "catioro", "caminha")
morcego = Mamiferos("Batman", "bat", "voa")

#print(cavalo.descobre_numero_de_patas())
#print(cachorro.descobre_numero_de_patas())
#print(morcego.descobre_numero_de_patas())

cavalo.reproduz_som("uhhhhhhhhhilllllllll")
cachorro.reproduz_som("auauauauauauua")
morcego.reproduz_som("itiitiitiititiiti")