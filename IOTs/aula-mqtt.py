import paho.mqtt.client as mqtt
import time as delay

client = mqtt.Client('Aluno-Daniels')
client.connect('10.10.10.80', 1883, 60)
while true:
  try:
      client.publish('aula/3011/mqtt', 'codex')
      
      delay.sleep(20)
  except Exception as e:
      client.loop_stop()
      client.disconnect()
      print(e)
