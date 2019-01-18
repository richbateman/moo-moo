#config.py
import preprocessing


mockConfig = {
    'API_KEY': '5cbc25b0',
    'BASE_URL': 'https://api.mockaroo.com/api/',
    'ROW_COUNT': '100',  #5k is Max for API call
    'FILE_COUNT': 2,
    'GENERATE_TYPE': 'generate.csv',
    'FILE_OUTPUT_PATH': '/Users/richbateman/Documents/Python-DataLoad/'
}

salesforceLogin = {
    'instance': 'test.login.com',
    'isSandbox': 'True',
    'username': 'chris.fernandez@qa.com.patch3',
    'password': 'C65ra79s',
    'token': 'mFEO9oFgI4JeulnGOM8wwKRjh',
    'client_id': 'Mockaroo-Load',
    'domain': 'login'
}

relationshipConfig = {
    'sobject': 'Account',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': '',
    'FIELDS': '''[
    {
      "name": "Name",
      "null_percentage": 0,
      "type": "Full Name",
      "formula": ""
    },
    {
      "name": "LLC_BI__Active__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Yes",
        "No"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "Account.LLC_BI__lookupKey__c",
      "column": "LLC_BI__Account__c",
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "Type",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Sole Proprietorship ",
        "Partnership ",
        "Corporation ",
        "Government ",
        "Trust ",
        "Association ",
        "Limited Liability Company ",
        "Individual"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Tax_Identification_Number__c",
      "null_percentage": 0,
      "type": "SSN",
      "formula": ""
    },
    {
      "name": "LLC_BI__Employee_Relationship__c",
      "null_percentage": 0,
      "type": "Boolean",
      "formula": ""
    },
    {
      "name": "LLC_BI__Reg_O_Relationship__c",
      "null_percentage": 0,
      "type": "Boolean",
      "formula": ""
    },
    {
      "name": "Industry",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Agriculture",
        "Apparel ",
        "Banking ",
        "Biotechnology ",
        "Chemicals ",
        "Communication ",
        "Construction ",
        "Consulting ",
        "Eductation ",
        "Electronics ",
        "Energy ",
        "Engineering ",
        "Entertainment ",
        "Environment ",
        "Finance ",
        "Food & Beverage ",
        "Government ",
        "Healthcare ",
        "Hospitality ",
        "Insurance ",
        "Machinery ",
        "Manufacturing ",
        "Media ",
        "Not for Profit ",
        "Other ",
        "Recreation ",
        "Retail ",
        "Shipping ",
        "Technology ",
        "Telecommunications ",
        "Transportation ",
        "Utilities"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": "if field('Type') == 'Individual' then nil else this end"
    },
    {
      "name": "Phone",
      "null_percentage": 0,
      "type": "Phone",
      "format": "(###) ###-####",
      "formula": ""
    },
    {
      "name": "LLC_BI__Status__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Prospect ",
        "Customer ",
        "None ",
        "Referral Source"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Review_Status__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "In Review",
        "Complete"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": "if field('LLC_BI__Active__c') == 'Yes' then this else nil end"
    },
    {
      "name": "LLC_BI__Partnership_Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "General Partnership ",
        "Limited Partnership ",
        "Limited Liability Partnership"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": "if field('Type') == 'Partnership' then this else nil end"
    },
    {
      "name": "Rating",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Hot ",
        "Warm ",
        "Cold"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "Ownership",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Public ",
        "Private ",
        "Subsidiary ",
        "Other"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__CustomerPriority__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "High",
        "Low",
        "Medium"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__UpsellOpportunity__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Maybe",
        "No",
        "Yes"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__SLA__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Platinum ",
        "Gold ",
        "Silver ",
        "Bronze"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__SLASerialNumber__c",
      "null_percentage": 0,
      "type": "Regular Expression",
      "value": "[:upper:]{2}-\\\\d{3}-[:lower:]{1}",
      "formula": "if field('LLC_BI__SLA__c') == nil then nil else this end"
    },
    {
      "name": "AccountSource",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Advertisement ",
        "Employee Referral ",
        "External Referral ",
        "Partner ",
        "Public Relations ",
        "Seminar - Internal ",
        "Seminar - Partner ",
        "Trade Show ",
        "Web ",
        "Word of mouth ",
        "Other"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Account_Review__c",
      "null_percentage": 0,
      "type": "Catch Phrase",
      "formula": ""
    },
    {
      "name": "LLC_BI__ActionFlag__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Yes",
        "No"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Automated_Financials__c",
      "null_percentage": 0,
      "type": "Boolean",
      "formula": ""
    },
    {
      "name": "LLC_BI__Facility__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Owned",
        "Leased"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "AccountNumber",
      "null_percentage": 0,
      "type": "Regular Expression",
      "value": "[:upper:]{2}-\\\\d{3}-[:lower:]{1}",
      "formula": ""
    },
    {
      "name": "LLC_BI__Naics_Code__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "NaicsCodeDescript",
      "column": "NAICS12",
      "selectionStyle": "sequential",
      "formula": "if field('Type') == 'Individual' then nil else this end"
    },
    {
      "name": "LLC_BI__NaicsDesc__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "NaicsCodeDescript",
      "column": " INDEX ITEM DESCRIPTION ",
      "selectionStyle": null,
      "formula": "if field('Type') == 'Individual' then nil else this end"
    },
    {
      "name": "LLC_BI__Pod__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Dogwood",
        "Cypress"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Region__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "North",
        "East",
        "South",
        "West"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Review_Frequency__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Annually",
        "Semi-Annually",
        "Quarterly",
        "Every 2 Months",
        "Monthly"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    }
  ]'''
}

