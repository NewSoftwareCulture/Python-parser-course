import requests
import re
from collections import Counter
from bs4 import BeautifulSoup

url = 'https://stepik.org/media/attachments/lesson/209719/2.html'

def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'
    return str(BeautifulSoup(r.text, 'lxml'))

def get_mass(html):
    mass = re.findall(r'<code>[A-z]*</code>', html)
    i = 0
    while i < len(mass):
        mass[i] = mass[i].replace('<code>', '').replace('</code>', '')
        i += 1
    return mass

def get_max_value_elements(mass):
    count = Counter(mass)
    max_v = str(max(count.values()))
    mass = []

    for i in count.keys():
        if str(count[i]) == max_v:
            mass.append(i)
    return mass
    
html = get_html(url)
mass = get_max_value_elements(get_mass(html))
mass.sort()

makeitastring = " ".join(str(x) for x in mass)
print(makeitastring)