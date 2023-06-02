# 单例模式构建数据库连接对象
import sqlite3


def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]
    return _singleton_wrapper


@Singleton
class crawler_sqlite():
    conn = None
    cur = None

    def __init__(self) -> None:
        try:
            self.conn = sqlite3.connect(r'./sqlite.db', timeout=600000)
            self.cur = self.conn.cursor()
            print("数据库连接成功")
        except Exception as e:
            print(e, "数据库连接失败")
            pass

    def sql_excute(self, sql_text):
        self.cur.execute(sql_text)
        self.conn.commit()

    def close(self, sql_text):
        self.conn.close()
        # self.instance={}

    def save_data(self, params):
        keys = params.keys()
        values = params.values()
        keys_str = ""
        values_str = ""
        for i in keys:
            keys_str = keys_str + str(i)+","
        for i in values:
            if len(values_str) == 0 :
                values_str =f'\'{str(i)}\''+","
            else:
                values_str =values_str + f'\'{str(i)}\''+","
        keys_str = keys_str[0:-1]
        values_str = values_str[0:-1]
        print(f'keys_str:{keys_str}')

        sql_statement = f"insert into crawler_data({keys_str}) values({values_str})"
        print(f"sql_statement:{sql_statement}")
        self.sql_excute(sql_statement)


if __name__ == "__main__":
    mysqli = crawler_sqlite()
    user_table = mysqli.cur.execute("SELECT * FROM \"USERS\";")
    # print(user_table)
    for row in user_table:
        for i in range(0, len(row)):
            print(row[i])
