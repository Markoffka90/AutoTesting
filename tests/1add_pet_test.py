import requests

############################################################################
#POST запрос на добавление нового питомца
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Leo",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "sweet"
    }
  ],
  "status": "available"
}
headers = {'accept': 'application/json',
          'Content-Type': 'application/json'}

res = requests.post(f"https://petstore.swagger.io/v2/pet",  json=data, headers=headers)

if 'application/json' in res.headers['Content-Type']:
    res.json()
    print(res.json())
else:
    res.text
    print(res.text)

print(res.status_code)