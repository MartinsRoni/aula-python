#Importando Biblioteca depois de instalada
import requests

resposta = requests.get("https://api.github.com")
print(resposta.status_code)  # Saída: 200
