from django.shortcuts import render
import requests

'''
    weather app in django using API.
    https://openweathermap.org
'''


def index(request):
    # the query(q) is the name of city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = request.GET.get( 'q' )
    if city is None:
        city = 'Gorgan'
    response = requests.get( url.format( city ) ).json()
    # print( response )
    # response now is a python dictionary
    context = {
        'city': response['name'],  # name of the city
        'country': response['sys']['country'],  # name of the country of the city
        'description': response['weather'][0]['description'],  # list of dictionary
        'temperature': response['main']['temp'],
        'icon': response['weather'][0]['icon']
    }
    return render( request, 'weather/weather-index.html', context )
