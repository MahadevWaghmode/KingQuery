#!C:\Users\Mahadev\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type: text/html")
print()

import cgi

form = cgi.FieldStorage()
se =  form.getvalue('music_value')

print("<h1>Form Data : "+ se)