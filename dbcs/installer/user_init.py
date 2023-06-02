import sqlite3
try:

    conn = sqlite3.connect('./sqlite.db', timeout=600000)
    print("连接数据库成功")
except:
    print("连接数据库失败")

# 创建用户表
cour = conn.cursor()

sql_users = '''create table USERS
                (id INTEGER PRIMARY KEY   AUTOINCREMENT,
                name text not null,
                password text not null,
                create_time text not null);'''
sql_crawler = '''
    create table crawler
    (
    id INTEGER PRIMARY KEY   AUTOINCREMENT,
    project_name text not null,
    note text,
    build_time text
    );
'''
sql_crawler_data='''
    create table crawler_data(
    id INTEGER PRIMARY KEY   AUTOINCREMENT,
    data text,
    time text,
    affiliated_project text,
    foreign key (affiliated_project) references crawler(project_name)
    );
'''
sql_crawler_setting='''
create table crawler_setting(
    id INTEGER PRIMARY KEY   AUTOINCREMENT,
    name text not null,
    value text,
    affiliated_project text not null,
    foreign key (affiliated_project) references craawler(project_name)
    );
'''
# cour.execute(sql_users)
cour.execute(sql_crawler)
cour.execute(sql_crawler_data)
cour.execute(sql_crawler_setting)
conn.commit()
print("用户表创建成功")
conn.close()
