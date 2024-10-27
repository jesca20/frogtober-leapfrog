import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = "YOUR_API_KEY"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        rate = data["conversion_rate"]
        converted_amount = amount * rate
        print(f"{amount} {from_currency} is {converted_amount} {to_currency}")
    else:
        print("Currency conversion failed.")

amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ")
to_currency = input("To currency (e.g., EUR): ")
convert_currency(amount, from_currency, to_currency)
