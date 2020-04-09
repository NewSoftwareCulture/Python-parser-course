import xmltodict

fin = open('resource/map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
to_print = parsedxml['osm']['node']

yes = 0
no = 0
for i in to_print:
    if 'tag' in i:
        yes += 1
    else:
        no += 1

print(str(yes) + ' ' + str(no))