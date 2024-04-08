from bs4 import BeautifulSoup
import requests

# result = requests.get("https://www.google.com/")
# print(result.status_code)
# content=result.text

# soup=BeautifulSoup(content, "lxml")

# print(soup.find_all("div"))

website = 'https://subslikescript.com/movie/Titanic-120338'

result=requests.get(website)
content = result.text
#print(result.text)
soup = BeautifulSoup(content, "lxml")
#print(soup.prettify())
box = soup.find('article', class_='main-article')
title = soup.find('h1').get_text()
print(title)
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
# print(transcript)

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
