
from tools.tools_module import *
from pyautogui import *
from tools.notifyer import notification
import json
import urllib.request
import datetime

weather = ""
city = ""
type = "default"

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time

def url_builder(city):
    # print(city)
    user_api = 'deba549f672cda8326f3888177fcb067'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?q='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city) + '&mode=json&units=' + unit + '&APPID=' + user_api
    # print(full_api_url)
    return full_api_url

def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    # print(raw_api_dict)
    return raw_api_dict

def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    # print(data)
    return data


def data_output(data):
    global weather
    global type
    m_symbol = '\xb0' + 'C'

    if type == "user_input":
        speak('Current weather in: {}, {}:'.format(data['city'], data['country']))
        speak('Tempareture is: {},{}'.format(data['temp'], m_symbol, data['sky']))
        speak('Max Tempareture is: {}, Min Tempareture is: {}'.format(data['temp_max'], data['temp_min']))
        speak('Wind Speed is: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
        speak('Humidity is: {}'.format(data['humidity']))
        speak('Cloud is: {}'.format(data['cloudiness']))
        speak('Pressure is: {}'.format(data['pressure']))
        speak('Sunrise at: {}'.format(data['sunrise']))
        speak('Sunset at: {}'.format(data['sunset']))
        speak('Last update from the server: {}'.format(data['dt']))
        speak("Thank You!")
        notification("Current Tempareture in "+str(data['city']),str(data['temp'])+""+m_symbol+" "+str(data['sky']))
    else:
        weather = str(data['temp'])+str(m_symbol+"  "+str(data['sky']))
    # print(weather)

## ==> GET WEATHER FUNCTION
def get_current_weather(inputType,self,city_name):
    global city
    global weather
    city = city_name
    global type
    type = 'default'

    try:
        data_output(data_organizer(data_fetch(url_builder(city.capitalize()))))
        # print("done")
        return weather
    except:
        # print('no internet')
        return "Uhh!"
    print(weather)


def find_temperature(inputType,self,city_name):
    global city
    global weather
    global type
    city = city_name

    type = "user_input" # INPUT TYPE LIKE VOICE OR KEYBOARD
    try:
        data_output(data_organizer(data_fetch(url_builder(city.capitalize()))))
        return weather
    except IOError:
        speak("Sorry, I am not able to fetch the data from the server......")
        speak("may be city name is incorrect or....... due to network issue?...Try again!......")
        return