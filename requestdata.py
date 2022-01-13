import requests
from datetime import date as d


def request_currency():
    date = d.today().strftime("%d.%m.%Y")
    data = requests.get(f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}")
    json = data.json()
    status = data.status_code
    currencies = json["exchangeRate"]

    return currencies, status


if __name__ == "__main__":
    print(request_currency())
