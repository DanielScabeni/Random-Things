import RPi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import Adafruit_DHT as dht
import os
import requests

gpio.setmode(gpio.BOARD)

ledvermelho = 11
ledverde = 12
botao = 18
pin_dht = 4
pin_t = 15
pin_e = 16
i = 0
espaco_v = 20

field_ocup = '&field1='
field_dist = '&field2='
field_umid = '&field3='
field_temp = '&field4='

api = 'https://api.thingspeak.com/update?api_key='
key = 'XMK7VU35IXUP6HKT'

dht_sensor = dht.DHT11

gpio.setup(ledvermelho, gpio.OUT)
gpio.setup(ledverde, gpio.OUT)
gpio.setup(botao, gpio.IN)
gpio.setup(pin_t, gpio.OUT)
gpio.setup(pin_e, gpio.IN)

gpio.output(ledvermelho, False)
gpio.output(ledverde, False)

def distancia():
    gpio.output(pin_t, True)
    delay.sleep(0.000001)
    gpio.output(pin_t, False)
    tempo_i = delay.time()
    tempo_f = delay.time()
    
    while gpio.input(pin_e) == False:
        tempo_i = delay.time()
    while gpio.input(pin_e) == True:
        tempo_f = delay.time()
        
    tempo_d = tempo_f - tempo_i
    distancia = (tempo_d*34300)/2
    
    return distancia

def testa_conexao():
    try:
        urlopen('http://www.colegiomaterdei.com.br/', timeout=1)
        return True
    except:
        return False
    
if testa_conexao() == True:
    while True:
        umid, temp = dht.read(dht_sensor, pin_dht)
        print(umid)
        print(temp)
        print(distancia())
        espaco_d = (distancia()/espaco_v)*100
        espaco_o = 100 - espaco_d
        
        print('Espaço disponível: '+str(espaco_d))
        print('Espaço ocupado: '+str(espaco_o))
        
        dados = (api+key+field_temp+str(temp)+field_umid+str(umid)+field_dist+str(espaco_d)+field_ocup+str(espaco_o))
        print('Link API: '+dados)
        requests.post(dados)
        print('Dados enviados')        
        delay.sleep(20)        
else:
    while i <= 3:
        gpio.output(ledvermelho, True)
        delay.sleep(1)
        gpio.output(ledvermelho, False)
        delay.sleep(1)
        i = i + 1    