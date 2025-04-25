from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurações do Selenium (modo headless para não abrir a janela do navegador)
options = Options()
options.add_argument('--headless')  # Comente esta linha se quiser ver o navegador funcionando
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Caminho do seu driver do Chrome (verifique a versão instalada do Chrome e o chromedriver)
driver = webdriver.Chrome(options=options)

url = 'https://castbox.fm/channel/XORUME-BACKUP-id5647344?country=br'
driver.get(url)

# Aguarda o carregamento inicial da página
time.sleep(3)

# Simula rolagem até o fim da página para carregar todos os episódios
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Espera o novo conteúdo carregar
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Agora que tudo está carregado, pegue os links
links = driver.find_elements(By.TAG_NAME, "a")

with open('links_extraidos_completos.txt', 'w', encoding='utf-8') as file:
    for link in links:
        href = link.get_attribute('href')
        text = link.text.strip()
        if href:
            file.write(f'{text}\t{href}\n')
            print(f'{text}: {href}')

driver.quit()
