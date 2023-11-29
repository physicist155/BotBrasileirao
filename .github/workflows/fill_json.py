import os
import json

# Cria um dicionário com os valores das variáveis de ambiente
json_content = {
    "type": "service_account",
    "project_id": "bot-brasileirao",
    "private_key_id": os.getenv('PRIVATE_KEY_ID'),
    "private_key": os.getenv('PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.getenv('CLIENT_EMAIL'),
    "client_id": os.getenv('CLIENT_ID'),
    "auth_uri": os.getenv('AUTH_URI'),
    "token_uri": os.getenv('TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL'),
    "universe_domain": os.getenv('UNIVERSE_DOMAIN')
}

# Escreve o dicionário em um arquivo JSON
with open('service_account.json', 'w') as json_file:
    json.dump(json_content, json_file, indent=4)
