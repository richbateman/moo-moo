#authenticate to target salesforce org

import config as cfg

from simple_salesforce import Salesforce
sf = Salesforce(cfg.salesforceLogin['username'], cfg.salesforceLogin['password'], cfg.salesforceLogin['token'], cfg.salesforceLogin['client_id'], cfg.salesforceLogin['domain'])
print(sf.query("SELECT Id, Email FROM Contact"))
