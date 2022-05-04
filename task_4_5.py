import requests
from requests import get, utils


def currency_rates(argv):
    program, *args = argv
    charcode = currency.upper()
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    val_dict = response['Valute']
    if charcode in val_dict:
        return(response['Valute'][charcode]['Value'])
    else:
        return None
    result = currency_rates(currency)
    print(f'результат: {result}')


currency = input('Введите код валюты ')

if __name__ == '__main__':
    import sys
    exit(currency_rates(sys.argv))



