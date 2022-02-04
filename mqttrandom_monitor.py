#CO2 monitor simulation, subscribes to several topics for CO2 data.
#Created by Juan Antonio Robledo Lara https://github.com/TonyRob127/mqttco2
#Last mod: Feb 4th 2022

import paho.mqtt.client as mqtt
import time

#globals
global client

#functions
def quit_program():
    client.loop_stop()
    exit()

#callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successful connection with rc: ", str(rc))
        print("--------------------------")
        
    else:
        print("Unable to connect with rc: ", str(rc))
        quit_program()

def on_message(client, userdata, message):
    topic_msg = str(message.payload.decode('utf-8'))
    print("message received: ", topic_msg)
    print("message topic: ", message.topic)
    print("--------------------------")
    if topic_msg == 'disconnect_monitor':
        quit_program()
def on_disconnect(client, userdata, rc):
    print('Disconnecting reason ' + str(rc))
def on_subscribe(client, userdata, mid, granted_qos):
    print('Mid value from callback: ', mid)
    print('Granted QoS from callback:', granted_qos)
    print('--------------------------')

#client info and declaration
client_id = "monitor_demo"
host_ad = '192.168.6.61' #CHANGE IT IF USING OTHER BROKER
client = mqtt.Client(client_id)
topic_id_lst = [('co2/library', 0), ('co2/classroom1b', 0), ('co2/laboratory', 0)]

#callback delcaration
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe

#Connect to broker
print("Connecting to broker ", host_ad, "as:", client_id)
try:
    client.connect(host_ad, port=1883, keepalive=60)
    time.sleep(3)
except:
    print("Connection failed, check host status or port")
    quit_program()


#Subscribing
try:
    sub_tuple = client.subscribe(topic_id_lst, qos=0)
    print('Retreived tuple (mid, QoS) from subscribe method: ', sub_tuple)
    time.sleep(3)
    print("Subscribing to topics: ", topic_id_lst)
except:
    time.sleep(3)
    print('Unable to subscribe to topic: ', topic_id_lst)
    print('Retreived tuple from subscribe method: ', sub_tuple)
    quit_program()

client.loop_forever()

