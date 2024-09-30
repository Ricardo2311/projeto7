import requests
from infos import EMAIL_PASSWORD, EMAIL_ADDRESS
import smtplib
from email.message import EmailMessage
import schedule
from time import sleep
preco_usuario = int(input('Digite o preço para alerta: '))
email_usuario = input('Digite o email para qual devo enviar o alerta: ')

def achar_preco_btc():
    api_link = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&ids=bitcoin&x_cg_demo_api_key=CG-Pr3ychdF3pSzZSkWPKk4ZUkE')
    preco_atual_btc = api_link.json()[0]['current_price']
    return preco_atual_btc

preco_btc = achar_preco_btc()

def enviar_email():
    mail = EmailMessage()
    mail['Subject'] = 'ALERTA!! Preço do BTC abaixo do solicitado!!!'
    mensagem = f'''
        Olá, o preço do BTC está R${preco_btc},00, abaixo do solicitado!!
    '''
    mail['From'] = EMAIL_ADDRESS
    mail['To'] = email_usuario
    mail.add_header('Content-Type','text/html')
    mail.set_payload(mensagem.encode('utf-8'))
    with smtplib.SMTP_SSL('smtp.gmail.com',465 ) as email:
        email.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        email.send_message(mail)
    print('Email enviado com sucesso!')

def verificar_precos():
    if preco_btc < preco_usuario:
        enviar_email()
    else:
        print('O preço do BTC está alto demais para enviar email!')
verificar_precos()
schedule.every(10).minutes.do(achar_preco_btc)
schedule.every(10).minutes.do(verificar_precos)

while True:
    schedule.run_pending()
    sleep(1)