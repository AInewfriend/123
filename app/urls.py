from django.conf.urls import url

# from boke111.urls import urlpatterns
from django.contrib.auth.decorators import login_required

from app import views

urlpatterns =[
    #注册
    url(r'^register/',views.register,name='register'),
    #登录
    url(r'^login/',views.login,name='login'),
    #首页
    url(r'^index/',login_required(views.index),name='index'),
    #退出登录
    url(r'^back_login/',views.back_login,name='back_login'),

]