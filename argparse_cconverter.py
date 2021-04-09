import argparse
import requests
import json

parser = argparse.ArgumentParser()

parser.add_argument('--have_curr', type=str, help="Enter currency code that you have.")
parser.add_argument('--want_curr', type=str, help="Enter the currency code that you want to receive.")
parser.add_argument('--num_money', type=float, help="Enter the amount of money that you have.")

args = parser.parse_args()

user_curr = args.have_curr.lower()
want_curr = args.want_curr.lower()
num_money = args.num_money

URL = f"http://www.floatrates.com/daily/{user_curr}.json"
rate = json.loads(requests.get(URL).text)[want_curr]['rate'] if user_curr != want_curr else 1
print(f"You received {round(rate * num_money, 2)} {want_curr.upper()}.")
