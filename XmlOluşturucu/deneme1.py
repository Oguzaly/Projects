import xml.etree.ElementTree as ET
tree = ET.parse('xml.xml')
root = tree.getroot()

print(root)
