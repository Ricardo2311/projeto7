import requests
preco_usuario = int(input('Digite o preço para alerta: '))
email_usuario = input('Digite o email para qual devo enviar o alerta: ')

api_link = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&ids=bitcoin&x_cg_demo_api_key=CG-Pr3ychdF3pSzZSkWPKk4ZUkE')
preco_atual_btc = api_link.json()[0]['current_price']


#