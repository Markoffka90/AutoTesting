import requests

############################################################################
#DELETE запрос на удаление питомца
pet_id = 9223372036854775807
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'api_key': 'special-key',
}
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}", headers=headers)

if 'application/json' in res.headers['Content-Type']:
    res.json()
    print(res.json())
else:
    res.text
    print(res.text)

print(res.status_code)