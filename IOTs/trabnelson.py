import RPi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import Adafruit_DHT as dht
import os
import requests

gpio.setmode(gpio.BOARD) #seta o modo de portas da placa 
gpio.setwarnings(False) #???

ledvermelho = 11 #definição das portas
ledverde = 12 #os 2 leds e o botao
botao = 18
pin_dht = 4 #sensor temp e umid
pin_t = 15 #PINO DIGITAL UTILIZADO PELO HC-SR04 TRIG(ENVIA)
pin_e = 16 #PINO DIGITAL UTILIZADO PELO HC-SR04 ECHO(RECEBE)
i = 0 #contagem do led usado em falha de conexao
ct = 0 #contagem do led usado 
espaco_v = 20 #?????
ctb = 0 #contagem de clicks no botao
valor_invalido = '' #string para concatenar variaveis com valores invalidos

field_ocup = '&field1=' #seta os cards usados para armazenar dados no thingspeak
field_disp = '&field2='
field_umid = '&field3='
field_temp = '&field4='

api = 'https://api.thingspeak.com/update?api_key=' #
key = 'Y8HVNLUHOIOKH836' #a chave da API do thingspeak

dht_sensor = dht.DHT11 #???

gpio.setup(ledvermelho, gpio.OUT) #seta os leds como saida
gpio.setup(ledverde, gpio.OUT)
gpio.setup(botao, gpio.IN) #botao logicamente entrada 
gpio.setup(pin_t, gpio.OUT) #(Trig) emissao sonora do sensor HC-SR04
gpio.setup(pin_e, gpio.IN) #(Echo) recebe o retorno do som emitido no sensor

gpio.output(ledvermelho, False) #desliga os leds
gpio.output(ledverde, False)

def distancia(): #função q emite e recebe o som depois calcula a distancia usando com base no tempo de resposta
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

def testa_conexao(): #base para o programa rodar
    try:
        urlopen('http://www.colegiomaterdei.com.br/', timeout=1)
        return True
    except:
        return False
