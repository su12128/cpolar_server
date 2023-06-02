from django.urls import re_path 
# 版本不同可能需要改成以下形式
# from django.urls import path
# from django.urls import re_path as url
from . import views
from . import api


app_name = 'first_app'

urlpatterns = [
    re_path('', api.axios_api), 
    
]
