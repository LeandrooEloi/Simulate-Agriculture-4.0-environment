import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPICO = "ufrn/atividade/fazenda/umidade"

def on_message(client, userdata, msg):
    umidade = int(msg.payload.decode())

    print(f"Umidade recebida: {umidade}")

    if umidade < 30:
        print(">>> Irrigador LIGADO")
    else:
        print(">>> Irrigador DESLIGADO")

client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883)
client.subscribe(TOPICO)

print("Irrigador iniciado...")

client.loop_forever()