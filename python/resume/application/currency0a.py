import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=407693ce10c7b2ef9f3cda5ff59a0559&symbols=USD,GBP,CAD, AUD, PLN, MXN")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
