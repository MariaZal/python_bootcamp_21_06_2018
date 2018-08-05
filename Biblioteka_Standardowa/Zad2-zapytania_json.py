# import modułów
# 1. biblioteka standardowa (alfabedyczna)
# 2. moduły obce
# 3. moduły Twoje własne
import json
import urllib.request as req

# adres = str("https://www.metaweather.com/api/location/search/?query=" +(input('jakie miasto: ')).lower()

# from collections import namedtuple
# Location = namedtuple('title',['title', 'woeid'])


#POBRANIE ID LOKALIZACJI
response = req.urlopen("https://www.metaweather.com/api/location/search/?query=" + (input('jakie miasto: ')).lower())
resp_body = response.read()
data = json.loads(resp_body)
# print(data)
x = data[0]
woeid = x.get('woeid', 0)
# print(woeid)

#POBRANIE POGODY
response_woeid = req.urlopen("https://www.metaweather.com/api/location/" + str(woeid))
info = response_woeid.read()
data_city = json.loads(info)

# print(data_city)

y = data_city['consolidated_weather']

for i in y:
    dzien = i.get('applicable_date', 0)
    print(f'DATA: {dzien}')

    for j in i:
        print(f'{j}: {i[j]}')

    print('\n')

#     print (c, y[i])
