import requests

url = 'https://v6.exchangerate-api.com/v6/4cab895b483d2a50aaa826e2/latest/USD'
response = requests.get(url)
data = response.json()

sek_rate = data['conversion_rates']['SEK']

def user_Select(choice):
    selectedRate=data['conversion_rates'][choice]
    return selectedRate
