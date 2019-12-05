from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput())
    phone = forms.CharField(label='手机号码')
class Login(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
class Uppassword(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    phone = forms.CharField(label='手机号码', max_length=11)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput())
class Upphone(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    phone = forms.CharField(label='手机号码', max_length=11)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
class Radio(forms.Form):
    radio = forms.CharField(label='分类',max_length=10)