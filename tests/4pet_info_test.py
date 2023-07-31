import requests

############################################################################
#GET запрос на получение информации о питомце
pet_id = 9223372036854608446
headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}
res = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}", headers=headers)

if 'application/json' in res.headers['Content-Type']:
    res.json()
    print(res.json())
else:
    res.text
    print(res.text)

print(res.status_code)