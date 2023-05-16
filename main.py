import xml.etree.ElementTree as ET
tree = ET.parse('xml.xml')
root = tree.getroot()
for i in root.iter('item'):
    if i[5].text.split()[1] == "15":
        print("Title: " + i[0].text + "\nDescription: " + i[3].text)
        print("---------------------------------------------------")
        
