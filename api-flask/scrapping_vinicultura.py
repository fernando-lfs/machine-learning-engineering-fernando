import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'  # Atribuindo url à uma variavel
response = requests.get(url)  # Requisição GET na url

# Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    html_content = response.text  # Armazenando o conteúdo HTML
    print("Página obtida com sucesso!")
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")

# Criando objeto BeutifulSoup, utilizado para navegar pelos elementos HTML
soup = BeautifulSoup(html_content, 'html.parser') 

#Encontra a tabela específica pela classe
table = soup.find('table', {'class': 'tb_base tb_dados'})

# Extrai as linhas da tabela
rows = table.find_all('tr')

# Lista para armazenar os dados
data = []

# Itera sobre as linhas e extrai o texto das células
for row in rows:
    cells = row.find_all(['th', 'td'])  # Inclui cabeçalhos (th) e dados (td)
    cells_text = [cell.get_text(strip=True) for cell in cells]
    data.append(cells_text)

# Converte os dados em um DataFrame do pandas
df = pd.DataFrame(data[1:], columns=data[0])  # A linha 0 é cabeçalho
df.head()

