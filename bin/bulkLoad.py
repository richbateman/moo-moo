import os, sys, csv, string, io
import config as cfg
from function import *

csv.register_dialect('myDialect',
    delimiter = '\n',
    quotechar='',
    quoting=csv.QUOTE_NONE)

#Perform Salesforce authentication
sForceAuth()

fileName = sys.argv[1]
SobjectConfig = sys.argv[2]
func = getattr(cfg, SobjectConfig)

from salesforce_bulk_api import SalesforceBulkJob
job = SalesforceBulkJob(func['bulkJobType'], func['sobject'], external_id_field=func['external_id_field'])
jobtorun = filetoprocess(fileName)
exec(jobtorun)

#create and save result file to be used as a DATASET in Modckaroo.
#The dataset contains Salesforce IDs that were created during the bulk load job
theResult = list(job.results())
with io.open(fileName + '.dataset', 'w', encoding='utf8') as f:
    #f.write(theResult)
    wr = csv.writer(f, dialect='myDialect')
    wr.writerow(theResult)

with io.open(fileName + '.dataset', 'r', encoding='utf8') as read:
    text = read.read().replace('(','').replace(')','').replace("'","").replace('False,','False')
# process Unicode text
with io.open(fileName + '.dataset', 'w', encoding='utf8') as final:
    final.write(text)