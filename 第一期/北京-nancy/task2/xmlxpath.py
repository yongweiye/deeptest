# -* coding:utf-8 *-
__author__ = 'nancy'

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse("xml_date.xml")
    root = tree.getroot()

    data = root.findall(".")
    for d in data:
        print(d.tag)

    # country node
    # first menthod
    countrys = root.findall(".//country")
    for country in countrys:
        print(country.tag, "--", country.attrib["name"], end="")
    print("")
    # second menthod
    countrys = root.findall("country")
    for country in countrys:
        print(country.tag, "--", country.attrib["name"], end="")
    print("")

    # name  = Panama
    countrys  = root.findall(".//*[@name='Panama']")
    for country in countrys:
        print(country.tag, "--", country.attrib["name"])

    # country name  = Panama  year
    countrys = root.findall(".//country[@name='Panama']/year")
    for year in countrys:
        print(year.text)

    # index find first country
    # index  start from 1
    country = root.findall(".//country[1]")
    for c in country:
        print(c.tag, "--", c.attrib["name"])

    # text find node
    gdppc = root.findall(".//*[gdppc='59900']")
    for g in gdppc:
        print(g.tag)
