from martins_package.weather import search_city, weather_forecast, main

query = 'london'

def test_city():
    assert type(search_city(query)) == dict
