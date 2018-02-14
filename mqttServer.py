import paho.mqtt.client as mqtt
import text, json

# global variables to keep track of meaningful results
flat = 0
top = 0
miss = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    text.ready()
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("pikachu/cw")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    json_data = json.loads(msg.payload)

    # index 's' contains achieved swing type for table tennis analysis
    if "s" in json_data:
        if json_data["s"] == 1: # 1 -> flat swing
            global flat
            flat += 1
            print ('Calculating...')
            text.flat_swing()
            print (str(flat) + ' consecutive flat swings')
        elif json_data["s"] == 2: # 2 -> top spin
            global top
            top += 1
            print ('Calculating...')
            text.top_spin()
            print (str(top) + ' consecutive top spins')
        text.ready()
    elif "XY" in json_data: # XY -> no swing detected
        global miss
        miss += 1
        print ('Calculating...')
        print ('No swing detected. Current misses: ' + str(miss))
        if json_data["YZ"] < 50:
            print ('Tips: Swing right to left more')
        else:
            print ('Tips: Make sure you keep your hand flat when you swing.')

        text.ready()
    # index 'c' contains measured angle in x-y plane for compass display
    elif "c" in json_data:
        text.compass(json_data["c"])


text.pikachu()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.87", 1883, 30)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
