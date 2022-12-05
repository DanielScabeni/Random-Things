import RPi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import Adafruit_DHT as dht
import os
import requests

#MEU   1909880   L7MAXQ83EGPBHJUE
#Colega   1928247   G37I8C7N8N56H27S
#Outro   ''

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
vb = False #para sair do loop do if do botao

field_ocup = '&field1=' #seta os cards usados para armazenar dados no thingspeak
field_disp = '&field2='
field_umid = '&field3='
field_temp = '&field4='

dht_sensor = dht.DHT11 #seta o tipo de sensor, dh11

gpio.setup(ledvermelho, gpio.OUT) #seta os leds como saida
gpio.setup(ledverde, gpio.OUT)
gpio.setup(botao, gpio.IN) #botao logicamente entrada 
gpio.setup(pin_t, gpio.OUT) #(Trig) emissao sonora do sensor HC-SR04
gpio.setup(pin_e, gpio.IN) #(Echo) recebe o retorno do som emitido no sensor

gpio.output(ledvermelho, False) #desliga os leds
gpio.output(ledverde, False)

def testa_conexao(): #base para o programa rodar
    try:
        urlopen('http://www.colegiomaterdei.com.br/', timeout=1)
        return True
    except:
        return False
    
if testa_conexao() == True: #praticamente o "MAIN"
    while True:
        #print('esperando click')
        if gpio.input(18) == True: #leitura do botao
            ctb = ctb + 1
            vb = True
            print('*click')
            gpio.output(ledvermelho, True)
            delay.sleep(2)
            gpio.output(ledvermelho, False)
            
        if ctb == 1 and vb == True:
            #leitura dados do colega
            espaco_ocupado_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/1/last?key=G37I8C7N8N56H27S').text)
            espaco_disponivel_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/2/last?key=G37I8C7N8N56H27S').text)
            umid_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/3/last?key=G37I8C7N8N56H27S').text)
            temp_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/4/last?key=G37I8C7N8N56H27S').text)
           
            print('--- Leitura Finalizada ---')
            
            u = umid_clg #validação de valores validos para os dados
            if u < 1 and u > 100: #concatena se tiver valaores invalidos
                valor_invalido = valor_invalido + 'Umidade ('+str(u)+'), '
            t = temp_clg
            if t < -50 and t > 80:
                valor_invalido = valor_invalido + 'Temperatura ('+str(t)+'), '
            d = espaco_disponivel_clg
            if d < -1 and d > 101:
                valor_invalido = valor_invalido + 'Espaço Disponivel ('+str(d)+'), '
            o = espaco_ocupado_clg
            if o < -1 and o > 101:
                valor_invalido = valor_invalido + 'Espaço Ocupado ('+str(o)+'), '

            if valor_invalido == '':
                while ct <= 3: #piscar verde 3 vezes se nao tiver valor invalido 
                    gpio.output(ledverde, True)
                    delay.sleep(0.3)
                    gpio.output(ledverde, False)
                    delay.sleep(0.3)
                    ct = ct + 1
                    
                print('Umidade: '+str(umid_clg))
                print('Temperatura: '+str(temp_clg))
                print('Espaço Disponiveis: '+str(espaco_disponivel_clg))
                print('Espaço Ocupado: '+str(espaco_ocupado_clg))
            
            else: #mostra string concatenada dos valores invalidos recebidos
                print('As seguientes variaveis receberam VALORES INVALIDOS----------')
                print(valor_invalido) 
                while ct <= 3: #piscar vermelho 3 vezes se tiver valor invalido 
                    gpio.output(ledvermelho, True)
                    delay.sleep(0.3)
                    gpio.output(ledvermelho, False)
                    delay.sleep(0.3)
                    ct = ct + 1
            vb = False

        if ctb == 2 and vb == True:
            print('---------------------')
    
            if espaco_ocupado_clg > 70:
                print('!!!OCUPAÇÃO DA LIXEIRA MAIOR QUE 70%')
                gpio.output(ledvermelho, True)
            else:
                gpio.output(ledverde, True)
        
            print('Umidade: '+str(umid_clg))
            print('Temperatura: '+str(temp_clg))
            print('Espaço Disponiveis: '+str(espaco_disponivel_clg))
            print('Espaço Ocupado: '+str(espaco_ocupado_clg))

            vb = False
            
        if ctb == 3 and vb == True:
            gpio.output(ledvermelho, False)
            gpio.output(ledverde, False)

            print('---------------------')
            #leitura dados do colega
            umid_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/3/last?key=G37I8C7N8N56H27S').text)
            temp_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/4/last?key=G37I8C7N8N56H27S').text)
            #leitura dados do meu thingspeak
            umid = float(requests.get('https://api.thingspeak.com/channels/1909880/fields/3/last?key=L7MAXQ83EGPBHJUE').text)
            temp = float(requests.get('https://api.thingspeak.com/channels/1909880/fields/4/last?key=L7MAXQ83EGPBHJUE').text)

            print('---Temperatura Meus Sensores')
            print('Umidade: '+str(umid))
            print('Temperatura: '+str(temp))
            print('---Temperatura Sensores Colega')
            print('Umidade: '+str(umid_clg))
            print('Temperatura: '+str(temp_clg))
            print('---Diferença do Meu para o do Colega')
            print('Umidade: '+str((umid-umid_clg)))
            print('Temperatura: '+str((temp-temp_clg)))

            vb = False
            
        if ctb == 4 and vb == True:
            #leitura dados do meu thingspeak
            espaco_disponivel = float(requests.get('https://api.thingspeak.com/channels/1909880/fields/2/last?key=L7MAXQ83EGPBHJUE').text)
            espaco_ocupado = float(requests.get('https://api.thingspeak.com/channels/1909880/fields/1/last?key=L7MAXQ83EGPBHJUE').text)
            #leitura dados do colega
            espaco_disponivel_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/2/last?key=G37I8C7N8N56H27S').text)
            espaco_ocupado_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/1/last?key=G37I8C7N8N56H27S').text)
            #leitura dados do colega externo
            espaco_disponivel_clge = float(requests.get('https://api.thingspeak.com/channels/1909879/fields/2/last?key=0D3EPD1O39791WXW').text)
            espaco_ocupado_clge = float(requests.get('https://api.thingspeak.com/channels/1909879/fields/1/last?key=0D3EPD1O39791WXW').text)
            
            print('---------------------')
            print('Taxa de Ocupação das Lixeiras')
            print('Minha: '+str(espaco_ocupado))
            print('Colega: '+str(espaco_ocupado_clg))
            print('Outro: '+str(espaco_ocupado_clge))
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
        
            vb = False
            
        if ctb == 5 and vb == True:
            gpio.output(ledverde, True)
            gpio.output(ledvermelho, True)
            delay.sleep(0.1) #leds para indicar q deu certo
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
            vb = False
     
else:
    print('---------------------------------------------')
    print('---------------Connection Lost---------------')
    while i <= 3: #piscar vermelho 3 vezes se não tiver conexao
        gpio.output(ledvermelho, True)
        delay.sleep(0.5)
        gpio.output(ledvermelho, False)
        delay.sleep(0.5)
        gpio.output(ledvermelho, True)
        delay.sleep(1)
        gpio.output(ledvermelho, False)
        delay.sleep(1)
        i = i + 1    