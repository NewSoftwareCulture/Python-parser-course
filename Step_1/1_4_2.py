from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

url = 'https://stepik.org/media/attachments/lesson/209723/4.html'

resp = urlopen(url) # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
table = str(soup.find('table'))

numbers = re.findall(r'[0-9]{1,4}', table)

sum = 0
for i in numbers:
    sum += int(i)

print(sum)