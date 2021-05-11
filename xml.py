import xml.etree.ElementTree as ET

def convertToDict(root):
    data = {}
    for item in root.findall('*'):
        for child in item:
            data[child.tag] = child.text
            
    return data


def main():
    result = []
    dataList = []
    tree =  ET.parse('opnsense.xml')
    
    root = tree.getroot()
    #print(root)
    
    for item in root.findall('.//rule'):
        #print(item)
        data = {}
        if len(item):
            for subitem in item:

                if len(subitem):
                    subdata = {}
                    for super_sub_item in subitem:
                        subdata[super_sub_item.tag] = super_sub_item.text
                    data[subitem.tag] = subdata
                else :
                    
                    data[subitem.tag] = subitem.text
        else :
            data[item.tag] = item.text
           
        dataList.append(data)
    
    print(dataList)
    
        
if __name__ == "__main__":
    main()