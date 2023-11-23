import tweepy

#Instalattion/Acess to Twitter account
consumer_key = 'LYWidG629E3zktPHpiBEtRPR1'
consumer_secret = 'yOyw5n1AXJ5yzW6gg5x8WYbo1pcxn0CjXDNq4PUDEOjipHjPCY'
access_token = '1726243424901206016-lobupBU226FPMjpB6rgfCK1TFUAXe6'
access_token_secret='jYhR8nLC49cXgRvaT8C7XMUZijbwKxtsKbcIQbol5xmWd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

client = tweepy.Client(
    consumer_key = 'LYWidG629E3zktPHpiBEtRPR1',
    consumer_secret = 'yOyw5n1AXJ5yzW6gg5x8WYbo1pcxn0CjXDNq4PUDEOjipHjPCY',
    access_token = '1726243424901206016-lobupBU226FPMjpB6rgfCK1TFUAXe6',
    access_token_secret = 'jYhR8nLC49cXgRvaT8C7XMUZijbwKxtsKbcIQbol5xmWd'
)



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

post_tweet(text="test")