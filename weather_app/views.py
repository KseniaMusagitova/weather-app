import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=uk&APPID=b7f7ccc381e0ac66f5bfeef48dfa5011'
    city = 'London'

    r = requests.get(url.format(city)).json()
  

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}


    return render(request, 'weather/weather.html', context)