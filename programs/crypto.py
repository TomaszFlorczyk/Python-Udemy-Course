import requests

coinsList = None
currency = "pln"

def getCoinsList():
    global coinsList
    #{'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}}

    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("Response ok")
        data = response.json()
        print(data[0])
        print("Ilość kryptowalut: " + str(len(data)))
        coinsList = data

def findCoinBySymbol(symbol):

    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None

def getCoinLastMarketData(coinId):
    #{'bitcoin': {'pln': 100383, 'pln_market_cap': 1916933293948.3464, 'pln_24h_vol': 161081057657.8612, 'pln_24h_change': -4.920317412142026, 'last_updated_at': 1658760293}}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+currency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data = response.json()
        return data
    else:
        None

def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]
    
getCoinsList()

btcData = findCoinBySymbol("btc")
print(btcData)

marketData = getCoinLastMarketData(btcData["id"])

print("marketData: ", marketData)

coinPrice = getCoinPriceInCurrency(btcData["id"], currency)
print("Coin price in "+ currency, coinPrice)

print("\nWitamy w crypto exchange")

while True:
    cryptoSymbolToBuy = input("Wybierz symbol crypto do kupienia np. btc lub exit by wyjść: ")
    if cryptoSymbolToBuy == "exit": break

    coinData = findCoinBySymbol( cryptoSymbolToBuy)
    if coinPrice == None:
        print("Nie ma takiej cryptowaluty")
        continue

    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena " + str(coinData["id"]), coinPrice, currency)

    moneyToBuyCrypto = float( input("Ile chcesz przeznaczyć na zakup: "))
    boughtCrypto = moneyToBuyCrypto/coinPrice

    print("\n Gratulacje kupiłeś " + str(boughtCrypto) + " " + cryptoSymbolToBuy)