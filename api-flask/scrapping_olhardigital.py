import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://olhardigital.com.br/2024/09/12/pro/ia-teria-encontrado-forma-de-nao-ser-controlada-por-humanos-entenda/'  # Atribuindo url à uma variavel
response = requests.get(url)  # Requisição GET na url

# Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    html_content = response.text  # Armazenando o conteúdo HTML
    print("Página obtida com sucesso!")
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")

# Criando objeto BeutifulSoup, utilizado para navegar pelos elementos HTML
soup = BeautifulSoup(html_content, 'html.parser') 

# 1. Pegando o título da página
title = soup.title.string
print(f"**Título da página:** {title}")

print("------------------------------------------------------")

# 2. Encontrando Todas as Tags de Cabeçalho
for i in range(1,7):
    headers = soup.find_all(f'h{i}')
    for header in headers:
        print(f"h{i}: {header.get_text(strip=True)}")

print("------------------------------------------------------")

# 3. Extraindo Todos os Links
links = soup.find_all('a')
print(f"Total de links encontrados: {len(links)}\n")

for link in links[:10]:  # Exibindo apenas os primeiros 10 links
    href = link.get('href')
    text = link.get_text(strip=True)
    print(f"Texto: {text} | URL: {href}")
