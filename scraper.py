#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:46:20 2018

@author: deathrow77
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os

dir=os.path.dirname(__file__)
driver=webdriver.Firefox(executable_path=(dir+'/geckodriver'))
print("Firefox Instance Opened!! \n")
driver.get('https://www.facebook.com')
driver.implicitly_wait(5)
# Login to Facebook
email = driver.find_element_by_id('email')
# Enter your email here
email.send_keys(' ')
password=driver.find_element_by_id('pass')
# Enter your password here
password.send_keys(' ')
email.submit()
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Events")))
events=driver.find_element_by_link_text('Events')
events.click()
WebDriverWait(driver,10).until(expected_conditions.invisibility_of_element_located((By.XPATH, "//div[@class='_3ixn']")))
bds=driver.find_element_by_link_text('Birthdays')
bds.click()
elems=driver.find_element_by_id('birthdays_content')
dates=elems.find_elements_by_class_name("_tzh")
for date in dates:
    print(date.text)
    print("\n\n")



# Extract the date and name
