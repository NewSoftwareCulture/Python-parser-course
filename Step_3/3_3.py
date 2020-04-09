import xmltodict

fin = open('resource/map3.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
nodes = parsedxml['osm']['node']

count = 0
for node in nodes:
    if 'tag' in node:
        tag = node['tag']
        if isinstance(tag, list):
            for i in tag:
                if i['@k'] == "amenity" and i['@v'] == "fuel":
                    count += 1
        else:
            if tag['@k'] == "amenity" and tag['@v'] == "fuel":
                count += 1 

print(count)      