from selenium import webdriver

import json
import time


driver = webdriver.Chrome()


class Login:
  def abrir_pagina():
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

  def click_button_sign_in():
    driver.find_element_by_css_selector("div.header_user_info > a").click()