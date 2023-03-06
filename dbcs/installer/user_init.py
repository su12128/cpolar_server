import sqlite3
try:
    
    conn = sqlite3.connect('./sqlite.db',timeout=600000)
    print("连接数据库成功")
except:
    print("连接数据库失败")

# 创建用户表
cour = conn.cursor()

sql_users = '''create table USERS
                (id int primary key not null,
                name text not null,
                password text not null,
                create_time text not null);'''
cour.execute(sql_users)
conn.commit()
print("用户表创建成功")
conn.close()


