import os
import config as cfg

os.environ["SALESFORCE_INSTANCE"] = "login.salesforce.com"
os.environ["SALESFORCE_SANDBOX"] = "False"
os.environ["SALESFORCE_USERNAME"] = cfg.salesforceLogin['username']
os.environ["SALESFORCE_PASSWORD"] = cfg.salesforceLogin['password']
os.environ["SALESFORCE_SECURITY_TOKEN"] = cfg.salesforceLogin['token']

from salesforce_bulk_api import SalesforceBulkJob

job = SalesforceBulkJob('upsert', 'Account', external_id_field='LLC_BI__lookupKey__c')
job.upload(
    ['Name', 'LLC_BI__Active__c', 'LLC_BI__lookupKey__c', 'Type', 'LLC_BI__Tax_Identification_Number__c',
     'LLC_BI__Employee_Relationship__c', 'LLC_BI__Reg_O_Relationship__c', 'Industry', 'Phone', 'LLC_BI__Status__c',
     'LLC_BI__Review_Status__c', 'LLC_BI__Partnership_Type__c', 'Rating', 'Ownership', 'LLC_BI__CustomerPriority__c',
     'LLC_BI__UpsellOpportunity__c', 'LLC_BI__SLA__c', 'LLC_BI__SLASerialNumber__c', 'AccountSource',
     'LLC_BI__Account_Review__c', 'LLC_BI__ActionFlag__c', 'LLC_BI__Automated_Financials__c', 'LLC_BI__Facility__c',
     'AccountNumber', 'NaicsCode', 'NaicsDesc', 'LLC_BI__Pod__c', 'LLC_BI__Region__c', 'LLC_BI__Review_Frequency__c'],
    [
        ('Fedora Twist2', 'Yes', '3434', 'Sole Proprietorship', '264-57-1847', 'false', 'true', 'Agriculture', '47(244)840-9207', 'None', 'In Review', '', 'Hot', 'Other', 'Medium', 'Maybe', 'Gold', 'BX-119-d', 'Word of mouth', 'Managed directional archive', 'Yes', 'true', 'Leased', 'GY-544-h', '111110', ' Soybean farming, field and seed production ', 'Cypress', 'South', 'Semi-Annually'),
        ('Fedora Twist3', 'Yes', '34343434', 'Sole Proprietorship',
         '264-57-1847', 'false', 'true', 'Agriculture', '47(244)840-9207', 'None', 'In Review', '', 'Hot', 'Other',
         'Medium', 'Maybe', 'Gold', 'BX-119-d', 'Word of mouth', 'Managed directional archive', 'Yes', 'true', 'Leased',
         'GY-544-h', '111110', ' Soybean farming, field and seed production ', 'Cypress', 'South', 'Semi-Annually')
    ]

)
