import pymysql

host = "localhost"
user = "root"
password = "root"
databases = "jason"
class DBUtils():


    def Update(self,sql, param):
        # 获取数据库连接
        con = pymysql.connect(host=host, user=user, password=password, database=databases)
        # 创建控制台
        cursor = con.cursor()
        # 执行sql
        cursor.execute(sql, param)
        # 提交
        con.commit()
        # 关闭
        cursor.close()
        con.close()

    def Select(self,sql, param):
        # 获取数据库连接
        con = pymysql.connect(host=host, user=user, password=password, database=databases)
        # 创建控制台
        cursor = con.cursor()
        # 执行sql
        cursor.execute(sql, param)
        # 提交
        con.commit()
        # 获取数据
        return cursor.fetchall()
        # 关闭
        cursor.close()
        con.close()