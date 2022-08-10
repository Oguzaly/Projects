import xml.etree.cElementTree as ET
from xml.dom import minidom #Beatufy Xml için kullanıcaz
import psycopg2

root = ET.Element("ADI")        #Elementin Adı
#obj1= root.append(ET.Element("Objects"))   #Elemente bağlı obje
doc = ET.SubElement(root,"Objects")   #elemente bağlı mappping

obj1= ET.SubElement(doc,"Objects", Action="REGIST",Code = "GroupID",ElementType="Movie",ID="GroupID")
obj2= ET.SubElement(obj1,"Property",Name='Type')
obj2.text ='1'
obj3= ET.SubElement(obj1,"Property",Name='FileUrl')
obj3.text ='ftp://ftp_user:test@172.27.0.226:21//contents/GUID/GroupID-movie.json'
obj4=ET.SubElement(obj1,"Property",Name='ScreenFormat')
obj4.text ='1'
obj5=ET.SubElement(obj1,"Property",Name='Duration')
obj5.text ='10'
obj6=ET.SubElement(obj1,"Property",Name='Definition')
obj6.text ='HD'
obj7=ET.SubElement(obj1,"Property",Name='Encryption')
obj7.text ='1'
tree = ET.ElementTree(root)
tree.write("filename.xml")

map=ET.SubElement(root,"Mappings")
obj1= ET.SubElement(map,"Mapping", Action="REGIST",ElementCode = "GroupID",ElementID = "GroupID",ElementType="Movie",ParentCode="Guid",ParentID="Guid",ParentType="Program")

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")  #Beatify işlemini yapıp kaydeden yer burası
with open("filename.xml", "w") as f:
    version ='<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' # \n alt satıra geç demek
    f.write(version);
    f.write(xmlstr.split('\n', 1)[1])

#Scrip line bt line ne yapıyor yazılmalı , anlaşılmalı
#FOR DONGÜSÜ eklenmeli excelden A kolonundan Guid , b kolunundan label id alınıp ilgili yerlere eklenmeli
#ELEMENTCODE ELEMENTID = GUİD
#parentcode parentid = Label

#Curl ile oluşturulan xml ya da xml ler gönderilmeli
