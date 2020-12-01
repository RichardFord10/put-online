from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from getpass import getpass
import pandas as pd
import sys
import csv
import os

# configure webdriver & headless chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options = chrome_options, executable_path=r'C:/Users/rford/Desktop/chromedriver/chromedriver.exe')

# current day format
currentDate = datetime.today().strftime('%Y-%m-%d')

#login function
def login(user, pword = str):
    driver.get("https://######.com/manager")
    Username = driver.find_element_by_id("bvuser")
    Password = driver.find_element_by_id("bvpass")
    Login = driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/input')
    Username.send_keys(user)
    Password.send_keys(pword)
    Login.click()
    print("Logging In...")
 
   
#item ids
item_ids = [
'14644',
'233269',
'5008',
'6209',
'6287',
'6288',
'9154',
'12509',
'13995',
'18807',
'19928',
'26265',
'29655',
'220267',
'220269',
'223737',
'229358',
'231103',
'231105',
'231285',
'231299',
]

def turn_online():
    for item_id in item_ids:
            WebDriverWait(driver, 1)  
            #Navigate to item    
            driver.get("https://www.######.com/manager/entry.php?area=general&id={}".format(item_id))
            WebDriverWait(driver, 10)
            try:
                #Click 'Yes' on 'Are you sure you want to continue' view
                driver.find_element_by_css_selector('#form1 > div > input[type=submit]:nth-child(2)').click()
                WebDriverWait(driver, 5)
            except NoSuchElementException:
                pass
            #Get Name
            WebDriverWait(driver, 5)  
            name = driver.find_element_by_xpath('//*[@id="form1"]/div/table/tbody/tr[1]/td[1]/textarea').text
            #get check box inputs
            is_sold_online = driver.find_element_by_xpath('//*[@id="4"]')
            is_sellable = driver.find_element_by_xpath('//*[@id="5"]')
            save = driver.find_element_by_xpath('//*[@id="form1"]/div/input[6]')
            #check box if box is not checked
            if is_sold_online.is_selected():
                pass
            else:
                is_sold_online.click()
            if is_sellable.is_selected():
                pass
            else:
                is_sellable.click()
            save.click()
            print(name + ' has been put online')
    print('All Items have been put back online!')


#Run
login(input("Enter Username: "), getpass("Enter Password: "))
turn_online()
 