import sys

import requests
import csv
import json
import config as cfg

import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


SobjectConfig = sys.argv[1]

func = getattr(cfg, SobjectConfig)

parse_json = json.loads(func['FIELDS'])

url = cfg.mockConfig['BASE_URL'] + cfg.mockConfig['GENERATE_TYPE'] + '?key=' + cfg.mockConfig['API_KEY'] + '&count=' + cfg.mockConfig['ROW_COUNT']


for i in range(cfg.mockConfig['FILE_COUNT']):


        with requests.Session() as s:
            download = s.post(url, json=parse_json)
            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            foutput = list(cr)
            #for row in foutput:
            with open(cfg.mockConfig['FILE_OUTPUT_PATH'] + id_generator() + '.csv', mode='w') as testOutput:
                    testOutput = csv.writer(testOutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    testOutput.writerow([foutput])

print(str(cfg.mockConfig['FILE_COUNT']) + ' files created.')
