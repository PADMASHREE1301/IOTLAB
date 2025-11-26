import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "test/topic"

def on_message(client, userdata, msg):
    print("Received MSG")

client = mqtt.Client()
client.connect(broker)

client.subscribe(topic)
client.on_message = on_message

client.loop_forever()