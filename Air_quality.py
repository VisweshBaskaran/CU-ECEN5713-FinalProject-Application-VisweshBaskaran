# Author : Visweshwaran 
# File name: Air_quality.py
# File Description: Driver code for MQ135 sensor
# Reference: Based on Raspberry Pi Adjustable hackster.io blog [https://www.hackster.io/kutluhan-aktar/raspberry-pi-adjustable-air-quality-detector-running-on-gui-b7fb75]
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep

# Create the SPI bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)


# Create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)


# Create the mcp object
mcp = MCP.MCP3008(spi, cs)


# Create analog inputs connected to the input pins on the MCP3008.
channel_0 = AnalogIn(mcp, MCP.P0)

# Define a function to evaluate the sensor value and print if it's safe or not
def evaluateSensorValue():
    # Test your module, then define the value range - in this case between 0 and 60000.
    sensorValue = int((channel_0.value - 0) * (1023 - 0) / (60000 - 0) + 0)
    
    print("Air Quality Sensor Value:", sensorValue)
    
    # Threshold
    if(sensorValue > 300):
        print("Status: DANGER - Air Quality Deteriorating!")
    else:
        print("Status: OK")


# Continuously monitor and display the sensor value and status
while True:
    evaluateSensorValue()
    sleep(1)
