import pymysql  
pymysql.install_as_MySQLdb()  
  
db = pymysql.connect("localhost",'root','','py_second')  
  
cursor = db.cursor()  
  
cursor.execute('SELECT VERSION()')  
  
data = cursor.fetchone()  
  
print("Version is %s" % data)  
  
db.close()  