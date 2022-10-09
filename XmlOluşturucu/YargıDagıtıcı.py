import xml.etree.cElementTree as ET
from xml.dom import minidom #Beatufy Xml için kullanıcaz
root = ET.Element("ADI")        #Elementin Adı
root.append(ET.Element("Objects"))   #Elemente bağlı obje
doc = ET.SubElement(root,"Mappings")   #elemente bağlı mappping
ET.SubElement(doc,"Mapping", Action="DELETE",ElementCode = "100009291",ElementID="100009291",ElementType="Program",ParentCode="923-label",ParentID="923-label",ParentType="Category")
tree = ET.ElementTree(root)
tree.write("filename.xml")
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")  #Beatify işlemini yapıp kaydeden yer burası
with open("filename.xml", "w") as f:
    version ='<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' # \n alt satıra geç demek
    f.write(version);
    f.write(xmlstr.split('\n', 1)[1])
#Scrip line bt line ne yapıyor yazılmalı , anlaşılmalı
#FOR DONGÜSÜ eklenmeli excelden A kolonundan Guid , b kolunundan label id alınıp ilgili yerlere eklenmeli
#ELEMENTCODE ELEMENTID = GUİD
#parentcode parentid = Label

#Curl ile oluşturulan xml ya da xml ler gönderilmeli
