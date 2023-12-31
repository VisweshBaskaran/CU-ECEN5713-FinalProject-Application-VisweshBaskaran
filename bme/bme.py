import bme280
import smbus2
from time import sleep

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(f"Humidity: {humidity:.2f}%")
    print(f"Pressure: {pressure:.2f} hPa")
    print(f"Ambient Temperature: {ambient_temperature:.2f} °C")
    sleep(3)