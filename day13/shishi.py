from  Dbutils import  select

import  xlwt
student=[]

def Db_to_excel():
    sql="select * from student"
    parm=[]
    user=select(sql,parm)
    for i in user:
        i=list(i)
        student.append(i)

    xw=xlwt.Workbook()
    sheet=xw.add_sheet("数据")
    title = ['编号', '姓名', '男', '年龄', 'dep编号']
    i = 0
    # 循环将表头写入到sheet页
    for header in title:
        sheet.write(0, i, header)
        i += 1
    # 写数据
    for row in range(1, len(student) + 1):
        for col in range(0, len(student[row - 1])):
            sheet.write(row, col, student[row - 1][col])
            col += 1
        row += 1
    xw.save("导入数据.xls")
    print("导入成功")
Db_to_excel()
