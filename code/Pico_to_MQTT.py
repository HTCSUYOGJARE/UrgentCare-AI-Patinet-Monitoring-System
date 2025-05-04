from machine import Pin, UART
import time
import network
from umqtt.simple import MQTTClient
import gc

# Initialize UART1 with GPIO4 (TX) and GPIO5 (RX)
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

#connect to wifi
wifi_ssid = "siddharth_hotspot"
wifi_password = "12345789"
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)


while not wlan.isconnected():
    print('Waiting for connection...')
    time.sleep(1)
print('Connected to WiFi')

# Connect to MQTT Broker
mqtt_host = "test.mosquitto.org"
mqtt_client_id = "pico_uart_mqtt2"
mqtt_client = MQTTClient(client_id=mqtt_client_id, server=mqtt_host)


try:
    mqtt_client.connect()
except Exception as e:
    print("MQTT connection failed:", e)
    time.sleep(2)


# List of expected activity labels (optional filtering)
#activities = ['Walking', 'Running', 'Standing', 'Sitting', 'Jumping']

# Initialize buffer
#buffer = ""

# Read data from UART
while True:
    if uart.any():
        line = uart.readline()
        if line:
            line = line.decode('utf-8').strip()
            print("Received from Nano:", line)
            try:
                mqtt_client.publish("pat/imu", line)
            except Exception as e:
                print("MQTT publish failed:", e)
    


    # Print available memory
    gc.collect()
    print("Free memory:", gc.mem_free())
    
    time.sleep(0.1)

