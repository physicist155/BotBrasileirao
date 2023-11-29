##versão v.1.1
import os
import tweepy
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Configuração do Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('.github/workflows/fill_json.py')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bot-brasileirao-default-rtdb.firebaseio.com/'
    })
def cria_json_firebase():
  file = open("file.json","w")
  file.write('{\n')

  file.write('"type": "service_account"')
  file.write(',\n')

  file.write('"project_id": "bot-brasileirao"')
  file.write(',\n')

  file.write('"private_key_id": "%s"'%(os.getenv("PRIVATE_KEY_ID")))
  file.write(',\n')

  file.write('client_email": "%s"'%(os.getenv("CLIENT_EMAIL")))
  file.write(',\n')

  file.write('"client_id": "%s"'%(os.getenv("CLIENT_ID")))
  file.write(',\n')

  file.write('"auth_uri": "%s"'%(os.getenv("AUTH_URI")))
  file.write(',\n')

  file.write('token_uri": "%s"'%(os.getenv("TOKEN_URI")))
  file.write(',\n')

  file.write('"auth_provider_x509_cert_url": "%s"'%(os.getenv("AUTH_PROVIDER_X500_CERT_URL")))
  file.write(',\n')

  file.write('"client_x509_cert_url": "%s"'%(os.getenv("CLIENT_X509_CERT_URL")))
  file.write(',\n')

  file.write('"universe_domain": "%s"'%(os.getenv("UNIVERSE_DOMAIN")))
  file.write(',\n')


  file.write('}\n')
  file.close()

def get_previous_scores():
    ref = db.reference('placares_anteriores')
    return ref.get() or {}

def save_current_scores(scores):
    ref = db.reference('placares_anteriores')
    ref.set(scores)

url = 'https://www.placardefutebol.com.br/brasileirao-serie-a'
response = requests.get(url)

if response.status_code != 200:
    print("Falha ao acessar o site, status code:", response.status_code)
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
jogos = soup.find_all('div', class_='match__md_card')

placares_anteriores = get_previous_scores()
placares_atualizados = {}

for jogo in jogos:
    time_casa = jogo.find('div', class_='match__md_card--ht-name text').text.strip()
    time_visitante = jogo.find('div', class_='match__md_card--at-name text').text.strip()
    placar_elemento = jogo.find('div', class_='match__md_card--scoreboard')
    info_elemento = jogo.find('div', class_='match__md_card--info')

    placar = placar_elemento.text.strip() if placar_elemento else 'Placar não disponível'
    minuto_gol = jogo.find('div', class_='match__md_card--live-minute').text.strip() if jogo.find('div', class_='match__md_card--live-minute') else 'Minuto desconhecido'

    if 'match__md_card--live' in str(info_elemento):
        jogo_id = f"{time_casa} vs {time_visitante}"
        if jogo_id in placares_anteriores and placares_anteriores[jogo_id] != placar:
            post_tweet(f"Gol no jogo {jogo_id} no {minuto_gol}. Novo placar: {placar}")
            gols_time_casa, gols_visitante = map(int, placar.split(' - '))
            gols_anteriores_time_casa, gols_anteriores_visitante = map(int, placares_anteriores[jogo_id].split(' - '))
            if gols_time_casa > gols_anteriores_time_casa:
               #print(f"Gol marcado pelo time da casa: {time_casa}")
                post_tweet(f"Gol marcado pelo time da casa: {time_casa}")
            if gols_visitante > gols_anteriores_visitante:
                post_tweet(f"Gol marcado pelo time visitante: {time_visitante}")
                #print(f"Gol marcado pelo time visitante: {time_visitante}")
        placares_atualizados[jogo_id] = placar

save_current_scores(placares_atualizados)
