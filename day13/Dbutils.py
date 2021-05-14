import  pymysql

host="localhost"
user="root"
password="root"
database="jason"
def update(sql,parm):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,parm)
    con.commit()
    cursor.close()
    con.close()

def select(sql,parm):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor1 = con.cursor()
    cursor1.execute(sql,parm)
    con.commit()
    return  cursor1.fetchall()
    cursor1.close()
    con.close()