contactConfig = {
    'sobject': 'Contact',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': '',
    'FIELDS': '''[
    {
      "name": "Account.LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "Account.LLC_BI__lookupKey__c",
      "column": null,
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "Birthdate",
      "null_percentage": 0,
      "type": "Formula",
      "value": "random(now()+days(-9125), now()+days(-15000))",
      "formula": ""
    },
    {
      "name": "Email",
      "null_percentage": 0,
      "type": "Email Address",
      "formula": "this.gsub(/\\\\.([\\\\w]+)$/, '.\\\\\\\\1.fake')"
    },
    {
      "name": "MobilePhone",
      "null_percentage": 5,
      "type": "Phone",
      "format": "#-(###)###-####",
      "formula": ""
    },
    {
      "name": "FirstName",
      "null_percentage": 0,
      "type": "First Name",
      "formula": ""
    },
    {
      "name": "LastName",
      "null_percentage": 0,
      "type": "Last Name",
      "formula": ""
    },
    {
      "name": "Phone",
      "null_percentage": 5,
      "type": "Phone",
      "format": "#-(###)###-####",
      "formula": ""
    },
    {
      "name": "LLC_BI__Drivers_License__c",
      "null_percentage": 5,
      "type": "Regular Expression",
      "value": "\\\\d{7}",
      "formula": ""
    },
    {
      "name": "LLC_BI__Employer_Name__c",
      "null_percentage": 34,
      "type": "Company Name",
      "formula": ""
    },
    {
      "name": "LLC_BI__Gender__c",
      "null_percentage": 34,
      "type": "Custom List",
      "values": [
        "Female",
        "Male",
        "Not Disclosed"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Home_City__c",
      "null_percentage": 0,
      "type": "City",
      "formula": ""
    },
    {
      "name": "LLC_BI__Home_State__c",
      "null_percentage": 0,
      "type": "State (abbrev)",
      "onlyUSPlaces": true,
      "formula": ""
    },
    {
      "name": "LLC_BI__Home_Address__c",
      "null_percentage": 0,
      "type": "Street Address",
      "formula": ""
    },
    {
      "name": "LLC_BI__Home_Zipcode__c",
      "null_percentage": 0,
      "type": "Postal Code",
      "formula": ""
    },
    {
      "name": "LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "LLC_BI__Contact__c.LLC_BI__lookupKey__c",
      "column": null,
      "selectionStyle": "random",
      "formula": ""
    },
    {
      "name": "LLC_BI__SS__c",
      "null_percentage": 0,
      "type": "SSN",
      "formula": ""
    },
    {
      "name": "LLC_BI__Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Primary",
        "Professional Contact",
        "Referral Source",
        "Other"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    }
  ]'''
}

