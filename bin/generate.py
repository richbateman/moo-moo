import sys, io

import requests,csv,json,string,random
import config as cfg


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

            open(cfg.mockConfig['FILE_OUTPUT_PATH'] + id_generator() + '.csv', 'w').write(decoded_content)

            #with open(cfg.mockConfig['FILE_OUTPUT_PATH'] + id_generator() + '.csv', 'wb') as fileOutput:
              #  wr = csv.writer(fileOutput, quotechar="'", quoting=csv.QUOTE_ALL, lineterminator='\n')
               # wr.writerow(cr)

            for row in foutput:
                    print(row)

print(str(cfg.mockConfig['FILE_COUNT']) + ' files created.')
