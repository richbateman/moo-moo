#authenticate to target salesforce org
import os
import config as cfg

def auth():
    from simple_salesforce import Salesforce
    sf = Salesforce(cfg.salesforceLogin['username'], cfg.salesforceLogin['password'], cfg.salesforceLogin['token'], cfg.salesforceLogin['client_id'], cfg.salesforceLogin['domain'])
    return sf

def bulkAuth():
    os.environ["SALESFORCE_INSTANCE"] = "login.salesforce.com"
    os.environ["SALESFORCE_SANDBOX"] = "False"
    os.environ["SALESFORCE_USERNAME"] = cfg.salesforceLogin['username']
    os.environ["SALESFORCE_PASSWORD"] = cfg.salesforceLogin['password']
    os.environ["SALESFORCE_SECURITY_TOKEN"] = cfg.salesforceLogin['token']
