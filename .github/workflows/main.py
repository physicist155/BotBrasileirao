import tweepy
import os

#Instalattion/Access to Twitter account

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'],os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit = True)

client = tweepy.Client(
    consumer_key = os.environ['CONSUMER_KEY'],
    consumer_secret = os.environ['CONSUMER_SECRET'],
    access_token = os.environ['ACCESS_TOKEN'],
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
)


API_KEY = os.environ.get("API_KEY")

#Função para trocar a foto de perfil da conta
def profile_image(filename):
    api.update_profile_image(filename)

#Função para atualizar informações da conta
def update_profile_info(params):
    api.update_profile(**params)

profile_info = {
    'name': 'Bot (?)',
    'url': 'https://twitter.com/Bot1631973',
    'location': 'São Paulo, Brasil',
    'description': 'Eu ainda não tenho propósito.'
}
#update_profile_info(profile_info)

def post_tweet(text):
    client.create_tweet(text)

def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text,media_ids=[media.media_id_string])
    
texto = "Teste"
client.create_tweet(text = texto)  
