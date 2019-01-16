import sys, io, requests,csv,json, string, os, collections
import config as cfg
from function import id_generator


csv.register_dialect('myDialect',
    delimiter = ',',
    quotechar="'",
    quoting=csv.QUOTE_ALL)

SobjectConfig = sys.argv[1]

func = getattr(cfg, SobjectConfig)

parse_json = json.loads(func['FIELDS'])

url = cfg.mockConfig['BASE_URL'] + cfg.mockConfig['GENERATE_TYPE'] + '?key=' + cfg.mockConfig['API_KEY'] + '&count=' + cfg.mockConfig['ROW_COUNT']

for i in range(cfg.mockConfig['FILE_COUNT']):

    fileName = id_generator()

    with requests.Session() as s:
            download = s.post(url, json=parse_json)
            decoded_content = download.content.decode('utf-8')

            #cr = csv.reader(decoded_content.splitlines(), delimiter=',', quotechar="'")
            #foutput = list(cr)

            #open(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv', 'w').write(decoded_content, dialect=QUOTE_ALL)

            with open(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv', 'w') as f:
                writer = csv.writer(f, dialect='myDialect')
                reader = csv.reader(decoded_content.splitlines())

                for row in reader:
                    writer.writerow(row)

            os.system('python bulkLoad.py ' + cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv ' + SobjectConfig)

print(str(cfg.mockConfig['FILE_COUNT']) + ' files created.')
