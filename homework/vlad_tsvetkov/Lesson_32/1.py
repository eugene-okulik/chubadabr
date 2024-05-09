import requests
from time import sleep

while True:
    response = requests.get('https://google.com')
    assert response.status_code == 200
    print("Пока в гугле не забанили")
    sleep(10)
