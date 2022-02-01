import paho.mqtt.client as mqtt
import time
from random import random

#globals
global client

#functions
def quit_program():
    client.loop_stop()
    exit()

#callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Succesful connection! rc = ", str(rc))
    else:
        print("Unable to connect, rc = ", str(rc))
        quit_program()
def on_message(client, userdata, message):
    topic_msg = str(message.payload.decode('utf-8'))
    if topic_msg == 'disconnect_sensor1':
        quit_program()
def on_disconnect(client, userdata, rc):
    print("disconnecting reason: " , str(rc))
def on_subscribe(client, userdata, mid, granted_qos):
    print('Mid value from callback: ', mid)
    print('Granted QoS from callback:', granted_qos)

#client/broker info
client_id = 'sensor_1'
broker_ad = '192.168.6.61' #CHANGE IT IF USING OTHER BROKER
topic_id = 'co2/library'
client = mqtt.Client(client_id)

#callbacks delcaration
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
#broker connection
print("Attempting to connect to ",broker_ad, "as ",client_id)
try:
    client.connect(broker_ad, port=1883, keepalive=60)
    client.loop_start()
    time.sleep(3)
except:
    print("Connection failed, check host status or port")
    quit_program()

#subscribe
try:
    sub_tuple = client.subscribe(topic_id, qos=0)
    print('Retreived tuple (mid, QoS) from subscribe method: ', sub_tuple)
    time.sleep(3)
except:
    time.sleep(3)
    print('Unable to subscribe to topic: ', topic_id)
    print('Retreived tuple from subscribe method: ', sub_tuple)
    quit_program()


#publishing
print("Starting publishing loop at topic: ", topic_id)
print("-----------------------")

while True:
    co2_value = random() * 100
    form_co2_value = "{:.2f}".format(co2_value)
    client.publish(topic_id, payload='CO2: ' + str(form_co2_value))
    time.sleep(5)
