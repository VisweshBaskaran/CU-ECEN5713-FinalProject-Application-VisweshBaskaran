# Author : Visweshwaran 
# File name: Air_quality.py
# File Description: Driver code for MQ135 sensor
# Reference: Based on Raspberry Pi Adjustable hackster.io blog [https://www.hackster.io/kutluhan-aktar/raspberry-pi-adjustable-air-quality-detector-running-on-gui-b7fb75]

from gpiozero import MCP3008
import time

mq135_channel = 0
threshold = 200  

#  MCP3008 object
adc = MCP3008(channel=mq135_channel)

while True:
        # Read the analog value from the MQ135 sensor
        sensor_value = adc.value

        # Print the sensor value and the result
        print(f"Sensor Value: {sensor_value} PPM")
        if sensor_value > threshold:
            print("Gas concentration is high!")
        else:
            print("Gas concentration is within safe levels.")

        # Wait for a short duration 
        time.sleep(1)
