#!/usr/bin/env python

import pyowm
import os

    # get variables values
api_key = os.environ['OPENWEATHER_API_KEY']
city = os.environ['CITY_NAME']
source = "openweathermap"

    # access the API with functional KEY
owm = pyowm.OWM(API_key=api_key,version='2.5', config_module=None, language=None, subscription_type=None)

    #get weather for specifies city (or cities with same name, for max 10 cities)
city_weather = owm.weather_at_place(city)
#city_weather = owm.weather_at_places(city,'like',10)

    #get info about conditions in the city
current_weather = city_weather.get_weather()
location = city
description = current_weather.get_detailed_status()
temperature = current_weather.get_temperature(unit='celsius')
humidity = current_weather.get_humidity()

    # because actual temperature is just one of item in disctionary, we access it via distionary_name["<name>"]
temp = temperature["temp"]


print ("source= "+ source + ", city =\""+ location + "\", desciption =\""+ description + "\", temp = " + str(temp) + ", humidity = " + str(humidity))