depositConfig = {
    'sobject': 'LLC_BI__Deposit__c',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': '',
    'FIELDS': '''[
    {
      "name": "LLC_BI__Account__r.LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "Account.LLC_BI__lookupKey__c",
      "column": "Name",
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "LLC_BI__Amount__c",
      "null_percentage": 0,
      "type": "Money",
      "min": 200,
      "max": 5000,
      "symbol": "none",
      "formula": ""
    },
    {
      "name": "LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "LLC_BI__Deposit__c.LLC_BI__lookupKey__c",
      "column": "Name",
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "Name",
      "null_percentage": 0,
      "type": "Fake Company Name",
      "formula": ""
    },
    {
      "name": "LLC_BI__Product_Line__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Deposit"
      ],
      "selectionStyle": "sequential",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Product_Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Business Banking"
      ],
      "selectionStyle": "sequential",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Product__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Business Checking"
      ],
      "selectionStyle": "sequential",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Interest_Rate__c",
      "null_percentage": 0,
      "type": "Number",
      "min": 1,
      "max": 24,
      "decimals": 3,
      "formula": ""
    },
    {
      "name": "LLC_BI__Initial_Deposit__c",
      "null_percentage": 0,
      "type": "Money",
      "min": 100,
      "max": 3000,
      "symbol": "none",
      "formula": ""
    },
    {
      "name": "LLC_BI__Stage__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Qualification",
        "Signature Signed",
        "Active"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Status__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Open",
        "Active",
        "Closed",
        "Dormant"
      ],
      "selectionStyle": "random",
      "distribution": [
        {
          "rule": "field(\\\"LLC_BI__Stage__c\\\") == \\\"Qualification\\\"",
          "frequencies": {
            "Open": 1,
            "Active": 1,
            "Closed": 1,
            "Dormant": 1
          }
        },
        {
          "rule": "field(\\\"LLC_BI__Stage__c\\\") == \\\"Signature Signed\\\"",
          "frequencies": {
            "Open": 1,
            "Active": 1,
            "Closed": 1,
            "Dormant": 1
          }
        },
        {
          "rule": "field(\\\"LLC_BI__Stage__c\\\") == \\\"Active\\\"",
          "frequencies": {
            "Open": 1,
            "Active": 1,
            "Closed": 1,
            "Dormant": 1
          }
        }
      ],
      "formula": ""
    },
    {
      "name": "LLC_BI__Open_Date__c",
      "null_percentage": 0,
      "type": "Formula",
      "value": "random(now()+days(-42)+year(-2), now()+days(-3))",
      "formula": ""
    },
    {
      "name": "LLC_BI__Annual_Rent_Amount__c",
      "null_percentage": 0,
      "type": "Number",
      "min": 1,
      "max": 16,
      "decimals": 2,
      "formula": ""
    },
    {
      "name": "LLC_BI__APY__c",
      "null_percentage": 0,
      "type": "Number",
      "min": 1,
      "max": 14,
      "decimals": 4,
      "formula": ""
    },
    {
      "name": "LLC_BI__Billing_Frequency__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Monthly",
        "Quarterly",
        "Semiannually",
        "Annually",
        "Biannually",
        "Monthly on the lease date anniversary",
        "Yearly on the lease date anniversary",
        "Other"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Billing_Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Give Notice",
        "Debit Account"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    }
  ]'''
}

