#ScriptName : Login.py
#---------------------
import time
from function import id_generator
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://mockaroo.com/users/sign_in"
username = "rich.bateman@ncino.com"
password = "sgsb5572"
fileName = id_generator()

dataSetUrl = "https://mockaroo.com/lists/new"

xpaths = { 'usernameTxtBox': "//*[@id='user_email']",
           'passwordTxtBox': "//*[@id='user_password']",
           'submitButton':   "/html/body/div[3]/div/div[2]/form/div[4]/div/input",
           'dataSetFileName': "//*[@id='list_name']",
           'uploadDataSetInput': "//*[@id='new_list']/div[2]/div/div[1]/input"
}

cssSelector = {'uploadDataSetButton': "input.btn",
               'uploadDataSetInputButton': "#new_list > div:nth-child(5) > div > div.bootstrap-filestyle.input-group > span > label"
               }

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

#Navigate to Dataset Upload page
mydriver.get(dataSetUrl)

#Write DataSet Filename TextBox
mydriver.find_element_by_xpath(xpaths['dataSetFileName']).send_keys(fileName)

#Set DataSet Filen to upload
element = mydriver.find_element_by_css_selector(cssSelector['uploadDataSetInputButton']).click()
time.sleep(5)
# element.send_keys("/Users/richbateman/Python-DataLoad/38YHNIDA8JGE.csv.result")
# time.sleep(5)
# mydriver.find_element_by_css_selector(cssSelector['uploadDataSetButton']).click()


# condition = EC.visibility_of_element_located((By.CSS,
#     "label[for='location_p'] + div ul.location-list > li"))
#
# first_option = WebDriverWait(driver, 15).until(condition)
#
# first_option.click()