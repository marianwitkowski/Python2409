
# Kursy walut z NBP
import requests
import json

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"
response = requests.get(url)
data = json.loads(response.text)[0]["rates"]
data = response.json()[0]["rates"]
for item in data:
    print(f"{item['currency']} - {item['code']} - {item['mid']}")