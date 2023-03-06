
from django.http import HttpResponse
from django.shortcuts import redirect
# redirect浏览器重定向

def api_(request):
    res={
        'code':200,
        'mes':"相应内容"
    }
    print(request.method,"请求方法")# 获取请求方法
    print(request.GET,"get的请求参数")#获取get的请求参数
    # print(request.POST,"post的请求体的参数")#获取post的请求体的参数
    return HttpResponse(request,"32434")
