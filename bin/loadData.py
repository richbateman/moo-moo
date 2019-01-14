import fnmatch,os
import config as cfg
import csv

#Create Salesforce object
from authenticate import auth
sf = auth()

for filename in os.listdir(cfg.mockConfig['FILE_OUTPUT_PATH']):
    if filename.endswith(".csv"):
            print(filename)
            with open(cfg.mockConfig['FILE_OUTPUT_PATH'] + filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:
                        print(f'Data: {", ".join(row)}')
                        line_count += 1
                print(f'Processed {line_count} lines.')

num_files = len(fnmatch.filter(os.listdir(cfg.mockConfig['FILE_OUTPUT_PATH']), '*.csv'))
print('File count: ' + str(num_files))
