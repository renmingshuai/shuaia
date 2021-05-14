import xlrd
import xlwt
#获取工作簿
wb = xlrd.open_workbook(filename="C:/Users/ThinkPad/Desktop/12月份衣服销售数据.xlsx",encoding_override=True)
#通过wb获取选项卡
sheet = wb.sheet_by_name("12月份各种服饰销售情况")
#获取行，列数据
rows = sheet.nrows #多少行
cols = sheet.ncols #多少列

#各种服饰总金额
yrfzong = 0
nzkzong = 0
fyzong = 0
pczong = 0
txzong = 0
cszong = 0
#各种服饰销售量
yrfl = 0
nzkl = 0
fyl = 0
pcl = 0
txl = 0
csl = 0

for i in range(rows)[1:]:
    # print(sheet.row_values(i)[1])
    if sheet.row_values(i)[1] =="羽绒服":
        yrf = sheet.row_values(i)[2]*sheet.row_values(i)[4]
        yrfzong = yrf+yrfzong
        yrfl = sheet.row_values(i)[4]+yrfl
    elif sheet.row_values(i)[1] =="牛仔裤":
        nzk = sheet.row_values(i)[2]*sheet.row_values(i)[4]
        nzkzong = nzk+nzkzong
        nzkl = sheet.row_values(i)[4]+nzkl
    elif sheet.row_values(i)[1] =="风衣":
        fy = sheet.row_values(i)[2]*sheet.row_values(i)[4]
        fyzong = fy+fyzong
        fyl = sheet.row_values(i)[4]+fyl
    elif sheet.row_values(i)[1] =="皮草":
        pc = sheet.row_values(i)[2]*sheet.row_values(i)[4]
        pczong =pc+pczong
        pcl = sheet.row_values(i)[4]+pcl
    elif sheet.row_values(i)[1] =="T血":
        tx = sheet.row_values(i)[2]*sheet.row_values(i)[4]
        txzong = tx+txzong
        txl = sheet.row_values(i)[4]+txl
    else:
        cs = sheet.row_values(i)[2]*sheet.row_values(i)[4]
        cszong = cs+cszong
        csl = sheet.row_values(i)[4]+csl

#总销售金额
zje = yrfzong+nzkzong+txzong+cszong+fyzong+pczong
#日平均销售量
zxsl = round((yrfl+nzkl+txl+pcl+fyl+csl)/30,2)
#各服饰销售占比
ryfpj = round(yrfl/zxsl*100,2)
nzkpj = round(nzkl/zxsl*100,2)
fypj = round(fyl/zxsl*100,2)
pcpj = round(pcl/zxsl*100,2)
txpj = round(txl/zxsl*100,2)
cspj = round(csl/zxsl*100,2)

# 添加
wb1 = xlwt.Workbook(encoding="utf-8")

sheet1 = wb1.add_sheet("总数据")
#设置列宽
sheet1.col(0).width = 256 * 20
sheet1.col(3).width = 256 * 20
sheet1.col(4).width = 256 * 20

for i in range(rows):
    for j in range(cols):
        z= sheet.cell_value(i,j)
        sheet1.write(i,j,z)
sheet1.write(32,0,"总销售额："+str(zje))
sheet1.write(32,3,"日平均销量"+str(zxsl))
sheet1.write(32,4,"羽绒服销售占比"+str(ryfpj))
sheet1.write(33,4,"牛仔裤销售占比"+str(nzkpj))
sheet1.write(34,4,"风衣销售占比"+str(fypj))
sheet1.write(35,4,"皮草销售占比"+str(pcpj))
sheet1.write(36,4,"T恤销售占比"+str(txpj))
sheet1.write(37,4,"衬衫销售占比"+str(cspj))

sheet2 = wb1.add_sheet("羽绒服")
sheet2.write(0,0,"名称")
sheet2.write(0,1,"本月销售量")
sheet2.write(1,0,"羽绒服")
sheet2.write(1,1,yrfl)

sheet3 = wb1.add_sheet("牛仔裤")
sheet3.write(0,0,"名称")
sheet3.write(0,1,"本月销售量")
sheet3.write(1,0,"牛仔裤")
sheet3.write(1,1,nzkl)

sheet4 = wb1.add_sheet("风衣")
sheet4.write(0,0,"名称")
sheet4.write(0,1,"本月销售量")
sheet4.write(1,0,"风衣")
sheet4.write(1,1,fyl)

sheet5 = wb1.add_sheet("皮草")
sheet5.write(0,0,"名称")
sheet5.write(0,1,"本月销售量")
sheet5.write(1,0,"皮草")
sheet5.write(1,1,pcl)

sheet6 = wb1.add_sheet("T血")
sheet6.write(0,0,"名称")
sheet6.write(0,1,"本月销售量")
sheet6.write(1,0,"T恤")
sheet6.write(1,1,txl)

sheet7 = wb1.add_sheet("衬衫")
sheet7.write(0,0,"名称")
sheet7.write(0,1,"本月销售量")
sheet7.write(1,0,"衬衫")
sheet7.write(1,1,csl)

# 保存
wb1.save("12月作业销售.xls")
