import requests  # Requisição HTTP (acessar página Web)
from bs4 import BeautifulSoup  # Parsing (análise/extração) de conteúdo HTML

# Atribuir determinada url à uma variavel
url = 'https://castbox.fm/channel/XORUME-BACKUP-id5647344?country=br'
# Requisição HTTP do tipo GET para a URL informada, cujo resultado será armazenado na variavel response. 
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida.
if response.status_code == 200:
# Armazena o conteúdo HTML da página na variável html_content
    html_content = response.text
    print('Página obtida com sucesso!')
else:
    print(f'Erro ao acessar a página. Código de status: {response.status_code}')

# Cria um objeto BeautifulSoup, que faz o parsing do conteúdo HTML contido em html_content.
# O segundo argumento 'html.parser' indica qual analisador será usado — aqui, o parser HTML nativo do Python.
# Esse objeto soup permite acessar e manipular elementos da página como se fosse uma estrutura de árvore (por exemplo, buscar tags, textos, atributos etc).
soup = BeautifulSoup(html_content, 'html.parser')

links = soup.find_all('a')

# for link in links:
#     href = link.get('href')
#     text = link.get_text(strip=True)
#     print(href)

with open('links_extraidos_novo.txt', 'w', encoding='utf-8') as file:
    for link in links:
        href = link.get('href')
        text = link.get_text(strip=True)
        if href:
            # Escreve o link e o texto âncora, separados por tabulação
            file.write(f'{text}\t{href}\n')
            print(f'{text}: {href}')