# import Adafruit_DHT
# from gpiozero import DistanceSensor
import random
import time
import matplotlib.pyplot as plt
from datetime import datetime

logFile = open('log.txt', 'a') # open the log file for writing.

dhtPin = 4 # should be changed to an appropriate pin.
dht = None # the DHT sensor instance.

echoPin = 18 # should be changed to an appropriate pin.
triggerPin = 17 # should be changed to an appropriate pin.
distanceSensor = None # the distance sensor instance.

# def setupDHT():
#     dht = Adafruit_DHT.DHT11 # get the dht sensor instance.
#     return

# def readTemp():
#     humidity, temperature = Adafruit_DHT.read(dht,  dhtPin) # read data from the sensor.
#     logFile.write(f'[{datetime.now()}] - Temperature: {temperature:.1f}C  Humidity: {humidity:.1f}%\n') # write the temperature and humidity values to the log file
#     return humidity, temperature # return the data.

# this function is for testing on non raspberry pi devices.
def setupDHT():
    return

# this function generates random values to simulate the process of reading data from the dht sensor.
def readTemp():
    humidity = random.uniform(0, 60) # get a random humidity value.
    temperature = random.uniform(0, 100) # get a random temperature value.
    logFile.write(f'[{datetime.now()}] - Temperature: {temperature:.1f}C  Humidity: {humidity:.1f}%\n') # write the temperature and humidity values to the log file
    return humidity, temperature

# def setupDistance():
#     distanceSensor = DistanceSensor(echo=echoPin, trigger=triggerPin) # get the distance sensor instance.
#     return

# def readDistance():
#     distance = distanceSensor.distance * 100  # convert to centimeters
#     logFile.write(f'[{datetime.now()}] - Distance: {distance:.1f} cm\n') # write the distance value to the log file.
#     return distance

# this function is for testing on non raspberry pi devices.
def setupDistance():
    return

# this function generates random values to simulate the process of reading data from the ultrasonic sensor.
def readDistance():
    distance = random.uniform(10, 400) # get a random distance value.
    logFile.write(f'[{datetime.now()}] - Distance: {distance:.1f} cm\n') # write the distance value to the log file.
    return distance

setupDHT() # setup the sensor (if on raspberry pi device) or call the testing function (if on non raspberry pi device).
setupDistance() # setup the sensor (if on raspberry pi device) or call the testing function (if on non raspberry pi device).

# Lists to store the data
temperatures = []
humidities = []
distances = []
timestamps = []

for i in range(60):
    humidity, temperature = readTemp() # read values from sensor (if on raspberry pi device) or get random values (if on non raspberry pi device).
    distance = readDistance()

    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature:.1f}C  Humidity: {humidity:.1f}%')
    else:
        print('Failed to get reading. Try again!')

    print(f'Distance: {distance:.1f} cm')

    # time.sleep(1) # commented this line out to speed up the testing process.

    temperatures.append(temperature)
    humidities.append(humidity)
    distances.append(distance)
    timestamps.append(i)


plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(timestamps, temperatures, marker='o', label='Temperature (C)')
plt.plot(timestamps, humidities, marker='o', label='Humidity (%)')
plt.title('Temperature and Humidity Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(timestamps, distances, marker='o', color='r', label='Distance (cm)')
plt.title('Distance Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Distance (cm)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

logFile.close() # close the log file.