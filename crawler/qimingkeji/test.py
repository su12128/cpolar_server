
import json
import requests
import execjs
import base64
import sys
# print(sys.path)s
import os
import time
# directory_path = os.path.dirname(os.path.abspath(__file__))
# print(directory_path)
# sys.path.append(directory_path)
# print(os.getcwd(),1111)
sys.path.append(os.getcwd())
from crawler.comment.class_execjs import my_execjs
from crawler.comment.handle_sqlite import crawler_sqlite
encrypt_data_url = "https://vipapi.qimingpian.cn/search/recommendedItemList"
heards = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',

}
req_data = {
    'page': 1,
    'num': 20,
    'sys': 'vip',
    'keywords': '',
    'unionid': ''
}
# # print(requests.post(url=encrypt_data_url,heard=heard).json())


def run():

    # # 生成js环境
    node = execjs.get()
    encrypt_data = requests.post(
        url=encrypt_data_url, headers=heards, data=req_data).json()['encrypt_data']
    # print(encrypt_data)
# # 读入js代码
    with open("./qimingkeji/test.js",) as f:
        js_code = f.read()

# # 编译js代码

    ctx = node.compile(js_code)

# # 执行

    res = ctx.call("s", encrypt_data)
    res = json.loads(res)
    # res=ctx.eval(f"s({encrypt_data})")
    print(res)


class crawler_qimingkeji:
    mysqlite = crawler_sqlite()
    encrypt_data_url = "https://vipapi.qimingpian.cn/search/recommendedItemList"
    heards = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',

    }
    req_data = {
        'page': 1,
        'num': 20,
        'sys': 'vip',
        'keywords': '',
        'unionid': ''
    }

    def __init__(self) -> None:
        pass
    # 爬取数据

    def get_encrypt_data(self):
        encrypt_data = requests.post(
            url=self.encrypt_data_url, headers=self.heards, data=self.req_data).json()['encrypt_data']
        return encrypt_data
    def read_encrypt_data(self,encrypt_data):
        execjs_node = my_execjs("./crawler/qimingkeji/test.js")
        data = execjs_node.call_js('s', encrypt_data)
        data = json.loads(data)
        return data

    def set_page(self, page: str):
        self.req_data['page'] = str

    # 存入数据库
    def update_data(self):
        data = self.get_encrypt_data()
        params = {
            'data': data,
            'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            'affiliated_project': '企名科技'
        }
        self.mysqlite.save_data(params=params)


if __name__ == "__main__":
    # print(os.path.abspath())
    qimingkeji = crawler_qimingkeji()
    # print(qimingkeji.get_encrypt_data())
    # run()

    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    qimingkeji.update_data()
    # print(qimingkeji.read_encrypt_data(qimingkeji.get_encrypt_data()))
    # params = {
    #     'data': "data1",
    #     'time': "time1",
    #     'affiliated_project': '企名科技'
    # }
    # keys = params.keys()
    # values = params.values()
    # keys_str = ""
    # values_str = ""
    # for i in keys:
    #     keys_str = keys_str + str(i)+","
    # for i in values:
    #     if len(values_str) == 0 :
    #         values_str =f'\'{str(i)}\''+","
    #     else:
    #         values_str =values_str + f'\'{str(i)}\''+","
    # keys_str = keys_str[0:-1]
    # values_str = values_str[0:-1]
    # print(f"insert into crawler_data({keys_str}) values({values_str});")
