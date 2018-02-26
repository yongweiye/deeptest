# -* coding:utf-8 *-
__author__ = 'nancy'

#import  xml.etree.ElementTree as ET
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree  = ET.parse("xml_date.xml")

    root = tree.getroot()
    print(root.tag)

    for child in root:
        print(child.tag, "name1=", child.attrib["name"])

    # find rand all
    # use iter
    for rank in root.iter("rank"):
        print("use iter:", rank.tag, "--", rank.text)

    # find rand all
    # use findall
    for country in root.findall("country"):
        rank = country.find("rank")
        print("use findall and find:", rank.tag, "--", rank.text)

    #  modify rank text
    for rank in root.iter("rank"):
        rank.text = "modify"
        rank.set('updated', 'yes')
    for rank in root.iter("rank"):
        print(rank.tag, "--", rank.text)

    # add cointry
    for country in root.iter("country"):
        url = ET.Element("url")
        url.text = "urltest"
        country.append(url)
    for rank in root.iter("url"):
       print(rank.tag, " - ", rank.text)

    # delete url
    for country in root.iter("country"):
        url  = country.find("url")

        if url is not None:
            country.remove(url)
            print("delete one url")

    tree.write("xml_date.xml", encoding="utf-8")


