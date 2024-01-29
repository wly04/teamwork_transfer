
import pymysql

# 连接数据库
db = pymysql.connect(
    host = "localhost",
    user = "root",
    database = "love_doreen",
    password = "WuLiuYu20040706"
)

cursor = db.cursor()
db.select_db("love_doreen")

# 创建用户表单
try:
    tablename = "user"
    sql = "CREATE TABLE %s (id integer not null auto_increment, name varchar(20) not null, email varchar(20), password varchar(20) not null, primary key(id))"%(tablename)
    cursor.execute(sql)
except Exception as e:
    print(e)
    # db.rollback()

def create_user(name:str, email:str, password:str):
    try:
        sql = "INSERT INTO user(name, email, password) values(%s, %s, %s)"
        values = (name, email, password)
        cursor.execute(sql, values)
        db.commit()
    except Exception:
        return False, "注册失败，请检查信息是否正确，谢谢"
    else:
        return True, "创建用户成功"

def query_user(email:str):
    try:
        sql = "SELECT * FROM user WHERE `email` = %s"
        values = (email)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        return result
        print("查询到所有符合的记录是", result)
    except:
        return "查询失败，无法查询该数据"

# 查询已导入论文粗略信息
def query_literature():
    sql = "SELECT `AU`, `TI` FROM `artical_data_copy1` LIMIT %s, %s"
    values = (0, 5)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    dic = {}
    num1 = 0
    for row in result:
        dic[num1] = row
        num1 += 1
    print(dic)


cursor.close()
db.close()
