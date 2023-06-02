
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from first_app.api_function.api_fun import api_fun
# redirect浏览器重定向
import json
api_fun = api_fun()
def api_(request):
    res={
        'code':200,
        'mes':"success"
    }
    user_name= request.GET.get('user_name')
    user_pwd=request.GET.get('user_pwd')

    if user_name=='admin'and user_pwd=='admin':
        # pass
        request.session['is_login']=True
        request.session['user_level']='1'
        request.session['user_name']='admin'
    print(request.GET.get('user_name'),"1111")
    # print(request.method,"请求方法")# 获取请求方法
    # print(request.META['REMOTE_ADDR'],'客户端IP')#客户端IP地址
    # print(request.GET,"get的请求参数")#获取get的请求参数
    # print(request.POST,"post的请求体的参数")#获取post的请求体的参数
    return HttpResponse(json.dumps(res))


def axios_api(request):
    print("请求方法:",request.method)
    if request.method == "GET":
        cmd = request.GET.get('cmd')
    else:
        cmd = request.POST.get('cmd')
    print(f'cmd:{cmd}')
    if cmd == '1':
        return api_fun.login(request)
    elif cmd == '2':
        return api_fun.visitor_login(request)