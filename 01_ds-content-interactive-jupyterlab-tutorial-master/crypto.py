import requests
import pandas as pd
# import json


def get_historic_price(symbol, currency, limit,  before='2023-10-17'):
    to_date = str(int(pd.Timestamp(before).timestamp()))
    url = f'https://min-api.cryptocompare.com/data/v2/histohour?fsym={symbol}&tsym={currency}&toTs={to_date}&limit={limit}'
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    # data = json.dumps(resp.json(), indent=2)
    # print(data)
    # input()
    df = pd.DataFrame(data['Data']['Data'], columns=[
        'time', 'high', 'low', 'open', 'volumefrom', 'volumeto',  'close', 'conversionType', 'conversionSymbol', 'NA'
    ])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df


time = '2023-10-17'
data_points = 2000


btc = get_historic_price('BTC', 'USD', data_points, time)

print(btc.head())

print(btc.show)

