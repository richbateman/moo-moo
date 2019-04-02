import string,random,os,sys,csv,io,requests,json,collections,time
import config as cfg
from selenium import webdriver

#random generator
def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def getfirstline(fileName):
    with open(fileName, 'r') as f:
        first_line = f.readline()
    return first_line


def filetoprocess(fileName):
    r = ''
    newline = getfirstline(fileName).strip('\n')
    headerRecord = str('[' + newline + '],')

    with open(fileName, 'r') as f:
        next(f)
        recordOpenBracket = str('[')
        for line in f:
            r += str('(' + line + '),')
        recordCloseBracket = str(']')
    f.close()

    convertedfile = 'job.upload(' + headerRecord + recordOpenBracket + r + recordCloseBracket + ')'

    return convertedfile


def sForceAuth():
    os.environ["SALESFORCE_INSTANCE"] = cfg.salesforceLogin['instance']
    os.environ["SALESFORCE_SANDBOX"] = cfg.salesforceLogin['isSandbox']
    os.environ["SALESFORCE_USERNAME"] = cfg.salesforceLogin['username']
    os.environ["SALESFORCE_PASSWORD"] = cfg.salesforceLogin['password']
    os.environ["SALESFORCE_SECURITY_TOKEN"] = cfg.salesforceLogin['token']


def printCSVtoConsole(printfile):
    f = open(printfile)
    with f:
        reader = csv.reader(f)
        for row in reader:
            for e in row:
                print(e)
