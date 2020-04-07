import requests
url = 'https://stepik.org/media/attachments/lesson/209717/1.html'

r = requests.get(url)  
r.encoding = 'utf8'
page = r.text

count_c = page.count('C++')
count_py = page.count('Python')

if count_c >= count_py:
    print('C++')
else:
    print('Python')