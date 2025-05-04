import paho.mqtt.client as mqtt
import winsound

# Define MQTT parameters
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "openmv/test"
MQTT_TOPIC2 = "pat/imu"

# Callback function when connection is established
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)
    client.subscribe(MQTT_TOPIC2)  # Subscribe to the second topic

# Callback function when a message is received
def on_message(client, userdata, msg):
    topic = msg.topic
    incoming_data = msg.payload.decode('utf-8')

    if topic == MQTT_TOPIC:
        score = float(incoming_data.split(":")[1].strip())
        if score < 0.70:
            print("No Presence Detected")
            
            winsound.Beep(1000, 300)
        else:
            print("Presence")
    
    elif topic == MQTT_TOPIC2:
        print(f"IMU Data Received: {incoming_data}")
        # Add more parsing logic here if needed
        if incoming_data.lower() != "i":
                print("Waving → Beep!")
                winsound.Beep(1300, 300)
        

# Create MQTT Client and connect
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)

# Blocking loop to the broker
client.loop_forever()
