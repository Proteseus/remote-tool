import requests
import json
from flask import jsonify

url = "https://community-open-weather-map.p.rapidapi.com/weather" 

class Weather():
    def fetch_weather(self, city):
        querystring = {"q":city,"lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"} 
        headers = {  
                "X-RapidAPI-Key": "b307c522a0msh3c285eddbe5c155p170e24jsn00d3a1167ff6",  
                "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
        } 
        
        response = requests.request("GET", url, headers=headers, params=querystring) 
        
        if(response.status_code == 200):
            with open("./static/weather_results.json", "w") as res:
                res.write(response.text)
            
            with open("./static/weather_results.json", "r") as responseFile:
                global data
                
                string = responseFile.read()
                ind = len(string)-1
                
                data = json.loads(string[5: int(ind)])
                js = json.dumps(data, indent=4)
                with open("./static/weather_results.json", "w") as res:
                    res.write(js)
                
        elif (response.status_code == 404):
            data = -1
            print("Result not found!")
        elif(response.status_code == 502):
            print("API DOWN")
    
    def fetch_status(self):
        print(data)
        return data
    def get_weather(self):
        weather_current = data['weather'][0]['main']
        icon_current = data['weather'][0]['icon']
        
        wr = {'weather': weather_current, 'icon': icon_current}
        return wr
    def get_temp(self):
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        
        wr = {'temp': temp, 'feels_like': feels_like, 'pressure': pressure, 'humidity': humidity}
        return wr
    def get_info(self):
        visibility = data['visibility']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        name = data['name']
        
        wr = {'visibility': visibility, 'wind_speed': wind_speed, 'wind_deg': wind_deg, 'name': name}
        return wr
        