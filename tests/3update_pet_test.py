import requests

############################################################################
#PUT запрос на редактирование информации о питомце
data = {
  "id": 9223372036854608446,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Mantis",
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

res = requests.put(f"https://petstore.swagger.io/v2/pet",  json=data, headers=headers)

if 'application/json' in res.headers['Content-Type']:
    res.json()
    print(res.json())
else:
    res.text
    print(res.text)

print(res.status_code)