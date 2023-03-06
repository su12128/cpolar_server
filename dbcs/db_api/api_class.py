import sqlite3


class user_sqlie_api:
    params = {}

    def __init__(self, params: dict) -> None:
        self.params = params
        check_ = self.check()
        assert check_ == True, check_
        print("ok")
        pass

    def check(self):
        keys = list(self.params.keys())
        if (keys.count('name') < 1):
            return "查询用户,但没有指定用户名"
        print(len(self.params["name"].strip()))
        if (len(self.params["name"].strip()) == 0):
            return "用户名为空"
        return True

    def user_select(self):
        conn = sqlite3.connect("./sqlite.db")
        cour =conn.cursor()
        sql_='select * from USERS where '
        for k,v in self.params.items():
            print(k,v,"key and value")
            sql_ = sql_ + f"{k}='{v}' and "
        # print(sql_,'before')
        sql_= sql_[0:-5]+';'
        # print(sql_,"after")
        try:
            rows=cour.execute(sql_)
            # 返回一个列表
            result=[]
            for row in rows:
                result.append(row)
            print(result,"result")

        except:
            raise("查询语句出错，可能是表中没有该属性")
        
        finally:
            conn.close()



if __name__ == "__main__":
    params = {
        "name": "admin1",
        # "password":"admin"
    }
    use = user_sqlie_api(params)
    use.user_select()
