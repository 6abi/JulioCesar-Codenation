import requests
import json
import hashlib

url_token = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8c934a282a945e8b820a06719d3a71dac9d45f51'
request = requests.get(url_token)
resposta = request.json()
arquivo = open('answer.json', "w")
json.dump(resposta, arquivo)
arquivo.close()
msg = resposta['cifrado']
s = ''

for c in msg:
    if chr(ord(c)).isidentifier():
        if (ord(c) - resposta['numero_casas']) < 98:
            s += chr(ord(c) - resposta['numero_casas'] + 27)
        else:
            s += chr(ord(c) - resposta['numero_casas'])
    else:
        s += chr(ord(c))

dados = {
    'numero_casas': resposta['numero_casas'],
    'token': resposta['token'],
    'cifrado': resposta['cifrado'],
    'decifrado': s,
    'resumo_criptografico': hashlib.sha1(s.encode()).hexdigest()
}

arquivo = open('answer.json', "w")
json.dump(dados, arquivo)
arquivo.close()

url = url_token
files = {'answer': open('answer.json', 'rb')}
r = requests.post(url, files=files)
r.text

