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
    time.sleep(1)

  def click_button_register():
    driver.find_element_by_css_selector("#SubmitLogin").click()
    time.sleep(2)

  def preencher_email(email):
    driver.find_element_by_css_selector("#email").send_keys(email)

  def preencher_senha(senha):
    driver.find_element_by_css_selector("#passwd").send_keys(senha)

  def validar_nome_usuario():
    with open('fixtures/MassaDeDados/LoginPessoal.json') as f:
      data = json.load(f)

    nome_usuario = driver.find_element_by_css_selector("nav > div:nth-child(1) > a > span").text

    if nome_usuario != data['nome']:
      print(f'Usuário {nome_usuario} não coincide com {data["nome"]}')
      return

    else:
      print(f'Usuário: {nome_usuario} validado com sucesso')
