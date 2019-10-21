import requests
from flask import request, Flask, jsonify

app = Flask(__name__)
app.config['DEBUG']=True

def get_allweathers(cityid):
    #returning all the weathers in several cities by inputing the cities' ID
    try:   
        param={
            'id':cityid,
            'units': 'metric',
            'appid':'3d6ae3df59815d39dbf27c8a52460ed0'
        }
        url = 'https://api.openweathermap.org/data/2.5/group'
        res = requests.get(url, params=param)
        return res.json()
    except Exception as e:
        res = "The Weathers Could Not Be Found"
        return res
        
def get_weathers(city):
    #returning the weather in a specific city by inputing the name of the city
    try:
        param={
            'q':city,
            'appid':'3d6ae3df59815d39dbf27c8a52460ed0'
        }
        url = 'https://api.openweathermap.org/data/2.5/weather'
        res = requests.get(url, params=param)
        return res.json()
    except Exception as e:
        res = "The Weather in"+city+"Could Not Be Found"
        return res

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET' :
        data = get_weathers(request.args.get('city'))
        weather_city = request.args.get('city')
        weather_country = data['sys']['country']
        weather_main = data['weather'][0]['main']
        weather_desc = data['weather'][0]['description']
        weather_temp = data['main']['temp']
        weather_wind = data['wind']['speed']
        res = {
            'city': weather_city,
            'country': weather_country,
            'main': weather_main,
            'desc': weather_desc,
            'temperature': weather_temp,
            'wind speed': weather_wind
        }
        return jsonify(res)

@app.route('/all', methods=['GET'])
def home():
    try:
        if request.method == 'GET' :
            data = get_allweathers(request.args.get('cityid'))
            res=[]
            
            for i in data['list']:
                weather_city = i['name']
                weather_country = i['sys']['country']
                weather_main = i['weather'][0]['main']
                weather_desc = i['weather'][0]['description']
                weather_temp = i['main']['temp']
                weather_wind = i['wind']['speed']
                tmp = {
                    'city': weather_city,
                    'country': weather_country,
                    'main': weather_main,
                    'desc': weather_desc,
                    'temperature': weather_temp,
                    'wind speed': weather_wind
                }
                res.append(tmp)

            return jsonify(res)
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run()
