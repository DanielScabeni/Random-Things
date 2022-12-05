import RPi.GPIO as gpio
import os
import time as delay
from urllib.request import urlopen
import request 

gpio.setmode(gpio.BOARD)
ledvermelho, ledverde = 11, 12

gpio.setup(ledverde, gpio.OUT)
gpio.setup(ledvermelho, gpio.OUT)

gpio.output(ledverde, False)
gpio.output(ledvermelho, False)

def testa_conexao():
    try:
        urlopen('http://www.colegiomaterdei.com.br/', timeout =1)
        return True
    except:
        return False
    
if testa_conexao == True:
    while True:
        consulta = requests.get('')
        
else:
    while contador < 3:
        gpio.output(ledvermelho, True)
        delay.sleep(1)
        gpio.output(ledvermelho, False)
        delay.sleep(1)
        contador = contador + 1
        