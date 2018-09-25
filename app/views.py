from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from app.form import UserloginForm, UserForm



#注册
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        #校验页面中传递的参数，是否填写完整
        form = UserForm(request.POST)
        if form.is_valid():
            #获取校验后的用户名和密码
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username,password=password)
            # return  render(request,'register.html')
            # else:
            #     return render(request,'register.html')
            #实现跳转
            return HttpResponseRedirect(reverse('app:login'))
        else:
            return render(request,'register.html',{'form':form})


#登录
def login(request):
    if request.method == 'GET':
        return  render(request,'login.html')

    if request.method == 'POST':
            #表单验证,用户名和密码是否填写，校验用户名是否注册
        form = UserloginForm(request.POST)
        # is_valid():判断表单是否验证通过
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user:
                #用户名和密码是正确的
                #login登录
                auth.login(request,user)
                # return HttpResponseRedirect(reverse('app:index'))

                return render(request,'index.html',{'form':form})
            else:
                #密码不正确
                pass
                return render(request,'login.html',{'error':'密码错误'})


        else:
            return render(request,'login.html',{'form':form})


#博客管理系统
def index(request):
    if request.method == 'GET':
        message = User.objects.last()
        return render(request,'index.html')
    if request.method == 'POST':
        pass

#退出登录
def back_login(request):
    if request.method == 'GET':
        return  HttpResponseRedirect(reverse('app:login'))
