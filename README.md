Mockaroo project
===================
When running generate.py, follow the sequence below:

Load
<ol>
<li>relationshipConfig</li>
<li>contactConfig</li>
<li>depositConfig</li>
<li>loanConfig</li>
<li>legalEntitiesConfig</li>
</ol>

Configuration
===================
config.py


| Config        | Key           | Description  |
| :------------- |:-------------| :-----|
| mockConfig      | API_KEY | Key is obtained from Mockaroo account |
|      | BASE_URL      |   The default value will never change unless you are using Mock API feature |
|  | ROW_COUNT      |    Defines the record count for each file generated.  Max rows is 5,000 |
|  | FILE_COUNT      |    Define the number of files you want to generate.  ROW_COUNT * FILE_COUNT gives you overall records to load |
|  | GENERATE_TYPE      |    This should never change from default value of `generate.csv` |
|  | FILE_OUTPUT_PATH      |    Writable path to store files generated and results |
| salesforceLogin | instance      |    Value will be login.salesforce.com or test.salesforce.com |
|  | isSandbox      |    Indicates instance as a Sandbox <True,False> |
|  | username      |    Valid user of Salesforce instance |
|  | password      |    Valid password of Salesforce instance |
|  | token      |    Valid security token of Salesforce instance |
|  | client_id      |    Text to identify bulk job in Salesforce, default is fine. |
| relationshipConfig | sobject      |    The Salesforce API value |
|  | external_id_field      |    The field on the sobject set to the external id. |
|  | bulkJobType      |  The arguments to create the bulkjob are ('create', 'update', 'delete', 'upsert', 'insert')   |
|  | SCHEMA      |    Should always be ''  |
|  | FIELDS      |    The contents from Mockaroo exported schema |


Samples:

<pre><code>
mockConfig = {
    'API_KEY': '5cbc25b0',
    'BASE_URL': 'https://api.mockaroo.com/api/',
    'ROW_COUNT': '100',  #5k is Max for API call
    'FILE_COUNT': 2,
    'GENERATE_TYPE': 'generate.csv',
    'FILE_OUTPUT_PATH': '/Users/richbateman/Documents/Python-DataLoad/'
}
</code></pre>

<pre><code>
salesforceLogin = {
    'instance': 'test.salesforce.com',
    'isSandbox': 'True',
    'username': 'user@email.com',
    'password': 'password123',
    'token': '12345abcd',
    'client_id': 'Mockaroo-Load'
}
</code></pre>



How to run
===================

Run Generate.py.

Parameter:  <relationshipConfig|contactConfig|depositConfig|loanConfig|legalEntitiesConfig>

Example:

`
./python generate.py relationshipConfig
`