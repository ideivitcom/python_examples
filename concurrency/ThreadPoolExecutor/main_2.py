import json

import requests
from tqdm import tqdm

raw_text = "Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need two indices that will slice that portion from the list."
data = raw_text.split()
DATA = [w.upper() for w in data]

if __name__ == '__main__':
    result = []
    data_list  = tqdm(DATA)
    for w in data_list:
        response = requests.get('http://localhost:5000/api/lowercase/{}'.format(w))
        json_data = json.loads(response.text)
        result.append(json_data['task'])

    a=1