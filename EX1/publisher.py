import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "test/topic"

client = mqtt.Client()
client.connect(broker)

client.publish(topic, "Hello MQTT")

client.disconnect()