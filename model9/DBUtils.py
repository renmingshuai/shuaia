import  pymysql
host="localhost"
user="root"
password="root"
database="jason"
#针对增删改
def  update(sql,parm):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()

    cursor.execute(sql,parm)
    con.commit()
    cursor.close()
    con.close()


#针对查询
def select(sql,parm):

    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,parm)
    con.commit()
    return  cursor.fetchall()
    cursor.close()
    con.close()
