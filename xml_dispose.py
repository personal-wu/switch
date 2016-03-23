# -*- coding: utf-8 -*- 
from xml.etree import ElementTree


def open_xml(file = 'file.xml'):
	try:
		root = ElementTree.parse(file)
		return root
	except Exception(e):
		print(str(e))
	
def xml_read(file = 'file.xml'):
	root = open_xml(file)
	list = []
	if root:
		lst_node = root.getiterator('elem')
		for node in lst_node:
			values = node.getiterator('value')
			elem = []
			
			for value in values:
				#print value.text
				elem.append(value.text)
				#print value.attrib['xxx']
			
			list.append(elem)
	return list