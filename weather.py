import requests
from datetime import datetime

api_key = "5fc099a0618f7a66fc2c0692ec87a346"
location = input("Enter the city name: ")

# getting api link
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# display data
print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')

# save data in text file
file = open("weather.txt", "a")
file.write("-------------------------------------------------------------\n")
file.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
file.write("-------------------------------------------------------------\n")

file.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
file.write("Current weather desc  :{}\n".format(weather_desc))
file.write("Current Humidity      : {}% \n".format(hmdt))
file.write("Current wind speed    : {}kmph\n".format(wind_spd))
file.close()