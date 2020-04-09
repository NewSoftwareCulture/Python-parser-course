import xmltodict
import re

path = 'resource/map4.osm'

def get_count(param):
    count = 0
    for node in param:
        if 'tag' in node:
            tag = node['tag']
            if isinstance(tag, list):
                for i in tag:
                    if i['@k'] == "amenity" and i['@v'] == "fuel":
                        count += 1
            else:
                if tag['@k'] == "amenity" and tag['@v'] == "fuel":
                    count += 1 
    return count

fin = open(path, 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
nodes = parsedxml['osm']['node']
ways = parsedxml['osm']['way']

count = get_count(nodes) + get_count(ways)
print(count)      