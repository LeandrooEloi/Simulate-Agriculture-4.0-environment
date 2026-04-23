import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
TOPICO = "ufrn/atividade/fazenda/temperatura"

client = mqtt.Client()
client.connect(BROKER, 1883)

print("Sensor de temperatura iniciado...")

while True:
    temp = random.randint(20, 35)
    client.publish(TOPICO, temp)
    print("Temperatura:", temp)
    time.sleep(2)