from coinmarketcapapi import CoinMarketCapAPI
import requests
import json
import re


def moeda(token):
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cmc = CoinMarketCapAPI('2880d47b-a189-45a2-8960-438edc0066fd')
    r = cmc.cryptocurrency_info(symbol=f'{token}')

    data = r.data
    data = data[token]
    n1 = data['description'].index('The')
    n2 = data['description'].index('s.')
    n3 = data['description'][n1:n2 + 2]

    usd = float(cotacoes['USDBRL']['bid'])
    valor_brl = float(re.sub("[^0-9.]", "", n3[:58])) * usd
    down_up = float(re.sub("[^0-9.-]", "", n3[60:80]))
    sobe_ou_desce = None
    if down_up > 1:
        sobe_ou_desce = 'subiu'
    else:
        sobe_ou_desce = 'caiu'

    return f'O último preço conhecido do token {token} é R${valor_brl:.2f} e {sobe_ou_desce} {down_up}% nas últimas 24 horas.'

