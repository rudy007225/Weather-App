import request
#Text-to-Speech API
import win32com.client as wincom
import json
import requests

speak = wincom.Dispatch("SAPI.SpVoice")
welcomeText = "WELCOME TO WEATHER APP VERSION 1.0 DEVELOPED by Rudy"
print(f"--------------{welcomeText}-----------")
speak.Speak(welcomeText)

city = input("Enter the city : ")
url = f"http://api.weatherapi.com/v1/current.json?key=b9b8fb147e24430fa75202755240407&q={city}&aqi=no"

try :
    req = requests.get(url)
    whetherdic = json.loads(req.text)
    temprature_celcius = whetherdic["current"]["temp_c"]
    condition = whetherdic["current"]["condition"]["text"]
    lastUpdate = whetherdic["current"]["last_updated"]
    windDirection = whetherdic["current"]["wind_dir"]
    windSpeed = whetherdic["current"]["wind_kph"]
    humidity = whetherdic["current"]["humidity"]

    print("\n-------------------------------------------------------------")
    print(f"Temperature(Celcius) : {temprature_celcius}degree")
    print(f"Condition \t\t\t : {condition}")
    print(f"last updated at \t : {lastUpdate}")
    print(f"Wind-Direction \t\t : {windDirection}")
    print(f"Wind Speed \t\t\t : {windSpeed}kph")
    print(f"Humidity \t\t\t : {humidity}")

except Exception :
    print("Name must be incorrect or misspelled!!!")

print("-------------------------------------------------------------")
