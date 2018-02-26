# -* coding:utf-8 *-
__author__ = 'nancy'

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os

# xml文件操作类
class xmlop():
    def __init__(self, xmlpath):
        if os.path.exists(xmlpath):
            self.xmlpath  = xmlpath
        else:
            raise "xml file not exit"

    def get_xml_data(self, page, element):
        '''
        获取xml数据，传入二级、三级节点名称，以字典格式返回元素信息
        :param page:二级节点名称
                lement:三级节点名称
        :return: 返回元素信息
        '''
        try:
            tree = ET.parse(self.xmlpath)
            root = tree.getroot()
            a = root.find(page)
            b = a.find(element)
            return b.attrib
        except Exception as e:
            print(e)
