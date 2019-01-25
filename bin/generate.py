import sys, io, requests,csv,json, string, os, collections
import config as cfg
from function import id_generator


csv.register_dialect('myDialect',
    delimiter = ',',
    quotechar="'",
    quoting=csv.QUOTE_ALL)

SobjectConfig = sys.argv[1]

url = cfg.mockConfig['BASE_URL'] + cfg.mockConfig['GENERATE_TYPE'] + '?key=' + cfg.mockConfig['API_KEY'] + '&count=' + cfg.mockConfig['ROW_COUNT']

for i in range(cfg.mockConfig['FILE_COUNT']):
    func = getattr(cfg, SobjectConfig)

    with open('../schema/' + func['SCHEMA']) as f:
        parse_json = json.load(f)

    #parse_json = json.loads(func['FIELDS'])

    fileName = id_generator()

    with requests.Session() as s:
            download = s.post(url, json=parse_json)
            decoded_content = download.content.decode('utf-8')

            with open(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv', 'w') as f:
                writer = csv.writer(f, dialect='myDialect')
                reader = csv.reader(decoded_content.splitlines())

                for row in reader:
                    writer.writerow(row)

            os.system('python bulkLoad.py ' + cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv ' + SobjectConfig)

            #delete file regardless of result
            os.remove(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv')

#print to console result
#will eventual upload results to Mockaroo as DataSet to be used in subsequent calls.
    f = open(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv.result')
    with f:
        reader = csv.reader(f)
        for row in reader:
            for e in row:
                print(e)
