import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/index.html'  # Atribuindo url à uma variavel
response = requests.get(url)  # Requisição GET na url

# Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    html_content = response.text  # Armazenando o conteúdo HTML
    print("Página obtida com sucesso!")
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")

# Lê o conteúdo da página
page_html = response.content

# Faz o parsing do HTML
page_soup = BeautifulSoup(page_html, "html.parser")

# Encontra todos os produtos na página
bookshelf = page_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

# Listas para armazenar os títulos e preços
titles = []
prices = []

for books in bookshelf:
    # Coleta o título do livro
    book_title = books.h3.a["title"]
    # Coleta o preço do livro
    book_price = books.find("p", {"class": "price_color"}).text.strip()

    print("Título do livro: " + book_title)
    print("Preço do livro: " + book_price)
    print("-------")

    titles.append(book_title)
    prices.append(book_price)

# Cria o dataframe do pandas
df_books = pd.DataFrame({'Título do Livro': titles, 'Preço': prices})

# Exibe o dataframe
df_books.head()