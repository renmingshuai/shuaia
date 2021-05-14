#将excel表里的数据写入到数据库
from  Dbutils  import  update

import xlrd

def Excel_to_db():
    xl=xlrd.open_workbook(filename="C:/Users/baba123/Desktop/导入数据.xls",encoding_override=True)
    sheet=xl.sheet_by_name("用户")
    rows=sheet.nrows

    for i in range(1,rows):#将标题之外的其他行写入数据库
      r= sheet.row_values(i)
      sql="insert into  student  values(%s,%s,%s,%s,%s)"
      update(sql,r)
print("添加成功")

Excel_to_db()


