import concurrent.futures
import json

import requests
from tqdm import tqdm

raw_text = "Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need two indices that will slice that portion from the list."
data = raw_text.split()
DATA = [w.upper() for w in data]

# Retrieve a single page and report the URL and contents
def get_lower(word):
    with requests.get('http://localhost:5000/api/lowercase/{}'.format(word)) as response:
        json_data = json.loads(response.text)
        return json_data['task']

if __name__ == '__main__':
    result = []
    data_list  = tqdm(DATA)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(get_lower, w): w for w in DATA}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))

