
from api_key import API_KEY
import requests


def convertor(source, target, amount):
    url = 'https://api.forexrateapi.com/v1/convert'
    params = {
        'api_key': API_KEY,
        'from': source,
        'to': target,
        'amount': amount,
    }

    response = requests.get(url, params=params)
    return response.json()['result']


def get_amount():

    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD):').upper()
        if currency not in currencies:
            print('Invalid currency')
        else:
            return currency


def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    final_amount = convertor(source_currency, target_currency, amount)
    print(f'{amount:.2f} {source_currency} is equal to {final_amount:.2f} {target_currency}')


if __name__ == '__main__':
    main()
