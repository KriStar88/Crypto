import  requests
import json
import pprint

result = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
data = json.loads(result.text)
for coin in data:
    if coin['id'] == 'bitcoin':
        res = coin['id']
        print(coin['id'], coin['current_price'])



