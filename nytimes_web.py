import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.nytimes.com')
soup = BeautifulSoup(webpage.text, 'lxml')

for heading in soup.find_all("h2", class_="e1voiwgp0"):
    if heading.h2:
        print(heading.h2.text.replace_with("\n", ' '.strip('<>')))
    else:
        print(heading.string)

