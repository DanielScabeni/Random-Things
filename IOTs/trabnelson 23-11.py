import RPi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import Adafruit_DHT as dht
import os
import requests

#MEU   1909880   L7MAXQ83EGPBHJUE
#Colega   1928247   G37I8C7N8N56H27S
#Outro   1928249   YK45KPNG2GOYJBTB  

gpio.setmode(gpio.BOARD) #seta o modo de portas da placa 
gpio.setwarnings(False) #???

ledvermelho = 11 #definição das portas
ledverde = 12 #os 2 leds e o botao
botao = 18 #butão
i = 0 #contagem do led usado em falha de conexao
ct = 0 #contagem do led usado 
ctb = 0 #contagem de clicks no botao
valor_invalido = '' #string para concatenar variaveis com valores invalidos
vb = False #Valida Botao, para evitar loop no if do botao

gpio.setup(ledvermelho, gpio.OUT) #seta os leds como saida
gpio.setup(ledverde, gpio.OUT)
gpio.setup(botao, gpio.IN) #botao logicamente entrada 

gpio.output(ledvermelho, False) #desliga os leds
gpio.output(ledverde, False)

def testa_conexao(): #base para o programa rodar
    try:
        urlopen('http://www.colegiomaterdei.com.br/', timeout=1)
        return True
    except:
        return False
    
def valida_leitura(o, d, u, t):#validação de valores validos para os dados lidos do colega
    valor_inv = ''
    if o < 0 and o > 100: #concatena se tiver valores invalidos
        valor_inv = valor_inv + '||Espaço Ocupado ('+str(o)+'), '
    if d < 0 and d > 100:
        valor_inv = valor_inv + '||Espaço Disponivel ('+str(d)+'), '  
    if u < 1 and u > 100:
        valor_inv = valor_inv + '||Umidade ('+str(u)+'), '
    if t < -50 and t > 80:
        valor_inv = valor_inv + '||Temperatura ('+str(t)+'), '
    return valor_inv

