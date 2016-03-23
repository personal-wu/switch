import sys
import excel_dispose
import xml_dispose
import txt_dispose
	
def main():
	#test excel
	tables = excel_dispose.excel_table_read_byindex(file = "1.xlsx")
	#print(tables)
	#excel_dispose.excel_table_write_byindex(file = 'excel_result.xls', content = tables)
	
	#test txt
	#txt_dispose.print_lol(tables)
	#txt_dispose.txt_write(content = tables, file = '1.txt')
	
	#test xml
	#write TODO
	
	#tables = excel_table_read_byname(file = "1.xlsx")
	#for row in tables:
	#	print row	

if __name__=="__main__":
	main()