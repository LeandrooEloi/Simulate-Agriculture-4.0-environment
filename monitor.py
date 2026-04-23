import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPICO = "ufrn/atividade/fazenda/#"

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883)
client.subscribe(TOPICO)

print("Monitorando dados...")

client.loop_forever()