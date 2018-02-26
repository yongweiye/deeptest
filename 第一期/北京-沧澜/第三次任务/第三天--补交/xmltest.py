# -*- coding:utf-8 -*-
__author__ = "张晋"
# 导入ElementTree
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    print("xml解析实例")
    print("---" * 10)
    data = """ <data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
    """
    root = ET.fromstring(data)
    print(root.tag)  # 打印根节点的节点tag，输出data
    print("---" * 10)
    for child in root:
        print(child.tag, '', child.attrib)
    print("---" * 10)
    for child in root.iter("year"):
        print(child.tag, '', child.text)  # 打印出year的tag和text
    print("---" * 10)
    for child in root.iter("year"):
        if child.text == "2011":
            child.text = "2007"
            child.set('updated', 'yes')
    print("将2011 -> 2007")
    for child in root.iter("year"):
        print(child.tag, '', child.text)  # 打印出year的tag和text
    print('---' * 10)
    for child in root.iter("country"):
        wx = ET.SubElement(child, "wx")
        wx.text = "开源优测"
    # 遍历wx节点并打印
    for child in root.iter("wx"):
        print(child.tag, '', child.text)
    # 下面演示删除所有的neighbor节点
    # 当然你自己可以加判断条件删除指定的节点，自行尝试吧
    print("---" * 10)
    for child in root.findall("neighbor"):
        root.remove(child)
        # 保存上述操作后的xml至xml_write_data.xml
    xml_update_data = ET.tostring(root, encoding="unicode")  # 写入xml_write_data.xml
    import codecs

    fp = codecs.open("xml_write_data.xml", "w", "utf-8")

    fp.write(xml_update_data)

    fp.close()
