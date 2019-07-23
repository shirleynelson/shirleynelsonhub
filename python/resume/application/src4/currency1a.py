import requests

def main():
    #res = requests.get("http://data.fixer.io/api/latest?access_key=407693ce10c7b2ef9f3cda5ff59a0559&base=USD&symbols=EUR,GBP,CAD, AUD, PLN, MXN")
    res = requests.get("http://data.fixer.io/api/latest?access_key=407693ce10c7b2ef9f3cda5ff59a0559&symbols=EUR,USD,GBP,CAD, AUD, PLN, MXN")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["EUR"]
    print(f"1 EUR is equal to {rate} EUR")
    rate = data["rates"]["USD"]
    print(f"1 EUR is equal to {rate} USD")
    rate = data["rates"]["GBP"]
    print(f"1 EUR is equal to {rate} GBP")
    rate = data["rates"]["AUD"]
    print(f"1 EUR is equal to {rate} AUD")
    rate = data["rates"]["PLN"]
    print(f"1 EUR is equal to {rate} PLN")
    rate = data["rates"]["MXN"]
    print(f"1 EUR is equal to {rate} MXN")

if __name__ == "__main__":
    main()
#{"success":true,"timestamp":1563915607,"base":"EUR","date":"2019-07-23","rates":{"USD":1.115157,"GBP":0.896363,"CAD":1.464815,"AUD":1.591936,"PLN":4.255159,"MXN":21.383296}}
