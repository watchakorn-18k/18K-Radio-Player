import json
import requests
import os

while True:
    solditems = requests.get('https://web-18k-mongodb-crud.herokuapp.com/api/get_18k_stat_request/') # (your url)
    print(solditems.json())
    