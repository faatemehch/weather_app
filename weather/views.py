from django.shortcuts import render
import requests

'''
    weather app in django using API.
    https://openweathermap.org
    
    this app shows the temperature in fahrenheit by default
    but can show the temperature in celsius as well --> ((°F − 32) × 5/9) = °C
'''


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


def index(request):
    # the query(q) is the name of city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8f310c4694db72dd9df4accd477b9bd'
    city_name = request.GET.get( 'q' )
    if city_name is None:  # consider a city as default
        city_name = 'New York'
    response = requests.get( url.format( city_name ) ).json()  # response now is a python dictionary
    temperature = 'F'
    # print(response)
    try:
        context = {
            'city': response['name'],  # name of the city
            'country': response['sys']['country'],  # name of the country of the city
            'description': response['weather'][0]['description'],  # list of dictionary
            'temperature': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        print( convert_to_celsius( context['temperature'] ) )

    except:
        # print( response.get( 'code' ) )
        context = {
            'error': f'{city_name} City Not Found!'
        }
    return render( request, 'weather/weather-index.html', context )
