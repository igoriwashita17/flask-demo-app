from services import viacep


class Adapter:
    def __init__(self):
        self.viacep = viacep

    def mapAddressData(self, address):
        return dict(
            postalCode=address.get('cep'),
            district=address.get('bairro'),
            addressType=address.get('logradouro').split(' ')[0],
            address=address.get('logradouro'),
            state=address.get('localidade'),
            city=address.get('uf'),
        )

    def getAddress(self, payload):
        address = self.viacep.getAddress(payload['cep'])
        return self.mapAddressData(address)
