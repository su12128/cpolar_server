import json
from django.http import HttpResponse, JsonResponse
class api_fun:
    def __init__(self) -> None:
        pass
    def login(self,request):
        pass
    def visitor_login(self,request):
        meta = request.META
        for k,v in meta.items():
            print(f"{k}:{v}")
        # print('REMOTE_ADDR,客户端的IP 地址',meta['REMOTE_ADDR'])
        # print('REMOTE_HOST,客户端的主机名',meta['REMOTE_HOST'])
        request.session['user_name'] = 'vistor'
        res={
            'code':200,
            'message':"success",
        }
        return HttpResponse(json.dumps(res))