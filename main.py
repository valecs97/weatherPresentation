import sys

import requests
import json

if __name__ == '__main__':
    pass
if len(sys.argv) == 1:
    print('Not enough arguments')
    exit(1)

apikey = '2ac04471f9d1ce57945ab013f3522809'
city = sys.argv[1]

r = requests.post("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID="+apikey)
response = json.loads(r.text)
if 'main' in response:
    celsiusDegrees = response['main']['temp'] - 273.15
    sky = response['weather'][0]['main']
    print("%.1f" % celsiusDegrees + " celsius degrees")
    print(sky)
    print('\nHello there !!')
else:
    print('Error in getting the weather, perhaps you didn\'t spell the city right')
    print('(1)You spelled : ' + city)

