from Classes.Login import Login

import json
import time

# Instanciando massa de dados
with open('fixtures/MassaDeDados/LoginPessoal.json') as f:
  data = json.load(f)


Login.abrir_pagina()
Login.click_button_sign_in()
Login.preencher_email(data['email'])
Login.preencher_senha(data['senha'])
Login.click_button_register()
Login.resultado_sucesso()