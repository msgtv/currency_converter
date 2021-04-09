import requests
import json


class CurrencyConverter:
    URL = None
    USER_CURR = None
    cash = None

    def __init__(self, url, user_curr):
        self.URL = url
        self.USER_CURR = user_curr
        self.cash = {'usd': json.loads(requests.get(URL).text)['usd']['rate'] if USER_CURR != 'usd' else 1,
                     'eur': json.loads(requests.get(URL).text)['eur']['rate'] if USER_CURR != 'eur' else 1}

    def converting(self, want_currency, num_m):
        if want_currency in self.cash:
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            self.cash[want_currency] = json.loads(requests.get(URL).text)[want_currency]['rate']
        print(f"You received {round(self.cash[want_currency] * num_m, 2)} {want_currency.upper()}.")

    def work(self):
        while True:
            want_curr = input("Please, enter the currency code that you want to receive: ").lower()
            if want_curr:
                num_money = float(input("Please enter the amount of money that you have: "))
                self.converting(want_curr, num_money)
            else:
                quit()


def get_constant():
    curr = input("Please, enter currency code that you have: ").lower()
    link = f"http://www.floatrates.com/daily/{curr}.json"
    return curr, link


USER_CURR, URL = get_constant()
converter = CurrencyConverter(USER_CURR, URL)
converter.work()
