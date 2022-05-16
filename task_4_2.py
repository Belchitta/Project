import requests
from requests import get, utils


def currency_rates():
    charcode = currency.upper()
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    val_dict = response['Valute']
    if charcode in val_dict:
        return(response['Valute'][charcode]['Value'])
    else:
        return None


currency = input('Введите код валюты ')
result = currency_rates()
print(result)


