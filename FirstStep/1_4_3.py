from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

url = 'https://stepik.org/media/attachments/lesson/209723/5.html '

resp = urlopen(url) # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
table = soup.find_all('td')

sum = 0

for i in table:
    sum += int(re.findall(r'[0-9]{1,4}', str(i))[0])

print(sum)