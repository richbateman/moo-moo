import os, sys, csv, string
import config as cfg
from function import getfirstline,filetoprocess

csv.register_dialect('myDialect',
    delimiter = ',',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL)

os.environ["SALESFORCE_INSTANCE"] = cfg.salesforceLogin['instance']
os.environ["SALESFORCE_SANDBOX"] = cfg.salesforceLogin['isSandbox']
os.environ["SALESFORCE_USERNAME"] = cfg.salesforceLogin['username']
os.environ["SALESFORCE_PASSWORD"] = cfg.salesforceLogin['password']
os.environ["SALESFORCE_SECURITY_TOKEN"] = cfg.salesforceLogin['token']

fileName = sys.argv[1]
SobjectConfig = sys.argv[2]
func = getattr(cfg, SobjectConfig)

from salesforce_bulk_api import SalesforceBulkJob
job = SalesforceBulkJob(func['bulkJobType'], func['sobject'], external_id_field=func['external_id_field'])
jobtorun = filetoprocess(fileName)
exec(jobtorun)

#create and save result file to be used in downstream calls
theResult = list(job.results())
with open(fileName + '.result', 'w') as myfile:
    wr = csv.writer(myfile, dialect='myDialect')
    wr.writerow(theResult)
