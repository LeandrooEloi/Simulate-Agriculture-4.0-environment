import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
TOPICO = "ufrn/atividade/fazenda/umidade"

client = mqtt.Client()
client.connect(BROKER, 1883)

print("Sensor de umidade iniciado...")

while True:
    umidade = random.randint(10, 80)
    client.publish(TOPICO, umidade)
    print("Umidade:", umidade)
    time.sleep(2)