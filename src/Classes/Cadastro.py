from selenium import webdriver
import json
import time


driver = webdriver.Chrome()


class Cadastro:
  def abrir_pagina():
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

  def click_button_sign_in():
    driver.find_element_by_css_selector("div.header_user_info > a").click()
    time.sleep(3)

  def click_button_create_account():
    driver.find_element_by_css_selector("#SubmitCreate").click()
    time.sleep(3)

  def click_button_register():
    driver.find_element_by_css_selector("#submitAccount").click()

  def click_checkbox_mr():
    time.sleep(10)
    driver.find_element_by_css_selector("#id_gender1").click()
    time.sleep(1)

  def preencher_email_cadastro(email):
    driver.find_element_by_css_selector("#email_create").send_keys(email)
    time.sleep(1)
  def preencher_nome_informacao(nome):
    driver.find_element_by_css_selector("#customer_firstname").send_keys(nome)
    time.sleep(1)

  def preencher_sobrenome_informacao(sobrenome):
    driver.find_element_by_css_selector("#customer_lastname").send_keys(sobrenome)
    time.sleep(1)

  def validar_email_inserido(email):
    email_inserido = driver.find_element_by_css_selector("#email").text

    if email_inserido != email:
      return
  
    time.sleep(1)

  def preencher_senha(senha):
    driver.find_element_by_css_selector("#passwd").send_keys(senha)

  def preencher_data_nascimento(dia, mes, ano):
    time.sleep(1)
    driver.find_element_by_css_selector("#days").send_keys(dia)
    driver.find_element_by_css_selector("#months").send_keys(mes)
    driver.find_element_by_css_selector("#years").send_keys(ano)
    time.sleep(1)

  def preencher_nome_endereco(nome):
    driver.find_element_by_css_selector("#firstname").send_keys(nome)
    time.sleep(1)
  
  def preencher_sobrenome_endereco(sobrenome):
    driver.find_element_by_css_selector("#lastname").send_keys(sobrenome)
    time.sleep(1)

  def preencher_empresa(empresa):
    driver.find_element_by_css_selector("#company").send_keys(empresa)
    time.sleep(1)

  def preencher_endereco(endereco):
    driver.find_element_by_css_selector("#address1").send_keys(endereco)
    time.sleep(1)

  def preencher_cidade(cidade):
    driver.find_element_by_css_selector("#city").send_keys(cidade)
    time.sleep(1)

  def preencher_estado(estado):
    driver.find_element_by_css_selector("#id_state").send_keys(estado)
    time.sleep(1)

  def preencher_codigo_postal(codigo_postal):
    driver.find_element_by_css_selector("#postcode").send_keys(codigo_postal)
    time.sleep(1)

  def preencher_pais(pais):
    driver.find_element_by_css_selector("#id_country").send_keys(pais)
    time.sleep(1)

  def preencher_telefone(telefone):
    driver.find_element_by_css_selector("#phone").send_keys(telefone)
    time.sleep(1)

  def preencher_celular(celular):
    driver.find_element_by_css_selector("#phone_mobile").send_keys(celular)
    time.sleep(1)