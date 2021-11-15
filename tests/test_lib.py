from martins_package.weather import *

query = 'london'

def test_city():
    assert type(search_city(query)) == dict
