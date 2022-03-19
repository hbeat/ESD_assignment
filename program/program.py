import requests
import json 

url = 'http://127.0.0.1:5000/get_data'
res = requests.get(url)
response = json.loads(res.text)
with open('api_data.txt', 'w') as f:
    f.write(res.text)
    f.close()
print("Product get from api:")
for product in response["products"]:
    print(product)
