import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

headers = {
	"X-RapidAPI-Key": "6f6b0083aamsh7ca17d6935d9f44p108bb7jsnd50fa74eab53",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)