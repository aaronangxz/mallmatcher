import requests
from bs4 import BeautifulSoup

URL = 'https://www.jem.sg/store-category.php?CategoryID=140&StoreLevel=B1'
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='storelisting')

print(results.prettify())