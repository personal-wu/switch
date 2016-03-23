#__author__ = 'Jonny'
#coding=utf-8

import os
import sys
import Tkinter
import tkFileDialog
from Tkinter import *

root = Tk()
def selectFiles():
    fnameEncode = tkFileDialog.askopenfilenames(filetypes=[('Excel file', '*.xls;*.xlsx')], multiple=1)
    #sysencode = sys.getfilesystemencoding()
    #fnameDecode = fnameEncode.encode(sysencode)
    #fnameTmpArray = root.tk.splitlist(fnameEncode)
    #fnameArray = [unicode(i, encoding=sysencode) for i in fnameTmpArray]
    print fnameEncode

def saveFiles():
    fnameSaved = tkFileDialog.asksaveasfilename(filetypes=[('Excel file', '*.xls;*.xlsx'),('Text document file','*.txt'),('XML file',';*.xml')])
    print fnameSaved

if __name__ == "__main__":
    root.title("文件转换...")
    root.geometry("300x150")
    root.iconbitmap("res/128x128.ico")
    buttonSelect = Button(root, text ="选择文件..", command = selectFiles)
    buttonSelect.pack()

    buttonSave = Button(root, text ="保存..", command = saveFiles)
    buttonSave.pack()
    root.mainloop()