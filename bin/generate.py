import sys

import requests
import csv
import json
import config as cfg

SobjectConfig = sys.argv[1]
generate_type = cfg.mockConfig['GENERATE_TYPE']
file_type = generate_type.split('.')

print(file_type[1])
func = getattr(cfg, SobjectConfig)

parse_json = json.loads(func['FIELDS'])

url = cfg.mockConfig['BASE_URL'] + generate_type + '?key=' + cfg.mockConfig['API_KEY'] + '&count=' + cfg.mockConfig['ROW_COUNT']

if 'json' in generate_type:
    response = requests.post(url, json=parse_json)
    json_data = json.loads(response.text)
    print(json_data)

elif 'csv' in generate_type:
    with requests.Session() as s:
        download = s.post(url, json=parse_json)
        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)
else:
    print("No File Type Defined")