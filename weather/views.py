from django.shortcuts import render
import requests

'''
    weather app in django using API.
    https://openweathermap.org
    
    this app shows the temperature in fahrenheit by default
    but can show the temperature in celsius ((°F − 32) × 5/9) = °C
    
'''


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


def index(request):
    # the query(q) is the name of city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={YOUR_APP_KEY}'
    city_name = request.GET.get( 'q' )
    if city_name is None:
        city_name = 'Gorgan'
    response = requests.get( url.format( city_name ) ).json()  # response now is a python dictionary
    print( response )
    temperature = 'F'
    try:
        context = {
            'city': response['name'],  # name of the city
            'country': response['sys']['country'],  # name of the country of the city
            'description': response['weather'][0]['description'],  # list of dictionary
            'temperature': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        if temperature == 'C':
            context['temperature'] = convert_to_celsius( context['temperature'] )
    except:
        print( response.get( 'code' ) )
        context = {
            'error': f'{city_name} City Not Found!'
        }
    return render( request, 'weather/weather-index.html', context )