"""
def valida_leitura():

    if umid < 1 and umid > 100:
        valor_invalido = valor_invalido + 'Umidade ('+str(umid)+'), '
    if temp < -50 and temp > 80:
        valor_invalido = valor_invalido + 'Temperatura ('+str(temp)+'), '
    if espaco_disponivel < -1 and espaco_disponivel > 101:
        valor_invalido = valor_invalido + 'Espaço Disponivel ('+str(espaco_disponivel)+'), '
    if espaco_ocupado > -1 and espaco_ocupado < 101:
        valor_invalido = valor_invalido + 'Espaço Ocupado ('+str(espaco_ocupado)+'), '
    
    return valor_invalido
"""
if testa_conexao() == True: #praticamente o "MAIN"
    while True:
        if gpio.input(18) == True:
            ctb = ctb + 1
            gpio.output(ledvermelho, True)
            delay(2)
            gpio.output(ledvermelho, False)
        if ctb == 1:
            #leitura dados do colega
            umid_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW')
            temp_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW')
            espaco_disponivel_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/3/last?key=0D3EPD1O39791WXW')
            espaco_ocupado_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/4/last?key=0D3EPD1O39791WXW')

            print('--- Leitura Finalizada ---')
            
            u = umid_clg
            if u < 1 and u > 100:
                valor_invalido = valor_invalido + 'Umidade ('+str(u)+'), '
            t = temp_clg
            if t < -50 and t > 80:
                valor_invalido = valor_invalido + 'Temperatura ('+str(t)+'), '
            d = espaco_disponivel_clg
            if d < -1 and d > 101:
                valor_invalido = valor_invalido + 'Espaço Disponivel ('+str(d)+'), '
            o = espaco_ocupado_clg
            if o > -1 and o < 101:
                valor_invalido = valor_invalido + 'Espaço Ocupado ('+str(o)+'), '

            if valor_invalido == '':
                while ct <= 3: #piscar verde 3 vezes se nao tiver valor invalido 
                    gpio.output(ledverde, True)
                    delay.sleep(0.3)
                    gpio.output(ledverde, False)
                    delay.sleep(0.3)
                    ct = ct + 1
            else:
                print('As seguientes variaveis receberam VALORES INVALIDOS----------')
                print(valor_invalido)
                while ct <= 3: #piscar verde 3 vezes se nao tiver valor invalido 
                    gpio.output(ledverde, True)
                    delay.sleep(0.3)
                    gpio.output(ledverde, False)
                    delay.sleep(0.3)
                    ct = ct + 1

        if ctb == 2:
            print('---------------------')
    
            if espaco_ocupado > 70:
                print('!!!OCUPAÇÃO DA LIXEIRA MAIOR QUE 70%')
                gpio.output(ledvermelho, True)
            else:
                gpio.output(ledverde, True)
        
            print('Umidade: '+umid_clg)
            print('Temperatura: '+temp_clg)
            print('Espaço Disponiveis: '+espaco_disponivel_clg)
            print('Espaço Ocupado: '+espaco_ocupado_clg)

        if ctb == 3:
            gpio.output(ledvermelho, False)
            gpio.output(ledverde, False)

            print('---------------------')
            #leitura dados do colega
            umid_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW')
            temp_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW')
            #leitura dados do meu thingspeak
            umid = requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW')
            temp = requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW')

            print('---Temperatura Meus Sensores')
            print('Umidade: '+umid)
            print('Temperatura: '+temp)
            print('---Temperatura Sensores Colega')
            print('Umidade: '+umid_clg)
            print('Temperatura: '+temp_clg)
            print('---Diferença do Meu para o do Colega')
            print('Umidade: '+(umid-umid_clg))
            print('Temperatura: '+(temp-temp_clg))

        if ctb == 4:
            #leitura dados do meu thingspeak
            espaco_disponivel = requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW')
            espaco_ocupado = requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW')
            #leitura dados do colega
            espaco_disponivel_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW')
            espaco_ocupado_clg = requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW')
            #leitura dados do colega externo
            espaco_disponivel_clge = requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW')
            espaco_ocupado_clge = requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW')
            
            print('---------------------')
            print('Taxa de Ocupação das Lixeiras')
            print('Minha: '+espaco_ocupado)
            print('Colega: '+espaco_ocupado_clg)
            print('Outro: '+espaco_ocupado_clge)
            if espaco_disponivel > espaco_disponivel_clg and espaco_disponivel > espaco_disponivel_clge:
                gpio.output(ledverde, True)
            elif espaco_disponivel_clg > espaco_disponivel and espaco_disponivel_clg > espaco_disponivel_clge:
                ct=0
                while ct <= 5:
                    gpio.output(ledverde, True)
                    delay.sleep(1)
                    gpio.output(ledverde, False)
                    delay.sleep(1)
                    ct = ct + 1
            else:
                gpio.output(ledvermelho, True)
        
        if ctb == 5:
            gpio.output(ledverde, True)
            gpio.output(ledvermelho, True)
            delay.sleep(0.1)
            gpio.output(ledverde, False)
            gpio.output(ledverde, False)
            ct = 0
            ctb = 0  
            umid = 0
            umid_clg = 0
            temp = 0
            temp_clg = 0
            espaco_disponivel = 0
            espaco_disponivel_clg = 0 
            espaco_disponivel_clge = 0
            espaco_ocupado = 0
            espaco_ocupado_clg = 0
            espaco_ocupado_clge = 0
    
else:
    while i <= 3: #piscar vermelho 3 vezes se não tiver conexao
        gpio.output(ledvermelho, True)
        delay.sleep(0.1)
        gpio.output(ledvermelho, False)
        delay.sleep(0.1)
        gpio.output(ledvermelho, True)
        delay.sleep(1)
        gpio.output(ledvermelho, False)
        delay.sleep(1)
        i = i + 1    