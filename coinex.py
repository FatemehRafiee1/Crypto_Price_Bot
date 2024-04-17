import requests

keyword_responses = {
    '/Bitcoin': 'BTCUSDT',
    '/Ethereum': 'ETHUSDT',
    '/XRP': 'XRPUSDT',
    '/Solana': 'SOLUSDT',
    '/Shiba': 'SHIBUSDT',
    '/Cardano': 'ADAUSDT',
    '/BNB': 'BNBUSDT',
    '/Dogecoin': 'DOGEUSDT',
    '/Toncoin': 'TONUSDT',
    '/Avalanche': 'AVAXUSDT',
    '/other': 'user'
}

def get_price(coin: str, limit: int, period: str, api_key: str):

    endpoint = "https://api.coinex.com/v2/spot/kline"

    params = {
        "market": coin,        
        "limit": limit,
        "period": period
    }

    headers = {
        "X-COINEX-KEY": api_key
    }
    
    response = requests.get(endpoint, params=params, headers=headers)

    data = response.json()
    return data['data']
