#!/usr/bin/env python
# coding=utf-8
import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def service_now():
    #### option of chrome
    options = webdriver.ChromeOptions()
    prefs = {"":""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    week = 2
    endTime = (datetime.datetime.now() + datetime.timedelta(days=(week*7))).strftime("%m-%d")

    url = "https://panasonic.service-now.com/nav_to.do?uri=%2Fchange_task_list.do%3Fsysparm_query%3Dassignment_group%3D13bd1cb30fbea1009045ee68b1050ed8%5EORassignment_group%3D783954cadb674300d1835200cf961931%5Eu_start_dateBETWEENjavascript:gs.beginningOfToday()@javascript:gs.dateGenerate(%272021-" + endTime + "%27,%2723:59:59%27)%26sysparm_first_row%3D1%26sysparm_view%3D"
    driver.implicitly_wait(10)
    driver.get(url)

    gID = input("ID: ")
    pw = "MoonZh" + input("pwNO. : ")
    username = "japan\\" + gID
    driver.find_element_by_id("userNameInput").send_keys(username)
    driver.find_element_by_id("passwordInput").send_keys(pw)
    driver.find_element_by_id("submitButton").click()

    driver.switch_to_frame("gsft_main")

    print("--------","EndTime: (" + str(week) + "weeks) " + endTime)

    menu = ActionChains(driver)
    menuLoc = driver.find_element_by_css_selector("#hdr_change_task > th:nth-child(5)")
    menu.context_click(menuLoc).send_keys(Keys.UP).send_keys(Keys.RIGHT).send_keys(Keys.ENTER).perform()
    time.sleep(5)
    
    dwload = ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(5)
    driver.quit()
    print("######  End of Download Today's REL  #######")

if __name__ == '__main__':
    service_now()
    