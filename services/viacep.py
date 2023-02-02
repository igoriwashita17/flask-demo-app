import requests
from config import default


def getAddress(cep):
    r = requests.get(f'{default.data["app"]["services"]["viacep"]}/ws/{cep}/json')
    return r.json()
