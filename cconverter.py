import requests
import json

USER_CURR = input().lower()
URL = f"http://www.floatrates.com/daily/{USER_CURR}.json"

save_curr = {'usd': json.loads(requests.get(URL).text)['usd']['rate'] if USER_CURR != 'usd' else 1,
             'eur': json.loads(requests.get(URL).text)['eur']['rate'] if USER_CURR != 'eur' else 1}

while True:
    want_curr = input().lower()
    if want_curr:
        num_money = input()
        if num_money:
            num_money = float(num_money)
            print("Checking the cache...")
            if want_curr in save_curr:
                print("Oh! It is in the cache!")
                print(f"You received {round(save_curr[want_curr] * num_money, 2)} {want_curr.upper()}.")
            else:
                print("Sorry, but it is not in the cache!")
                save_curr[want_curr] = json.loads(requests.get(URL).text)[want_curr]['rate']
                print(f"You received {round(save_curr[want_curr] * num_money, 2)} {want_curr.upper()}.")
    else:
        exit()
