from  DBUtils import  update
from  DBUtils import  select
sql="insert into  bank  values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
parm=["avc","11","123","cn","cn","sds","ads",0,"123"]


#update(sql,parm)
sql1="select * from bank where username=%s"
parm1=["tFq7OJU6"]
date=select(sql1,parm1)
print(date)