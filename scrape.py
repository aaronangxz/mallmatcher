import requests
from bs4 import BeautifulSoup

URL = 'https://www.jem.sg/store-level.php?StoreLevel=B1&ResultLimit=88#nothing'
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='storelisting')

job_elems = results.find_all('div',class_ = 'retailerlogo')

#print(results.prettify())

for job_elem in job_elems:
    title_elem = job_elem.find('div')
    print(title_elem.text.strip())
    #print(job_elem,end = '\n'*2)