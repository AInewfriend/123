from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    #检验注册信息
    username = forms.CharField(required=True,max_length=5,min_length=2,)
    password = forms.CharField(required=True,min_length=6,)
    password2 = forms.CharField(required=True,min_length=6,)
    def clean(self):
        #校验密码和确认密码是否相同
        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if user:
            #如果已经注册过
            raise forms.ValidationError({'username':'用户名已存在，请直接登录或者重新注册'})
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password':'两次密码不一致'})
        return self.cleaned_data


class UserloginForm(forms.Form):
    # 检验注册信息
    username = forms.CharField(required=True, max_length=5, min_length=2,)
    password = forms.CharField(required=True, min_length=6,)
    def clean(self):
        #检验用户是否注册
        user = User.objects.filter(username=self.cleaned_data['username'])
        if not user:
            raise forms.ValidationError({'username':'请先注册再来登录'})
        return self.cleaned_data



