import execjs

class my_execjs:
    js_file_path=""
    def __init__(self,js_file_path) -> None:
        self.js_file_path=js_file_path

    def call_js(self,funname:str,*args):
        print('funname:',funname)
        # print('args:',args)
        # 生成js环境
        node=execjs.get()
        # 读取js文件
        with open(self.js_file_path,) as f:
            js_code = f.read()
        # 编译js代码
        ctx=node.compile(js_code)
        # 执行
        res=ctx.call(funname,*args)
        return res

