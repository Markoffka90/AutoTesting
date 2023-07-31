import requests

############################################################################
#GET запрос на получение списка питомцев с определенным статусом
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

if 'application/json' in res.headers['Content-Type']:
    res.json()
    print(res.json())
else:
    res.text
    print(res.text)

print(res.status_code)




