import requests

url = 'https://my.sdu.edu.kz/index.php?mod=schedule'
response = requests.get(url, verify='/path/to/certfile')

print(response.content)

