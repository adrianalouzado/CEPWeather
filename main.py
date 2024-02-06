import requests
import json

cep = input('Digite o cep: ')

dados = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

dadosaux = json.loads(dados.text)

parametros = {
    'access_key' : '6204ca3f799a0caa84e6562c4379dd44', 
    'query' : dadosaux.get('localidade')  
}

dados = requests.get('http://api.weatherstack.com/current',parametros)
print(dados.text)
