import json

import requests

if __name__ == '__main__':
    response = requests.get('http://localhost:5000/api/lowercase/CASA')
    json_data = json.loads(response.text)
    print(json_data['task'])