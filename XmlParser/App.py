from xml.etree import ElementTree as ET
import re
from openpyxl import Workbook,load_workbook
#ET.fromstring(open('C:/Users/HP/Desktop/playground/XmlParser/2.xml').read())
count = input('Count of Xml : ')
count = int(count)
ara =input('date : ')
with open('C:/Users/HP/Desktop/playground/XmlParser/xmlparse.csv','a') as f:
    for i in range(1,count+1):
        print(i)
        tree =ET.parse('C:/Users/HP/Desktop/playground/XmlParser/xml/{}.xml'.format(i))
        root=tree.getroot()
        for x in root.findall('programme'):
            epgcode= x.attrib['Ericsson_ProgramId']
            starttime =x.attrib['start']
            trimstarttime = starttime.replace(ara,'').replace('+0000','')
            stoptime =x.attrib['stop']
            trimstoptime = stoptime.replace(ara,'').replace('+0000','')
            if re.search(ara,epgcode):
                print(epgcode,' ',trimstarttime,' ',trimstoptime,' ',type(epgcode))
                f.write('{}'.format(i)+','+'{}'.format(epgcode)+','+'{}'.format(trimstarttime)+','+'{}'.format(trimstoptime)+'\n')


#
#
#
# print(ET.fromstring(root))
#
# print(root.tag)
# print(root[0].tag)
# print(root[0].attrib)
#
# for x in root[0]:
#     print(x.tag,x.attrib)
# for x in root[0]:
#     print(x.text)
#
