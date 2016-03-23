# -*- coding: utf-8 -*- 
import os, sys

def print_lol(list = [], format = '%10r', file_name = sys.stdout):
	for item in list:
		for elem in item:
			print(format % elem, end = '', file = file_name)
		print("", file = file_name)
		#print(format * len(item) % item, file = file_name)

def open_txt(file = 'file.txt'):
	try:
		fsock = open(file ,'r')
		return fsock
	except Exception(e):
		print(str(e))
		
def write_txt(file = 'file.txt'):
	try:
		fsock = open(file ,'w')
		return fsock
	except Exception(e):
		print(str(e))
	
def txt_read(file = 'file.txt'):
	fsock = open_txt(file)
	list = []
	if fsock:
		line = fsock.readline()
		
		while line:
			elem = line.split()
			list.append(elem)
			line = fsock.readline()
	fsock.close()
	return list
	
def txt_write(file = 'file.txt', content = []):
	fsock = write_txt(file)
	print_lol(list = content, file_name = fsock)
	fsock.close()
	