if testa_conexao() == True: #praticamente o "MAIN"
    print('---!-!-POWER ON-!-!---')
    
    while True:
        if gpio.input(18) == True: #leitura do botao
            ctb = ctb + 1
            vb = True
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('\n*click')
            
        if ctb == 1 and vb == True:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Acender Vermelho por 2 segundos, fazer leitura, verificar se os valores são validos\n'+
                  'se todos forem validos, piscar Verde 3x se tiver algum valor invalido, piscar o vermelho3x')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            gpio.output(ledvermelho, True)  # ao identificar click, acender ledvermelho por 2 segundos dps fazer leitura
            delay.sleep(2)
            gpio.output(ledvermelho, False)
            # leitura dados do colega--------------
            espaco_ocupado_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/1/last?key=G37I8C7N8N56H27S').text)
            espaco_disponivel_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/2/last?key=G37I8C7N8N56H27S').text)
            umid_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/3/last?key=G37I8C7N8N56H27S').text)
            temp_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/4/last?key=G37I8C7N8N56H27S').text)
           
            print('\n-!-!- Leitura Finalizada -!-!-')

            valor_invalido = valida_leitura(espaco_ocupado_clg, espaco_disponivel_clg, umid_clg, temp_clg)

            if valor_invalido == '':
                while ct < 3: #piscar verde 3 vezes se nao tiver valor invalido 
                    gpio.output(ledverde, True)
                    delay.sleep(0.3)
                    gpio.output(ledverde, False)
                    delay.sleep(0.3)
                    ct = ct + 1

                print('\nEspaço Ocupado: '+str(espaco_ocupado_clg))
                print('Espaço Disponiveis: '+str(espaco_disponivel_clg))
                print('Umidade: '+str(umid_clg))
                print('Temperatura: '+str(temp_clg))
                
            else: #mostra string concatenada dos valores invalidos recebidos
                while ct <= 3: #piscar vermelho 3 vezes se tiver valor invalido 
                    gpio.output(ledvermelho, True)
                    delay.sleep(0.3)
                    gpio.output(ledvermelho, False)
                    delay.sleep(0.3)
                    ct = ct + 1
                print('\nAs seguientes variaveis receberam VALORES INVALIDOS----------')
                print(valor_invalido)

            vb = False

        if ctb == 2 and vb == True:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Se a ocupação da lixeira for maior q 70 manter o vermelho aceso\n'+
                  'Se não, manter aceso o Verde. independente disto mostrar os valores')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
            if espaco_ocupado_clg > 70:
                print('\n!!!OCUPAÇÃO DA LIXEIRA MAIOR QUE 70%')
                gpio.output(ledvermelho, True)
            else:
                gpio.output(ledverde, True)

            print('\nEspaço Ocupado: '+str(espaco_ocupado_clg))
            print('Espaço Disponiveis: '+str(espaco_disponivel_clg))
            print('Umidade: '+str(umid_clg))
            print('Temperatura: '+str(temp_clg))
            
            vb = False
            delay.sleep(2)#delay para nao contar 2 clicks
            
        if ctb == 3 and vb == True:
            gpio.output(ledvermelho, False)
            gpio.output(ledverde, False)

            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Ler Umidade e Temperatura, comparar com o do colega, mostrar os valores e a diferença')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            #leitura dados do colega
            umid_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/3/last?key=G37I8C7N8N56H27S').text)
            temp_clg = float(requests.get('https://api.thingspeak.com/channels/1928247/fields/4/last?key=G37I8C7N8N56H27S').text)
            #leitura dados do meu thingspeak
            umid = float(requests.get('https://api.thingspeak.com/channels/1909880/fields/3/last?key=L7MAXQ83EGPBHJUE').text)
            temp = float(requests.get('https://api.thingspeak.com/channels/1909880/fields/4/last?key=L7MAXQ83EGPBHJUE').text)

            print('\n---Temperatura Meus Sensores')
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
            espaco_disponivel_clge = float(requests.get('https://api.thingspeak.com/channels/1928249/fields/2/last?key=YK45KPNG2GOYJBTB').text)
            espaco_ocupado_clge = float(requests.get('https://api.thingspeak.com/channels/1928249/fields/1/last?key=YK45KPNG2GOYJBTB').text)
            
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Mostrar ocupação da lixeira, minha, do colega e de outro'+
            '\nSe a minha lixeira estiver com mais espaço disponivel acender verde'+
            '\nSe a do colega estiver com mais espaço disponivel piscar 5x Verde (interv 1s)'+
            '\nSe a do outro colega estiver com mais espaço disponivel acender Vermelho')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

            print('\nTaxa de Ocupação das Lixeiras')
            print('Minha: '+str(espaco_ocupado))
            print('Colega: '+str(espaco_ocupado_clg))
            print('Outro: '+str(espaco_ocupado_clge))
            if espaco_disponivel > espaco_disponivel_clg and espaco_disponivel > espaco_disponivel_clge:
                gpio.output(ledverde, True)
            elif espaco_disponivel_clg > espaco_disponivel and espaco_disponivel_clg > espaco_disponivel_clge:
                ct = 0
                while ct < 5:
                    print('socoroooo')
                    gpio.output(ledverde, True)
                    delay.sleep(1)
                    gpio.output(ledverde, False)
                    delay.sleep(1)
                    ct = ct + 1
            else:
                gpio.output(ledvermelho, True)
        
            vb = False
            
        if ctb == 5 and vb == True:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('=-=-=-=-=-=-=-=-=FINALIZADO-=-=-=-=-=-=-=-=-=-=\n')
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
            delay.sleep(10)
     
else:
    print('----------A FATAL ERROR HAS OCCURRED---------')
    print('-----Connection Lost-----Connection Lost-----')
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