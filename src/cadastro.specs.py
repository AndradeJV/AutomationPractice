from Classes.Cadastro import Cadastro
import json
import time

with open('fixtures/MassaDeDados/CadastroUsuario.json') as f:
  data = json.load(f)


Cadastro.abrir_pagina()
Cadastro.click_button_sign_in()
Cadastro.preencher_email_cadastro(data['informacaoCadastro']['email'])
Cadastro.click_button_create_account()
Cadastro.click_checkbox_mr()
Cadastro.preencher_nome_informacao(data['informacaoCadastro']['primeiroNome'])
Cadastro.preencher_sobrenome_informacao(data['informacaoCadastro']['segundoNome'])
Cadastro.validar_email_inserido(data['informacaoCadastro']['email'])
Cadastro.preencher_senha(data['informacaoCadastro']['senha'])
Cadastro.preencher_data_nascimento(data['informacaoCadastro']['dataNascimento']['dia'], data['informacaoCadastro']['dataNascimento']['mes'], data['informacaoCadastro']['dataNascimento']['ano'])
Cadastro.preencher_nome_endereco(data['endereco']['primeiroNome'])
Cadastro.preencher_sobrenome_endereco(data['endereco']['segundoNome'])
Cadastro.preencher_empresa(data['endereco']['empresa'])
Cadastro.preencher_endereco(data['endereco']['address'])
Cadastro.preencher_cidade(data['endereco']['cidade'])
Cadastro.preencher_estado(data['endereco']['estado'])
Cadastro.preencher_codigo_postal(data['endereco']['codigoPostal'])
Cadastro.preencher_pais(data['endereco']['pais'])
Cadastro.preencher_telefone(data['endereco']['tel'])
Cadastro.preencher_celular(data['endereco']['cel'])
Cadastro.click_button_register()