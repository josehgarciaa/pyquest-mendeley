import requests
import json

client_id = input("Enter your client_id: ")
client_secret = input("Enter your client_secret: ")

url = "https://api.mendeley.com/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "scope": "all",
    "client_id": str(client_id),
    "client_secret": str(client_secret)
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)

# write the dictionary to a JSON file
with open("credentials.json", "w") as f:
    json.dump(response.text, f)

