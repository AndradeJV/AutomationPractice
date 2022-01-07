from selenium import webdriver

import json
import time


driver = webdriver.Chrome()


class Login():
  def abrir_pagina():
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()


  def click_login():
    driver.find_element_by_css_selector("div.header_user_info > a").click()
    time.sleep(1)