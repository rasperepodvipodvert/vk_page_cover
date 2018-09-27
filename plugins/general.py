def get_btc_cost(coin):
    url = 'https://api.cryptonator.com/api/ticker/%s-usd' % coin
    import urllib.request, json
    data=[]
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data['ticker']['price']