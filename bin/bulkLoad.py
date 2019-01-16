import os, sys, csv, string
import config as cfg
from function import getfirstline,filetoprocess

os.environ["SALESFORCE_INSTANCE"] = "login.salesforce.com"
os.environ["SALESFORCE_SANDBOX"] = "False"
os.environ["SALESFORCE_USERNAME"] = cfg.salesforceLogin['username']
os.environ["SALESFORCE_PASSWORD"] = cfg.salesforceLogin['password']
os.environ["SALESFORCE_SECURITY_TOKEN"] = cfg.salesforceLogin['token']

fileName = sys.argv[1]
SobjectConfig = sys.argv[2]

if SobjectConfig == 'relationshipConfig':
    SobjectConfig = 'Account'
elif SobjectConfig == 'contactConfig':
    SobjectConfig = 'Contact'
elif SobjectConfig == 'depositConfig':
    SobjectConfig = 'LLC_BI__Deposit__c'
else:
    SobjectConfig = 'not set'

print(SobjectConfig)

from salesforce_bulk_api import SalesforceBulkJob

job = SalesforceBulkJob('upsert', SobjectConfig, external_id_field='LLC_BI__lookupKey__c')

jobtorun = filetoprocess(fileName)

exec(jobtorun)

#delete file if successful
if sys.exit() == 0:
    os.remove(cfg.mockConfig['FILE_OUTPUT_PATH'] + fileName + '.csv ')