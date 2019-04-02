import preprocessing

mockConfig = {
    'API_KEY': '5cbc25b0',
    'BASE_URL': 'https://api.mockaroo.com/api/',
    'ROW_COUNT': '10',  #5k is Max for API call
    'FILE_COUNT': 1,
    'GENERATE_TYPE': 'generate.csv',
    'FILE_OUTPUT_PATH': '/Users/richbateman/Python-DataLoad/',
    'SIGNIN_URL': 'https://mockaroo.com/users/sign_in',
    'DATASET_URL': 'https://mockaroo.com/lists/new',
    'USER_NAME': 'rich.bateman@ncino.com',
    'PASS_WORD': 'sgsb5572'
}

salesforceLogin = {
    'instance': 'test.login.com',
    'isSandbox': 'True',
    'username': 'chris.fernandez@qa.com.patch3',
    'password': 'C65ra79s',
    'token': 'mFEO9oFgI4JeulnGOM8wwKRjh',
    'client_id': 'Mockaroo-Load'
}

relationshipConfig = {
    'sobject': 'Account',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': 'Sobject_Account.schema.json'
}

contactConfig = {
    'sobject': 'Contact',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': 'Sobject_Contact.schema.json'
}

depositConfig = {
    'sobject': 'LLC_BI__Deposit__c',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': 'Sobject_LLC_BI__Deposit__c.schema.json'
}

legalEntitiesConfig = {
    'sobject': 'LLC_BI__Legal_Entities__c',
    'external_id_field': '',
    'bulkJobType': 'insert',
    'SCHEMA': 'Sobject_LLC_BI__Legal_Entities__c.schema.json'
}

loanConfig = {
    'sobject': 'LLC_BI__Loan__c',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': 'Sobject_LLC_BI__Loan__c.schema.json'
}
