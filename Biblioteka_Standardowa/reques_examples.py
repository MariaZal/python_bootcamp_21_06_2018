import json
import urllib.request as req

from collections import namedtuple
Currency = namedtuple('Currency',['currency', 'code', 'mid'])


response = req.urlopen("http://api.nbp.pl/api/exchangerates/tables/a/?format=json")
print(dir(response))
print(response.status)
resp_body = response.read()
# print(type(resp_body))
data = json.loads(resp_body)
print(data)
# print(type(data))

x = data[0]['rates'][0]
waluta = Currency(
    currency=x['currency'],
    code=x['code'],
    mid=x['mid']
)

print(waluta)
print(waluta.code)
print(help(waluta.index))
