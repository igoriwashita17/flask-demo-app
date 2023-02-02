import os

data = {
    'app': {
        'services': {
            'viacep': os.environ.get('SERVICE_VIACEP_BASE_PATH')
        }
    }
}