legalEntitiesConfig = {
    'sobject': 'LLC_BI__Legal_Entities__c',
    'external_id_field': '',
    'bulkJobType': 'insert',
    'SCHEMA': '',
    'FIELDS': '''[
    {
      "name": "LLC_BI__Account__r.LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "Account.LLC_BI__lookupKey__c",
      "column": null,
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "LLC_BI__Loan__r.LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "LLC_BI__Loan__c.LLC_BI__lookupKey__c",
      "column": "Name",
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "LLC_BI__Deposit__r.LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "LLC_BI__Deposit__c.LLC_BI__lookupKey__c",
      "column": "Name",
      "selectionStyle": "sequential",
      "formula": "if this == 'LLC_BI__lookupKey__c' then random(1,50) else this end"
    },
    {
      "name": "LLC_BI__Borrower_Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Borrower ",
        "Guarantor ",
        "Limited Guarantor ",
        "Co-Borrower ",
        "Related Entity"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Relationship_Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Primary Owner ",
        "Secondary Owner ",
        "Joint Owner"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Ownership__c",
      "null_percentage": 0,
      "type": "Number",
      "min": 50,
      "max": 100,
      "decimals": 0,
      "formula": ""
    }
  ]'''
}

loanConfig = {
    'sobject': 'LLC_BI__Loan__c',
    'external_id_field': 'LLC_BI__lookupKey__c',
    'bulkJobType': 'upsert',
    'SCHEMA': '',
    'FIELDS': '''[
    {
      "name": "LLC_BI__Account__r.LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "Account.LLC_BI__lookupKey__c",
      "column": null,
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "LLC_BI__lookupKey__c",
      "null_percentage": 0,
      "type": "Dataset Column",
      "dataset": "LLC_BI__Loan__c.LLC_BI__lookupKey__c",
      "column": "Name",
      "selectionStyle": "sequential",
      "formula": ""
    },
    {
      "name": "LLC_BI__Accrued_Interest__c",
      "null_percentage": 0,
      "type": "Money",
      "min": 0,
      "max": 1000,
      "symbol": "none",
      "formula": ""
    },
    {
      "name": "LLC_BI__Amount__c",
      "null_percentage": 0,
      "type": "Money",
      "min": 1000,
      "max": 450000,
      "symbol": "none",
      "formula": ""
    },
    {
      "name": "LLC_BI__Description__c",
      "null_percentage": 0,
      "type": "Catch Phrase",
      "formula": ""
    },
    {
      "name": "LLC_BI__InterestRate__c",
      "null_percentage": 0,
      "type": "Number",
      "min": 1,
      "max": 24,
      "decimals": 3,
      "formula": ""
    },
    {
      "name": "LLC_BI__Last_Pay_Date__c",
      "null_percentage": 0,
      "type": "Formula",
      "value": "random(now()+days(-23), now()+days(-13))",
      "formula": ""
    },
    {
      "name": "Name",
      "null_percentage": 0,
      "type": "Catch Phrase",
      "formula": "this + \\\"-Loan\\\""
    },
    {
      "name": "LLC_BI__Monthly_Payment__c",
      "null_percentage": 0,
      "type": "Money",
      "min": 100,
      "max": 1000,
      "symbol": "none",
      "formula": ""
    },
    {
      "name": "LLC_BI__Next_Payment_Due__c",
      "null_percentage": 0,
      "type": "Formula",
      "value": "random(now()+days(+23), now()+days(+13))",
      "formula": ""
    },
    {
      "name": "LLC_BI__Principal_Balance__c",
      "null_percentage": 0,
      "type": "Formula",
      "value": "field(\\\"LLC_BI__Amount__c\\\").to_f - (field(\\\"LLC_BI__Monthly_Payment__c\\\").to_f * random(1,2))",
      "formula": ""
    },
    {
      "name": "LLC_BI__Product_Line__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Commercial"
      ],
      "selectionStyle": "sequential",
      "distribution": [
        {
          "frequencies": {
            "PL1": "1",
            "Commercial": "2"
          }
        }
      ],
      "formula": ""
    },
    {
      "name": "LLC_BI__Product_Type__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Real Estate"
      ],
      "selectionStyle": "sequential",
      "distribution": [
        {
          "rule": "field(\\\"LLC_BI__Product_Line__c\\\") == \\\"Commercial\\\"",
          "frequencies": {
            "PT1": 1,
            "Real Estate": "2"
          }
        }
      ],
      "formula": ""
    },
    {
      "name": "LLC_BI__Product__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Construction"
      ],
      "selectionStyle": "sequential",
      "distribution": [
        {
          "rule": "field(\\\"LLC_BI__Product_Line__c\\\") == \\\"Commercial\\\"",
          "frequencies": {
            "P1": 1,
            "Construction": "2"
          }
        },
        {
          "rule": "field(\\\"LLC_BI__Product_Type__c\\\") == \\\"Real Estate\\\"",
          "frequencies": {
            "P1": 1,
            "Construction": "2"
          }
        }
      ],
      "formula": ""
    },
    {
      "name": "LLC_BI__Risk_Grade__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Stage__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Qualification ",
        "Proposal ",
        "Credit Underwriting  ",
        "Processing ",
        "Doc Prep ",
        "Doc Review ",
        "Closing ",
        "Compliance ",
        "Booked",
        "Complete"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Status__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Open ",
        "Hold ",
        "Lost ",
        "Declined ",
        "Charge-Off ",
        "Paid Out ",
        "Withdrawn"
      ],
      "selectionStyle": "custom",
      "distribution": [
        {
          "rule": "field(\\\"Stage\\\") == \\\"Qualification\\\"",
          "frequencies": {
            "Open": "1",
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Proposal\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Credit Underwriting\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Processing\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Doc Prep\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Doc Review\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Closing\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Compliance\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": "0",
            "Paid Out": "0",
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Booked\\\"",
          "frequencies": {
            "Open": 1,
            "Hold": "0",
            "Lost": "0",
            "Declined": "0",
            "Charge-Off": 1,
            "Paid Out": 1,
            "Withdrawn": 1
          }
        },
        {
          "rule": "field(\\\"Stage\\\") == \\\"Complete\\\"",
          "frequencies": {
            "Open": "0",
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": 1,
            "Paid Out": 1,
            "Withdrawn": 1
          }
        },
        {
          "frequencies": {
            "Open": 1,
            "Hold": 1,
            "Lost": 1,
            "Declined": 1,
            "Charge-Off": 1,
            "Paid Out": 1,
            "Withdrawn": 1
          }
        }
      ],
      "formula": ""
    },
    {
      "name": "LLC_BI__Pricing_Basis__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Variable",
        "Fixed"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Index__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Prime ",
        "Libor ",
        "Treasury Constant Maturity - 10 Year + ",
        "Treasury Constant Maturity - 5 Year +"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Payment_Schedule__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Weekly ",
        "Bi-Weekly ",
        "Semi-Monthly ",
        "Monthly ",
        "Bi-Monthly ",
        "Quarterly ",
        "Semi-Annual ",
        "Annual"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__LeadSource__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Broker ",
        "Industry Professional ",
        "Trade Show ",
        "Magazine ",
        "Employee Referral ",
        "Current Customer ",
        "Association ",
        "Email Campaign ",
        "Prior Origination ",
        "Direct Call ",
        "Wholesaler ",
        "Other"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    },
    {
      "name": "LLC_BI__Legal_Firm__c",
      "null_percentage": 0,
      "type": "Custom List",
      "values": [
        "Williams & Hayes",
        "PLLC ",
        "Raubenheimer & Partners ",
        "Rivenbark & Associates ",
        "Rhine Law Firm",
        "P.C. ",
        "Greg Jones Law"
      ],
      "selectionStyle": "random",
      "distribution": null,
      "formula": ""
    } 
  ]'''
}
