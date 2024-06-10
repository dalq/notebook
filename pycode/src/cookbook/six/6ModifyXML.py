# 解析、修改和重写XML
from xml.etree.ElementTree import parse, Element

doc = parse('./res/pred.xml')
root = doc.getroot()

toIndex = root.getchildren().index(root.find('cr'))
e = Element('spam')
e.text = 'This is a test'
root.insert(toIndex + 1, e)
root.remove(root.find('sri'))
root.remove(root.find('cr'))

doc.write('./res/newpred.xml', xml_declaration=True)