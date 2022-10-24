#!C:\Users\acer\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi

import cgitb
cgitb.enable()

#輸出http header
print("Content-type:text/html\n")
#輸出html
print('<html><head><meta charset="utf-8">')
print('<title>Hello Word</title></head>')
print('<body>')
print('<h2>Hello Word ! 你好嗎 ?</h2>')
print('</body></html>')