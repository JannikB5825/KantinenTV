import requests

url = "http://ergast.com/api/f1/current/driverStandings"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)