import requests
import json
from flask import jsonify

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current" 

class Weather():
    def fetch_weather(self):
        querystring = {"lat":"9.0","lon":"38.7","units":"metric","lang":"en"}

        headers = {
            "X-RapidAPI-Key": "fbc3f7553bmshc5986cd99c61e17p1514a6jsn9a924f8deda7",
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }
        
        response = requests.request("GET", url, headers=headers, params=querystring) 
        
        if(response.status_code == 200):
            with open("./static/weather_results.json", "w") as res:
                res.write(response.text)
            
            with open("./static/weather_results.json", "r") as responseFile:
                global data
                data = json.load(responseFile)
        elif (response.status_code == 404):
            data = -1
            print("Result not found!")
        elif(response.status_code == 502):
            print("API DOWN")
    
    def fetch_status(self):
        print(data)
        return data
    def get_weather(self):
        weather_current = data['data'][0]['weather']['description']
        icon_current = data['data'][0]['weather']['icon']
        
        wr = {'weather': weather_current, 'icon': icon_current}
        return wr
    def get_temp(self):
        temp = data['data'][0]['temp']
        feels_like = data['data'][0]['app_temp']
        pressure = data['data'][0]['pres']
        humidity = data['main']['humidity']
        
        wr = {'temp': temp, 'feels_like': feels_like, 'pressure': pressure, 'humidity': humidity}
        return wr
    def get_info(self):
        visibility = data['data'][0]['vis']
        wind_speed = data['data'][0]['wind_spd']
        wind_deg = data['data'][0]['wind_dir']
        name = data['data'][0]['city_name']
        
        wr = {'visibility': visibility, 'wind_speed': wind_speed, 'wind_deg': wind_deg, 'name': name}
        return wr
        