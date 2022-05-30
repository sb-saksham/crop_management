import serial
import time
import re
import requests
import json

humidity = []
temperature = []
sunlight = []

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

for i in range(50):
    line = ser.readline()   # read a byte
    if line:
        line_str = line.decode()  # convert the byte string to a unicode string
        hum = re.search("Humidity: (\d+)", line_str)
        temp = re.search("Temperature: (\d+)", line_str)
        sun = re.search("Sunlight: (\d+)", line_str)
        if hum:
            hum = int(hum.group(1))
            print("hum:", hum)
            humidity.append(hum)
        if temp:

            temp = int(temp.group(1))
            print("temp:", temp)
            temperature.append(int(temp))
        if sun:
            sun = int(sun.group(1))
            print("sun:",sun )
            sunlight.append(int(sun))

headers = {
    "Content-Type": "application/json",
}
localhost_url = "http://127.0.0.1:8000"
production_host_url = "https://cropmanagement.pythonanywhere.com/"
endpoint = production_host_url+"/api/"
humidity = int((sum(humidity)/len(humidity)))
temperature = int((sum(temperature)/len(temperature)))
sunlight = int((sum(sunlight)/len(sunlight)))
data = {
    'humidity': int((sum(humidity)/len(humidity))),
    'temperature': int((sum(temperature)/len(temperature))),
    'sunlight': int((sum(sunlight)/len(sunlight))),
}
humidity_is_ok = humidity >= 45 and humidity <=65
temperature_is_ok = temperature >= 25 and temperature <= 45
sunlight_is_ok = sunlight >= 900 and sunlight <= 1100
crop_health = 5
if humidity_is_ok and temperature_is_ok and sunlight_is_ok:
    crop_health = 9
else:
    crop_health = 3
data['crop_health'] = crop_health
r = requests.post(endpoint, data=json.dumps(data), headers=headers)
print(r.json())
ser.close()
