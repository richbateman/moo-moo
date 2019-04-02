import codecs, sys, requests
import config as cfg

fileName = sys.argv[1]
SobjectConfig = sys.argv[2]
headers = {'content-type': 'text/csv'}

url = cfg.mockConfig['BASE_URL'] + 'upload?key=' + cfg.mockConfig['API_KEY'] + '&name=' + fileName + '&filename=' + fileName + '.csv'

with codecs.open(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv.dataset', 'r', encoding='utf8') as f:
    body = f.read()

with requests.Session() as s:
    upload = s.post(url, data=body, headers=headers)
