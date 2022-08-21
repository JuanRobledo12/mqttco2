# mqttco2

mqtt demo for co2 monitoring:

The simulation is made with 4 clients, three of them written in Python and the other one written in the Arduino IDE. The Python programs called sensors are MQTT publishers that simulates what a sensor module would do. The program called monitor is an MQTT subscriber that get the data published by the sensors in a specific MQTT topic. Finally, the Arduino program is both a subscriber and a publisher.
