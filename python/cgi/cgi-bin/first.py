import os

print ("Content-type:text/html;charset=utf-8")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<title>Hello Word</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word</h2>')
print ("<b>环境变量</b><br>")
print ("<ul>")
for key in os.environ.keys():
    print ("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print ("</ul>")
print ('</body>')
print ('</html>')