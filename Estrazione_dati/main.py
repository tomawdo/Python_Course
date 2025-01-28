from bs4 import BeautifulSoup
import requests

url = 'https://www.star-consulting.it/post/beautiful-soup' # l'URL del sito web da cui desideri estrarre dati

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'): # 'a' è il tag che indica un hyperlink

    print(link.get('href'))