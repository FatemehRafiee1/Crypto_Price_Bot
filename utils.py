from coinex import get_price

def get_color(x):
    return '🟢' if x > 0 else '🔴'

def to_pct(x2, x1):
    return round((float(x2) / float(x1) - 1) * 100, 4)

def get_change(config, response: str):
    now = get_price(response, 2, "1min", config['coinex']['Access_ID'])
    hour = get_price(response, 2, "1hour", config['coinex']['Access_ID'])
    day = get_price(response, 2, "1day", config['coinex']['Access_ID'])
    week = get_price(response, 8, "1day", config['coinex']['Access_ID'])

    try:
        hc = to_pct(hour[-1]['close'], hour[-2]['close'])
        dc = to_pct(day[-1]['close'], day[-2]['close'])
        wc = to_pct(week[-1]['close'], week[-7]['close'])

        return now, hc, dc, wc
    except KeyError:
        return -1
    