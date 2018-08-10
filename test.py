from xml.dom import minidom
# parse an xml file by name
mydoc = minidom.parse('a.xml')

items = mydoc.getElementsByTagName('coach')

print(items[0].attributes[0].value)
